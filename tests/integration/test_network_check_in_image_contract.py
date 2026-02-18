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
    / "senior-zero-network-check"
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
    / "Senior Zero Network Check.desktop"
)


class NetworkCheckInImageContractTests(unittest.TestCase):
    def test_required_files_exist(self) -> None:
        self.assertTrue(SCRIPT.exists(), f"Missing network-check script: {SCRIPT}")
        self.assertTrue(DESKTOP_FILE.exists(), f"Missing network-check desktop entry: {DESKTOP_FILE}")

    def test_script_contract(self) -> None:
        text = read_text(SCRIPT)
        ok, missing = contains_all(
            text,
            [
                "SENIOR_ZERO_NETWORK_CHECK_DRY_RUN",
                "SENIOR_ZERO_NETWORK_CHECK_FAKE",
                "networkmanager_active=",
                "default_route_present=",
                "dns_resolution_ok=",
                "internet_ping_ok=",
                "SENIOR_ZERO_NETWORK_CHECK_OK",
                "SENIOR_ZERO_NETWORK_CHECK_ATTENTION",
            ],
        )
        self.assertTrue(ok, f"Missing network-check contract entries: {missing}")

    def test_desktop_entry_targets_network_check(self) -> None:
        text = read_text(DESKTOP_FILE)
        ok, missing = contains_all(
            text,
            [
                "Type=Application",
                "Name=Senior Zero Network Check",
                "Exec=lxterminal -e senior-zero-network-check",
            ],
        )
        self.assertTrue(ok, f"Network-check desktop entry mismatch: {missing}")


if __name__ == "__main__":
    unittest.main()
