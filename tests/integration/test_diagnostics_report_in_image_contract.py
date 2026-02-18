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
    / "senior-zero-diagnostics-report"
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
    / "Senior Zero Diagnostics Report.desktop"
)


class DiagnosticsReportInImageContractTests(unittest.TestCase):
    def test_required_files_exist(self) -> None:
        self.assertTrue(SCRIPT.exists(), f"Missing diagnostics-report script: {SCRIPT}")
        self.assertTrue(DESKTOP_FILE.exists(), f"Missing diagnostics-report desktop entry: {DESKTOP_FILE}")

    def test_script_contract(self) -> None:
        text = read_text(SCRIPT)
        ok, missing = contains_all(
            text,
            [
                "SENIOR_ZERO_DIAGNOSTICS_REPORT_DRY_RUN",
                "SENIOR_ZERO_DIAGNOSTICS_REPORT_FAKE",
                "SENIOR_ZERO_DIAGNOSTICS_REPORT_V1",
                "timestamp_utc=",
                "user=",
                "locale=",
                "networkmanager_active=",
                "unattended_upgrades_enabled=",
                "memory_total_mb=",
                "memory_available_mb=",
                "SENIOR_ZERO_DIAGNOSTICS_REPORT_WRITTEN=",
            ],
        )
        self.assertTrue(ok, f"Missing diagnostics-report contract entries: {missing}")

    def test_desktop_entry_targets_diagnostics_report(self) -> None:
        text = read_text(DESKTOP_FILE)
        ok, missing = contains_all(
            text,
            [
                "Type=Application",
                "Name=Senior Zero Diagnostics Report",
                "Exec=lxterminal -e senior-zero-diagnostics-report",
            ],
        )
        self.assertTrue(ok, f"Diagnostics-report desktop entry mismatch: {missing}")


if __name__ == "__main__":
    unittest.main()
