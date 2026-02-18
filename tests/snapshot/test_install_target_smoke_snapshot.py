from pathlib import Path
import unittest

from tests.lib.markdown_checks import normalize_markdown, read_text


REPO_ROOT = Path(__file__).resolve().parents[2]
SNAP_DIR = REPO_ROOT / "tests" / "snapshots"
SCRIPT = REPO_ROOT / "scripts" / "install_target_smoke.sh"


class InstallTargetSmokeSnapshotTests(unittest.TestCase):
    def test_install_target_smoke_script_snapshot(self) -> None:
        actual = normalize_markdown(read_text(SCRIPT))
        expected = normalize_markdown(read_text(SNAP_DIR / "install-target-smoke-script.snap"))
        self.assertEqual(actual, expected, "Snapshot mismatch for install_target_smoke.sh")


if __name__ == "__main__":
    unittest.main()
