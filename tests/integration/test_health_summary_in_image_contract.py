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
    / "senior-zero-health-summary"
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
    / "Senior Zero Health Summary.desktop"
)


class HealthSummaryInImageContractTests(unittest.TestCase):
    def test_required_files_exist(self) -> None:
        self.assertTrue(SCRIPT.exists(), f"Missing health summary script: {SCRIPT}")
        self.assertTrue(DESKTOP_FILE.exists(), f"Missing health summary desktop entry: {DESKTOP_FILE}")

    def test_script_contract(self) -> None:
        text = read_text(SCRIPT)
        ok, missing = contains_all(
            text,
            [
                "SENIOR_ZERO_HEALTH_SUMMARY_DRY_RUN",
                "networkmanager_active",
                "unattended_upgrades_enabled",
                "preflight_command_available",
                "app_center_policy_available",
                "language_switch_available",
                "SENIOR_ZERO_HEALTHY",
                "SENIOR_ZERO_ATTENTION_REQUIRED",
            ],
        )
        self.assertTrue(ok, f"Missing health summary contract entries: {missing}")

    def test_desktop_entry_targets_health_summary(self) -> None:
        text = read_text(DESKTOP_FILE)
        ok, missing = contains_all(
            text,
            [
                "Name=Senior Zero Health Summary",
                "Exec=lxterminal -e senior-zero-health-summary",
            ],
        )
        self.assertTrue(ok, f"Health summary desktop entry mismatch: {missing}")


if __name__ == "__main__":
    unittest.main()
