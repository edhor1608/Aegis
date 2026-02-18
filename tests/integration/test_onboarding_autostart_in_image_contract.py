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


class OnboardingAutostartInImageContractTests(unittest.TestCase):
    def test_files_exist(self) -> None:
        self.assertTrue(SCRIPT.exists(), f"Missing onboarding script: {SCRIPT}")
        self.assertTrue(AUTOSTART.exists(), f"Missing onboarding autostart file: {AUTOSTART}")

    def test_onboarding_script_contract(self) -> None:
        text = read_text(SCRIPT)
        ok, missing = contains_all(
            text,
            [
                "SENIOR_ZERO_ONBOARDING_DRY_RUN",
                "SENIOR_ZERO_ONBOARDING_SHOWN",
                "SENIOR_ZERO_ONBOARDING_ALREADY_DONE",
                "welcome.txt",
                "onboarding.done",
            ],
        )
        self.assertTrue(ok, f"Missing onboarding script entries: {missing}")

    def test_autostart_targets_onboarding_script(self) -> None:
        text = read_text(AUTOSTART)
        ok, missing = contains_all(
            text,
            [
                "Type=Application",
                "Name=Senior Zero Onboarding",
                "Exec=senior-zero-onboarding",
                "X-GNOME-Autostart-enabled=true",
            ],
        )
        self.assertTrue(ok, f"Autostart entry mismatch: {missing}")


if __name__ == "__main__":
    unittest.main()
