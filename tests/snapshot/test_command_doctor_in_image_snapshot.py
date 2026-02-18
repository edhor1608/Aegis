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
    / "senior-zero-command-doctor"
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
    / "Senior Zero Command Doctor.desktop"
)
SNAP_DIR = REPO_ROOT / "tests" / "snapshots"


class CommandDoctorInImageSnapshotTests(unittest.TestCase):
    def test_script_snapshot(self) -> None:
        actual = normalize_markdown(read_text(SCRIPT))
        expected = normalize_markdown(read_text(SNAP_DIR / "command-doctor-script.snap"))
        self.assertEqual(actual, expected, "Snapshot mismatch for command-doctor script")

    def test_desktop_entry_snapshot(self) -> None:
        actual = normalize_markdown(read_text(DESKTOP_FILE))
        expected = normalize_markdown(read_text(SNAP_DIR / "desktop-entry-command-doctor.snap"))
        self.assertEqual(actual, expected, "Snapshot mismatch for command-doctor desktop entry")


if __name__ == "__main__":
    unittest.main()
