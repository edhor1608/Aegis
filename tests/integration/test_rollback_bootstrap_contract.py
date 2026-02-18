from pathlib import Path
import unittest

from tests.lib.markdown_checks import contains_all, read_text


REPO_ROOT = Path(__file__).resolve().parents[2]
INCLUDES = REPO_ROOT / "build" / "live-build" / "config" / "includes.chroot"
BOOTSTRAP_SCRIPT = INCLUDES / "usr" / "local" / "sbin" / "senior-zero-rollback-bootstrap"
BOOTSTRAP_SERVICE = INCLUDES / "etc" / "systemd" / "system" / "senior-zero-rollback-bootstrap.service"
BOOTSTRAP_WANTS = (
    INCLUDES
    / "etc"
    / "systemd"
    / "system"
    / "multi-user.target.wants"
    / "senior-zero-rollback-bootstrap.service"
)


class RollbackBootstrapContractTests(unittest.TestCase):
    def test_required_bootstrap_files_exist(self) -> None:
        required = [BOOTSTRAP_SCRIPT, BOOTSTRAP_SERVICE, BOOTSTRAP_WANTS]
        missing = [str(path) for path in required if not path.exists()]
        self.assertEqual(missing, [], f"Missing files: {missing}")

    def test_bootstrap_script_contains_btrfs_snapper_flow(self) -> None:
        text = read_text(BOOTSTRAP_SCRIPT)
        ok, missing = contains_all(
            text,
            [
                "findmnt -n -o FSTYPE /",
                "snapper create-config /",
                "awk 'NR>1 {print $2}'",
                "systemctl enable --now snapper-timeline.timer",
                "systemctl enable --now snapper-cleanup.timer",
                "/var/lib/senior-zero/rollback-bootstrap.done",
                "BOOTSTRAP_PASS",
            ],
        )
        self.assertTrue(ok, f"Missing bootstrap flow entries: {missing}")

    def test_bootstrap_service_executes_script_once(self) -> None:
        text = read_text(BOOTSTRAP_SERVICE)
        ok, missing = contains_all(
            text,
            [
                "Type=oneshot",
                "ExecStart=/usr/local/sbin/senior-zero-rollback-bootstrap",
                "ConditionPathExists=!/var/lib/senior-zero/rollback-bootstrap.done",
                "WantedBy=multi-user.target",
            ],
        )
        self.assertTrue(ok, f"Missing bootstrap service entries: {missing}")

    def test_bootstrap_wants_is_symlink(self) -> None:
        self.assertTrue(BOOTSTRAP_WANTS.is_symlink(), f"Expected symlink: {BOOTSTRAP_WANTS}")
        target = BOOTSTRAP_WANTS.readlink().as_posix()
        self.assertEqual(target, "../senior-zero-rollback-bootstrap.service")


if __name__ == "__main__":
    unittest.main()
