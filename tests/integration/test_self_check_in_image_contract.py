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
    / "senior-zero-self-check"
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
    / "Senior Zero Self Check.desktop"
)


class SelfCheckInImageContractTests(unittest.TestCase):
    def test_required_files_exist(self) -> None:
        self.assertTrue(SCRIPT.exists(), f"Missing self-check script: {SCRIPT}")
        self.assertTrue(DESKTOP_FILE.exists(), f"Missing self-check desktop entry: {DESKTOP_FILE}")

    def test_script_contract(self) -> None:
        text = read_text(SCRIPT)
        ok, missing = contains_all(
            text,
            [
                "SENIOR_ZERO_SELF_CHECK_DRY_RUN",
                "SENIOR_ZERO_SELF_CHECK_FAKE",
                "check_preflight=",
                "check_update_policy=",
                "check_runtime_profile=",
                "check_diagnostics_report=",
                "SENIOR_ZERO_SELF_CHECK_RESULTS=",
                "SENIOR_ZERO_SELF_CHECK_OK",
                "SENIOR_ZERO_SELF_CHECK_ATTENTION",
            ],
        )
        self.assertTrue(ok, f"Missing self-check contract entries: {missing}")

    def test_desktop_entry_targets_self_check(self) -> None:
        text = read_text(DESKTOP_FILE)
        ok, missing = contains_all(
            text,
            [
                "Type=Application",
                "Name=Senior Zero Self Check",
                "Exec=lxterminal -e senior-zero-self-check",
            ],
        )
        self.assertTrue(ok, f"Self-check desktop entry mismatch: {missing}")


if __name__ == "__main__":
    unittest.main()
