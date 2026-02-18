from pathlib import Path
import unittest

from tests.lib.markdown_checks import normalize_markdown, read_text


REPO_ROOT = Path(__file__).resolve().parents[2]
DESKTOP_FILE = (
    REPO_ROOT
    / "build"
    / "live-build"
    / "config"
    / "includes.chroot"
    / "etc"
    / "skel"
    / "Desktop"
    / "Senior Zero Acceptance Runner.desktop"
)
SNAP_DIR = REPO_ROOT / "tests" / "snapshots"


class AcceptanceDesktopEntryInImageSnapshotTests(unittest.TestCase):
    def test_desktop_entry_snapshot(self) -> None:
        actual = normalize_markdown(read_text(DESKTOP_FILE))
        expected = normalize_markdown(read_text(SNAP_DIR / "desktop-entry-acceptance-runner.snap"))
        self.assertEqual(actual, expected, "Snapshot mismatch for acceptance desktop entry")


if __name__ == "__main__":
    unittest.main()
