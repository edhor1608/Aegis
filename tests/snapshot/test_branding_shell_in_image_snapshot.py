from pathlib import Path
import unittest

from tests.lib.markdown_checks import normalize_markdown, read_text


REPO_ROOT = Path(__file__).resolve().parents[2]
INCLUDES = REPO_ROOT / "build" / "live-build" / "config" / "includes.chroot"
HOOKS = REPO_ROOT / "build" / "live-build" / "config" / "hooks" / "normal"
SNAP_DIR = REPO_ROOT / "tests" / "snapshots"

BRANDING_SCRIPT = INCLUDES / "usr" / "local" / "bin" / "senior-zero-branding-apply"
AUTOSTART_FILE = INCLUDES / "etc" / "xdg" / "autostart" / "senior-zero-branding.desktop"
WALLPAPER_FILE = INCLUDES / "usr" / "share" / "senior-zero" / "branding" / "aegis-wallpaper.svg"
ISSUE_FILE = INCLUDES / "etc" / "issue"
OS_RELEASE_HOOK = HOOKS / "6100-brand-os-release.hook.chroot"


class BrandingShellInImageSnapshotTests(unittest.TestCase):
    def _assert_snapshot(self, target_file: Path, snapshot_name: str) -> None:
        actual = normalize_markdown(read_text(target_file))
        expected = normalize_markdown(read_text(SNAP_DIR / snapshot_name))
        self.assertEqual(actual, expected, f"Snapshot mismatch for {target_file}")

    def test_branding_script_snapshot(self) -> None:
        self._assert_snapshot(BRANDING_SCRIPT, "branding-apply-script.snap")

    def test_branding_autostart_snapshot(self) -> None:
        self._assert_snapshot(AUTOSTART_FILE, "branding-autostart-desktop.snap")

    def test_wallpaper_snapshot(self) -> None:
        self._assert_snapshot(WALLPAPER_FILE, "branding-wallpaper.snap")

    def test_issue_snapshot(self) -> None:
        self._assert_snapshot(ISSUE_FILE, "branding-issue.snap")

    def test_os_release_hook_snapshot(self) -> None:
        self._assert_snapshot(OS_RELEASE_HOOK, "brand-os-release-hook.snap")


if __name__ == "__main__":
    unittest.main()
