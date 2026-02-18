from pathlib import Path
import unittest

from tests.lib.markdown_checks import contains_all, read_text


REPO_ROOT = Path(__file__).resolve().parents[2]
INCLUDES = REPO_ROOT / "build" / "live-build" / "config" / "includes.chroot"
SCRIPT = INCLUDES / "usr" / "local" / "sbin" / "senior-zero-app-center-policy"
CURATED = INCLUDES / "etc" / "senior-zero" / "app-center" / "curated-default-packages.txt"
WARNING = INCLUDES / "etc" / "senior-zero" / "app-center" / "more-apps-warning.txt"


class AppCenterPolicyInImageContractTests(unittest.TestCase):
    def test_required_files_exist(self) -> None:
        self.assertTrue(SCRIPT.exists(), f"Missing in-image app-center policy script: {SCRIPT}")
        self.assertTrue(CURATED.exists(), f"Missing curated app list: {CURATED}")
        self.assertTrue(WARNING.exists(), f"Missing more-apps warning text: {WARNING}")

    def test_script_contract_entries(self) -> None:
        text = read_text(SCRIPT)
        ok, missing = contains_all(
            text,
            [
                "SENIOR_ZERO_APP_CENTER_POLICY_DRY_RUN",
                "/etc/senior-zero/app-center/curated-default-packages.txt",
                "/etc/senior-zero/app-center/more-apps-warning.txt",
                "SENIOR_ZERO_APP_CENTER_POLICY_PASS",
            ],
        )
        self.assertTrue(ok, f"Missing app-center policy script entries: {missing}")

    def test_curated_default_list_contains_seed_apps(self) -> None:
        curated_text = read_text(CURATED)
        ok, missing = contains_all(
            curated_text,
            [
                "firefox-esr",
                "thunderbird",
                "libreoffice",
                "vlc",
            ],
        )
        self.assertTrue(ok, f"Missing curated seed apps: {missing}")

    def test_warning_text_mentions_curated_and_more_apps(self) -> None:
        warning_text = read_text(WARNING)
        ok, missing = contains_all(
            warning_text,
            [
                "curated",
                "More Apps",
                "warning",
            ],
        )
        self.assertTrue(ok, f"Missing warning semantics: {missing}")


if __name__ == "__main__":
    unittest.main()
