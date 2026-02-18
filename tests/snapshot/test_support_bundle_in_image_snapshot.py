from pathlib import Path
import unittest

from tests.lib.markdown_checks import normalize_markdown, read_text


REPO_ROOT = Path(__file__).resolve().parents[2]
SCRIPT = (
    REPO_ROOT
    / "build"
    / "live-build"
    / "config"
    / "includes.chroot"
    / "usr"
    / "local"
    / "bin"
    / "senior-zero-support-bundle"
)
DESKTOP_FILE = (
    REPO_ROOT
    / "build"
    / "live-build"
    / "config"
    / "includes.chroot"
    / "etc"
    / "skel"
    / "Desktop"
    / "Senior Zero Support Bundle.desktop"
)
SNAP_DIR = REPO_ROOT / "tests" / "snapshots"


class SupportBundleInImageSnapshotTests(unittest.TestCase):
    def test_script_snapshot(self) -> None:
        actual = normalize_markdown(read_text(SCRIPT))
        expected = normalize_markdown(read_text(SNAP_DIR / "support-bundle-script.snap"))
        self.assertEqual(actual, expected, "Snapshot mismatch for support-bundle script")

    def test_desktop_entry_snapshot(self) -> None:
        actual = normalize_markdown(read_text(DESKTOP_FILE))
        expected = normalize_markdown(read_text(SNAP_DIR / "desktop-entry-support-bundle.snap"))
        self.assertEqual(actual, expected, "Snapshot mismatch for support-bundle desktop entry")


if __name__ == "__main__":
    unittest.main()
