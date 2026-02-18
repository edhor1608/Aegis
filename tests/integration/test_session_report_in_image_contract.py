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
    / "senior-zero-session-report"
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
    / "Senior Zero Session Report.desktop"
)


class SessionReportInImageContractTests(unittest.TestCase):
    def test_required_files_exist(self) -> None:
        self.assertTrue(SCRIPT.exists(), f"Missing session-report script: {SCRIPT}")
        self.assertTrue(DESKTOP_FILE.exists(), f"Missing session-report desktop entry: {DESKTOP_FILE}")

    def test_script_contract(self) -> None:
        text = read_text(SCRIPT)
        ok, missing = contains_all(
            text,
            [
                "SENIOR_ZERO_SESSION_REPORT_DRY_RUN",
                "SENIOR_ZERO_SESSION_REPORT_FAKE",
                "section_update_check=",
                "section_network_check=",
                "section_storage_check=",
                "section_runtime_profile=",
                "section_self_check=",
                "SENIOR_ZERO_SESSION_REPORT_WRITTEN=",
                "SENIOR_ZERO_SESSION_REPORT_READY",
                "SENIOR_ZERO_SESSION_REPORT_PARTIAL",
            ],
        )
        self.assertTrue(ok, f"Missing session-report contract entries: {missing}")

    def test_desktop_entry_targets_session_report(self) -> None:
        text = read_text(DESKTOP_FILE)
        ok, missing = contains_all(
            text,
            [
                "Type=Application",
                "Name=Senior Zero Session Report",
                "Exec=lxterminal -e senior-zero-session-report",
            ],
        )
        self.assertTrue(ok, f"Session-report desktop entry mismatch: {missing}")


if __name__ == "__main__":
    unittest.main()
