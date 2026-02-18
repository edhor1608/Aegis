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
    / "senior-zero-daily-checklist"
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
    / "Senior Zero Daily Checklist.desktop"
)


class DailyChecklistInImageContractTests(unittest.TestCase):
    def test_required_files_exist(self) -> None:
        self.assertTrue(SCRIPT.exists(), f"Missing daily-checklist script: {SCRIPT}")
        self.assertTrue(DESKTOP_FILE.exists(), f"Missing daily-checklist desktop entry: {DESKTOP_FILE}")

    def test_script_contract(self) -> None:
        text = read_text(SCRIPT)
        ok, missing = contains_all(
            text,
            [
                "SENIOR_ZERO_DAILY_CHECKLIST_DRY_RUN",
                "SENIOR_ZERO_DAILY_CHECKLIST_FAKE",
                "checklist_items=network,updates,storage,help",
                "item_network=",
                "item_updates=",
                "item_storage=",
                "item_help=",
                "SENIOR_ZERO_DAILY_CHECKLIST_WRITTEN=",
                "SENIOR_ZERO_DAILY_CHECKLIST_READY",
                "SENIOR_ZERO_DAILY_CHECKLIST_PARTIAL",
            ],
        )
        self.assertTrue(ok, f"Missing daily-checklist contract entries: {missing}")

    def test_desktop_entry_targets_daily_checklist(self) -> None:
        text = read_text(DESKTOP_FILE)
        ok, missing = contains_all(
            text,
            [
                "Type=Application",
                "Name=Senior Zero Daily Checklist",
                "Exec=lxterminal -e senior-zero-daily-checklist",
            ],
        )
        self.assertTrue(ok, f"Daily-checklist desktop entry mismatch: {missing}")


if __name__ == "__main__":
    unittest.main()
