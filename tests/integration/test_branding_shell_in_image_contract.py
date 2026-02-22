from pathlib import Path
import unittest

from tests.lib.markdown_checks import contains_all, read_text


REPO_ROOT = Path(__file__).resolve().parents[2]
INCLUDES = REPO_ROOT / "build" / "live-build" / "config" / "includes.chroot"
HOOKS = REPO_ROOT / "build" / "live-build" / "config" / "hooks" / "normal"

BRANDING_SCRIPT = INCLUDES / "usr" / "local" / "bin" / "senior-zero-branding-apply"
AUTOSTART_FILE = INCLUDES / "etc" / "xdg" / "autostart" / "senior-zero-branding.desktop"
WALLPAPER_FILE = INCLUDES / "usr" / "share" / "senior-zero" / "branding" / "aegis-wallpaper.svg"
ISSUE_FILE = INCLUDES / "etc" / "issue"
OS_RELEASE_HOOK = HOOKS / "6100-brand-os-release.hook.chroot"


class BrandingShellInImageContractTests(unittest.TestCase):
    def test_required_files_exist(self) -> None:
        required = [BRANDING_SCRIPT, AUTOSTART_FILE, WALLPAPER_FILE, ISSUE_FILE, OS_RELEASE_HOOK]
        missing = [str(path) for path in required if not path.exists()]
        self.assertEqual(missing, [], f"Missing branding assets: {missing}")

    def test_branding_script_contract(self) -> None:
        text = read_text(BRANDING_SCRIPT)
        ok, missing = contains_all(
            text,
            [
                "SENIOR_ZERO_BRANDING_DRY_RUN",
                "SENIOR_ZERO_BRANDING_APPLIED",
                "/usr/share/senior-zero/branding/aegis-wallpaper.svg",
                "pcmanfm --set-wallpaper",
            ],
        )
        self.assertTrue(ok, f"Missing branding script entries: {missing}")

    def test_autostart_contract(self) -> None:
        text = read_text(AUTOSTART_FILE)
        ok, missing = contains_all(
            text,
            [
                "Type=Application",
                "Name=Aegis Session Branding",
                "Exec=senior-zero-branding-apply",
                "OnlyShowIn=LXDE;",
            ],
        )
        self.assertTrue(ok, f"Branding autostart mismatch: {missing}")

    def test_issue_banner_is_branded(self) -> None:
        text = read_text(ISSUE_FILE)
        ok, missing = contains_all(
            text,
            [
                "Aegis Linux",
                "Senior-friendly secure desktop",
            ],
        )
        self.assertTrue(ok, f"Branded issue banner missing entries: {missing}")

    def test_os_release_hook_contract(self) -> None:
        text = read_text(OS_RELEASE_HOOK)
        ok, missing = contains_all(
            text,
            [
                "/usr/lib/os-release",
                "PRETTY_NAME=\"Aegis Linux\"",
                "NAME=\"Aegis\"",
                "ID=aegis",
            ],
        )
        self.assertTrue(ok, f"OS release branding hook missing entries: {missing}")
        self.assertNotIn(
            'cp "$TARGET" /etc/os-release',
            text,
            "Hook must not copy os-release over itself when /etc/os-release links to /usr/lib/os-release",
        )


if __name__ == "__main__":
    unittest.main()
