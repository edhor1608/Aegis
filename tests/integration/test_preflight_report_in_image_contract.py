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
    / "sbin"
    / "senior-zero-preflight-report"
)


class PreflightReportInImageContractTests(unittest.TestCase):
    def test_script_exists(self) -> None:
        self.assertTrue(SCRIPT.exists(), f"Missing in-image preflight report script: {SCRIPT}")

    def test_script_covers_runtime_checks(self) -> None:
        text = read_text(SCRIPT)
        ok, missing = contains_all(
            text,
            [
                "SENIOR_ZERO_PREFLIGHT_REPORT_DRY_RUN",
                "networkmanager_active",
                "unattended_upgrades_enabled",
                "locale_en_us_present",
                "locale_de_de_present",
                "snapper_available",
                "btrfs_available",
                "SENIOR_ZERO_PREFLIGHT_REPORT_PASS",
            ],
        )
        self.assertTrue(ok, f"Missing preflight report entries: {missing}")


if __name__ == "__main__":
    unittest.main()
