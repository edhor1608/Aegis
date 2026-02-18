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
    / "senior-zero-update-check"
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
    / "Senior Zero Update Check.desktop"
)


class UpdateCheckInImageContractTests(unittest.TestCase):
    def test_required_files_exist(self) -> None:
        self.assertTrue(SCRIPT.exists(), f"Missing update-check script: {SCRIPT}")
        self.assertTrue(DESKTOP_FILE.exists(), f"Missing update-check desktop entry: {DESKTOP_FILE}")

    def test_script_contract(self) -> None:
        text = read_text(SCRIPT)
        ok, missing = contains_all(
            text,
            [
                "SENIOR_ZERO_UPDATE_CHECK_DRY_RUN",
                "SENIOR_ZERO_UPDATE_CHECK_FAKE",
                "policy_file=/etc/apt/preferences.d/90-senior-zero-security.pref",
                "unattended_service=unattended-upgrades",
                "security_pin_present=",
                "unattended_upgrades_enabled=",
                "apt_update_required_for_fresh_data",
                "SENIOR_ZERO_UPDATE_CHECK_OK",
                "SENIOR_ZERO_UPDATE_CHECK_ATTENTION",
            ],
        )
        self.assertTrue(ok, f"Missing update-check contract entries: {missing}")

    def test_desktop_entry_targets_update_check(self) -> None:
        text = read_text(DESKTOP_FILE)
        ok, missing = contains_all(
            text,
            [
                "Type=Application",
                "Name=Senior Zero Update Check",
                "Exec=lxterminal -e senior-zero-update-check",
            ],
        )
        self.assertTrue(ok, f"Update-check desktop entry mismatch: {missing}")


if __name__ == "__main__":
    unittest.main()
