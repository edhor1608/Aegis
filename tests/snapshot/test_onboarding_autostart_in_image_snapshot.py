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
    / "senior-zero-onboarding"
)
AUTOSTART = (
    REPO_ROOT
    / "build"
    / "live-build"
    / "config"
    / "includes.chroot"
    / "etc"
    / "xdg"
    / "autostart"
    / "senior-zero-onboarding.desktop"
)
SNAP_DIR = REPO_ROOT / "tests" / "snapshots"


class OnboardingAutostartInImageSnapshotTests(unittest.TestCase):
    def test_script_snapshot(self) -> None:
        actual = normalize_markdown(read_text(SCRIPT))
        expected = normalize_markdown(read_text(SNAP_DIR / "onboarding-script.snap"))
        self.assertEqual(actual, expected, "Snapshot mismatch for onboarding script")

    def test_autostart_snapshot(self) -> None:
        actual = normalize_markdown(read_text(AUTOSTART))
        expected = normalize_markdown(read_text(SNAP_DIR / "onboarding-autostart.snap"))
        self.assertEqual(actual, expected, "Snapshot mismatch for onboarding autostart desktop file")


if __name__ == "__main__":
    unittest.main()
