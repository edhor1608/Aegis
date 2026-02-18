from pathlib import Path
import unittest

from tests.lib.markdown_checks import contains_all, read_text


REPO_ROOT = Path(__file__).resolve().parents[2]
DESKTOP_FILE = (
    REPO_ROOT
    / "build"
    / "live-build"
    / "config"
    / "includes.chroot"
    / "etc"
    / "skel"
    / "Desktop"
    / "Senior Zero Acceptance Runner.desktop"
)


class AcceptanceDesktopEntryInImageContractTests(unittest.TestCase):
    def test_desktop_file_exists(self) -> None:
        self.assertTrue(DESKTOP_FILE.exists(), f"Missing acceptance desktop entry: {DESKTOP_FILE}")

    def test_desktop_entry_contract(self) -> None:
        text = read_text(DESKTOP_FILE)
        ok, missing = contains_all(
            text,
            [
                "Type=Application",
                "Name=Senior Zero Acceptance Runner",
                "Exec=lxterminal -e senior-zero-acceptance-runner --dry-run",
            ],
        )
        self.assertTrue(ok, f"Acceptance desktop entry mismatch: {missing}")


if __name__ == "__main__":
    unittest.main()
