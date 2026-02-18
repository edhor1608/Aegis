from pathlib import Path
import unittest

from tests.lib.markdown_checks import contains_all, read_text


REPO_ROOT = Path(__file__).resolve().parents[2]
SCRIPT = REPO_ROOT / "scripts" / "install_target_smoke.sh"


class InstallTargetSmokeContractTests(unittest.TestCase):
    def test_script_exists(self) -> None:
        self.assertTrue(SCRIPT.exists(), f"Missing script: {SCRIPT}")

    def test_script_has_install_target_checks(self) -> None:
        text = read_text(SCRIPT)
        ok, missing = contains_all(
            text,
            [
                "findmnt -n -o FSTYPE /",
                "systemctl is-enabled unattended-upgrades",
                "/etc/apt/apt.conf.d/52unattended-upgrades-senior-zero",
                "/etc/apt/preferences.d/90-senior-zero-security.pref",
                "systemctl is-enabled snapper-timeline.timer",
                "systemctl is-enabled snapper-cleanup.timer",
                "/var/lib/senior-zero/rollback-bootstrap.done",
                "locale -a",
                "de_DE.utf8",
                "en_US.utf8",
                "INSTALL_TARGET_SMOKE_PASS",
            ],
        )
        self.assertTrue(ok, f"Missing install-target smoke checks: {missing}")


if __name__ == "__main__":
    unittest.main()
