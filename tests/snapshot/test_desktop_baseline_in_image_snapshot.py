from pathlib import Path
import unittest

from tests.lib.markdown_checks import normalize_markdown, read_text


REPO_ROOT = Path(__file__).resolve().parents[2]
INCLUDES = REPO_ROOT / "build" / "live-build" / "config" / "includes.chroot"
DESKTOP_DIR = INCLUDES / "etc" / "skel" / "Desktop"
SNAP_DIR = REPO_ROOT / "tests" / "snapshots"
HELP_FILE = INCLUDES / "usr" / "share" / "senior-zero" / "help" / "welcome.txt"


class DesktopBaselineInImageSnapshotTests(unittest.TestCase):
    def test_browser_desktop_entry_snapshot(self) -> None:
        actual = normalize_markdown(read_text(DESKTOP_DIR / "Senior Zero Browser.desktop"))
        expected = normalize_markdown(read_text(SNAP_DIR / "desktop-entry-browser.snap"))
        self.assertEqual(actual, expected, "Snapshot mismatch for Senior Zero Browser desktop entry")

    def test_documents_desktop_entry_snapshot(self) -> None:
        actual = normalize_markdown(read_text(DESKTOP_DIR / "Senior Zero Documents.desktop"))
        expected = normalize_markdown(read_text(SNAP_DIR / "desktop-entry-documents.snap"))
        self.assertEqual(actual, expected, "Snapshot mismatch for Senior Zero Documents desktop entry")

    def test_health_desktop_entry_snapshot(self) -> None:
        actual = normalize_markdown(read_text(DESKTOP_DIR / "Senior Zero Health.desktop"))
        expected = normalize_markdown(read_text(SNAP_DIR / "desktop-entry-health.snap"))
        self.assertEqual(actual, expected, "Snapshot mismatch for Senior Zero Health desktop entry")

    def test_help_text_snapshot(self) -> None:
        actual = normalize_markdown(read_text(HELP_FILE))
        expected = normalize_markdown(read_text(SNAP_DIR / "help-welcome.snap"))
        self.assertEqual(actual, expected, "Snapshot mismatch for welcome help text")


if __name__ == "__main__":
    unittest.main()
