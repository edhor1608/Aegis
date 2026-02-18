from pathlib import Path
import unittest

from tests.lib.markdown_checks import contains_all, read_text


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
    / "senior-zero-launcher"
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
    / "Senior Zero Launcher.desktop"
)


class SimpleLauncherInImageContractTests(unittest.TestCase):
    def test_required_files_exist(self) -> None:
        self.assertTrue(SCRIPT.exists(), f"Missing simple launcher script: {SCRIPT}")
        self.assertTrue(DESKTOP_FILE.exists(), f"Missing simple launcher desktop entry: {DESKTOP_FILE}")

    def test_script_contract(self) -> None:
        text = read_text(SCRIPT)
        ok, missing = contains_all(
            text,
            [
                "SENIOR_ZERO_LAUNCHER_DRY_RUN",
                "action_browser=firefox-esr",
                "action_mail=thunderbird",
                "action_documents=libreoffice --writer",
                "action_media=vlc",
                "action_help=xdg-open $HELP_FILE",
                "action_health=senior-zero-health-summary",
                "SENIOR_ZERO_LAUNCHER_INVALID_ACTION",
                "SENIOR_ZERO_LAUNCHER_ACTION_EXECUTED",
            ],
        )
        self.assertTrue(ok, f"Missing simple launcher contract entries: {missing}")

    def test_desktop_entry_targets_simple_launcher(self) -> None:
        text = read_text(DESKTOP_FILE)
        ok, missing = contains_all(
            text,
            [
                "Type=Application",
                "Name=Senior Zero Launcher",
                "Exec=lxterminal -e senior-zero-launcher",
            ],
        )
        self.assertTrue(ok, f"Simple launcher desktop entry mismatch: {missing}")


if __name__ == "__main__":
    unittest.main()
