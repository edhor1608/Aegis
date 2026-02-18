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
    / "senior-zero-support-bundle"
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
    / "Senior Zero Support Bundle.desktop"
)


class SupportBundleInImageContractTests(unittest.TestCase):
    def test_required_files_exist(self) -> None:
        self.assertTrue(SCRIPT.exists(), f"Missing support-bundle script: {SCRIPT}")
        self.assertTrue(DESKTOP_FILE.exists(), f"Missing support-bundle desktop entry: {DESKTOP_FILE}")

    def test_script_contract(self) -> None:
        text = read_text(SCRIPT)
        ok, missing = contains_all(
            text,
            [
                "SENIOR_ZERO_SUPPORT_BUNDLE_DRY_RUN",
                "SENIOR_ZERO_SUPPORT_BUNDLE_FAKE",
                "included_checks=preflight_report,security_audit,network_check,storage_check,update_check",
                "check_preflight_report=",
                "check_security_audit=",
                "check_network_check=",
                "check_storage_check=",
                "check_update_check=",
                "SENIOR_ZERO_SUPPORT_BUNDLE_WRITTEN=",
                "SENIOR_ZERO_SUPPORT_BUNDLE_READY",
                "SENIOR_ZERO_SUPPORT_BUNDLE_PARTIAL",
            ],
        )
        self.assertTrue(ok, f"Missing support-bundle contract entries: {missing}")

    def test_desktop_entry_targets_support_bundle(self) -> None:
        text = read_text(DESKTOP_FILE)
        ok, missing = contains_all(
            text,
            [
                "Type=Application",
                "Name=Senior Zero Support Bundle",
                "Exec=lxterminal -e senior-zero-support-bundle",
            ],
        )
        self.assertTrue(ok, f"Support-bundle desktop entry mismatch: {missing}")


if __name__ == "__main__":
    unittest.main()
