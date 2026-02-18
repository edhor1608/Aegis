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
    / "senior-zero-language-switch"
)


class LanguageSwitchHelperInImageContractTests(unittest.TestCase):
    def test_script_exists(self) -> None:
        self.assertTrue(SCRIPT.exists(), f"Missing language switch helper: {SCRIPT}")

    def test_script_supports_dry_run_and_targets(self) -> None:
        text = read_text(SCRIPT)
        ok, missing = contains_all(
            text,
            [
                "SENIOR_ZERO_LANGUAGE_SWITCH_DRY_RUN",
                "--to en",
                "--to de",
                "--print-current",
                "en_US.UTF-8",
                "de_DE.UTF-8",
                "SENIOR_ZERO_LANGUAGE_SWITCH_APPLIED",
            ],
        )
        self.assertTrue(ok, f"Language switch helper missing entries: {missing}")


if __name__ == "__main__":
    unittest.main()
