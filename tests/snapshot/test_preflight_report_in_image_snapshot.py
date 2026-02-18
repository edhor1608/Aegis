from pathlib import Path
import unittest

from tests.lib.markdown_checks import normalize_markdown, read_text


REPO_ROOT = Path(__file__).resolve().parents[2]
SNAP_DIR = REPO_ROOT / "tests" / "snapshots"
SCRIPT = (
    REPO_ROOT
    / "build"
    / "live-build"
    / "config"
    / "includes.chroot"
    / "usr"
    / "local"
    / "sbin"
    / "senior-zero-preflight-report"
)


class PreflightReportInImageSnapshotTests(unittest.TestCase):
    def test_script_snapshot(self) -> None:
        actual = normalize_markdown(read_text(SCRIPT))
        expected = normalize_markdown(read_text(SNAP_DIR / "preflight-report-in-image-script.snap"))
        self.assertEqual(actual, expected, "Snapshot mismatch for in-image preflight report script")


if __name__ == "__main__":
    unittest.main()
