from pathlib import Path
import unittest

from tests.lib.markdown_checks import normalize_markdown, read_text


REPO_ROOT = Path(__file__).resolve().parents[2]
SNAP_DIR = REPO_ROOT / "tests" / "snapshots"
INCLUDES = REPO_ROOT / "build" / "live-build" / "config" / "includes.chroot"


class RollbackBootstrapSnapshotTests(unittest.TestCase):
    def _assert_snapshot(self, target_file: Path, snapshot_name: str) -> None:
        actual = normalize_markdown(read_text(target_file))
        expected = normalize_markdown(read_text(SNAP_DIR / snapshot_name))
        self.assertEqual(actual, expected, f"Snapshot mismatch for {target_file}")

    def test_bootstrap_script_snapshot(self) -> None:
        self._assert_snapshot(
            INCLUDES / "usr" / "local" / "sbin" / "senior-zero-rollback-bootstrap",
            "rollback-bootstrap-script.snap",
        )

    def test_bootstrap_service_snapshot(self) -> None:
        self._assert_snapshot(
            INCLUDES / "etc" / "systemd" / "system" / "senior-zero-rollback-bootstrap.service",
            "rollback-bootstrap-service.snap",
        )


if __name__ == "__main__":
    unittest.main()
