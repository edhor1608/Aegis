from pathlib import Path
import unittest

from tests.lib.markdown_checks import contains_all, read_text


REPO_ROOT = Path(__file__).resolve().parents[2]
INCLUDES = REPO_ROOT / "build" / "live-build" / "config" / "includes.chroot"
DESKTOP_DIR = INCLUDES / "etc" / "skel" / "Desktop"
HELP_FILE = INCLUDES / "usr" / "share" / "senior-zero" / "help" / "welcome.txt"

DESKTOP_FILES = {
    "Senior Zero Browser.desktop": [
        "Type=Application",
        "Name=Senior Zero Browser",
        "Exec=firefox-esr",
    ],
    "Senior Zero Documents.desktop": [
        "Type=Application",
        "Name=Senior Zero Documents",
        "Exec=libreoffice",
    ],
    "Senior Zero Help.desktop": [
        "Type=Application",
        "Name=Senior Zero Help",
        "Exec=lxterminal -e less /usr/share/senior-zero/help/welcome.txt",
    ],
    "Senior Zero Health.desktop": [
        "Type=Application",
        "Name=Senior Zero Health",
        "Exec=lxterminal -e senior-zero-preflight-report",
    ],
}


class DesktopBaselineInImageContractTests(unittest.TestCase):
    def test_desktop_files_and_help_exist(self) -> None:
        missing = [str(DESKTOP_DIR / name) for name in DESKTOP_FILES if not (DESKTOP_DIR / name).exists()]
        if not HELP_FILE.exists():
            missing.append(str(HELP_FILE))
        self.assertEqual(missing, [], f"Missing desktop baseline assets: {missing}")

    def test_desktop_entries_have_expected_execs(self) -> None:
        failures = []
        for filename, expected_entries in DESKTOP_FILES.items():
            text = read_text(DESKTOP_DIR / filename)
            ok, missing = contains_all(text, expected_entries)
            if not ok:
                failures.append((filename, missing))
        self.assertEqual(failures, [], f"Desktop entry mismatches: {failures}")

    def test_help_file_contains_baseline_guidance(self) -> None:
        text = read_text(HELP_FILE)
        ok, missing = contains_all(
            text,
            [
                "Senior Zero Linux",
                "Browser",
                "Documents",
                "Health",
                "DE/EN",
            ],
        )
        self.assertTrue(ok, f"Help content missing required guidance: {missing}")


if __name__ == "__main__":
    unittest.main()
