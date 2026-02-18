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
    / "senior-zero-command-doctor"
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
    / "Senior Zero Command Doctor.desktop"
)


class CommandDoctorInImageContractTests(unittest.TestCase):
    def test_required_files_exist(self) -> None:
        self.assertTrue(SCRIPT.exists(), f"Missing command-doctor script: {SCRIPT}")
        self.assertTrue(DESKTOP_FILE.exists(), f"Missing command-doctor desktop entry: {DESKTOP_FILE}")

    def test_script_contract(self) -> None:
        text = read_text(SCRIPT)
        ok, missing = contains_all(
            text,
            [
                "SENIOR_ZERO_COMMAND_DOCTOR_DRY_RUN",
                "SENIOR_ZERO_COMMAND_DOCTOR_FAKE",
                "required_commands=senior-zero-preflight-report,senior-zero-security-audit,senior-zero-network-check,senior-zero-storage-check,senior-zero-self-check,senior-zero-support-bundle,senior-zero-daily-checklist",
                "command_senior_zero_preflight_report=",
                "command_senior_zero_security_audit=",
                "command_senior_zero_network_check=",
                "command_senior_zero_storage_check=",
                "command_senior_zero_self_check=",
                "command_senior_zero_support_bundle=",
                "command_senior_zero_daily_checklist=",
                "SENIOR_ZERO_COMMAND_DOCTOR_WRITTEN=",
                "SENIOR_ZERO_COMMAND_DOCTOR_READY",
                "SENIOR_ZERO_COMMAND_DOCTOR_PARTIAL",
            ],
        )
        self.assertTrue(ok, f"Missing command-doctor contract entries: {missing}")

    def test_desktop_entry_targets_command_doctor(self) -> None:
        text = read_text(DESKTOP_FILE)
        ok, missing = contains_all(
            text,
            [
                "Type=Application",
                "Name=Senior Zero Command Doctor",
                "Exec=lxterminal -e senior-zero-command-doctor",
            ],
        )
        self.assertTrue(ok, f"Command-doctor desktop entry mismatch: {missing}")


if __name__ == "__main__":
    unittest.main()
