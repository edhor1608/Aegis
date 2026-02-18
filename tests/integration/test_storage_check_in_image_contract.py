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
    / "senior-zero-storage-check"
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
    / "Senior Zero Storage Check.desktop"
)


class StorageCheckInImageContractTests(unittest.TestCase):
    def test_required_files_exist(self) -> None:
        self.assertTrue(SCRIPT.exists(), f"Missing storage-check script: {SCRIPT}")
        self.assertTrue(DESKTOP_FILE.exists(), f"Missing storage-check desktop entry: {DESKTOP_FILE}")

    def test_script_contract(self) -> None:
        text = read_text(SCRIPT)
        ok, missing = contains_all(
            text,
            [
                "SENIOR_ZERO_STORAGE_CHECK_DRY_RUN",
                "SENIOR_ZERO_STORAGE_CHECK_FAKE",
                "btrfs_command_available=",
                "snapper_command_available=",
                "root_fs_is_btrfs=",
                "root_usage_percent=",
                "SENIOR_ZERO_STORAGE_CHECK_OK",
                "SENIOR_ZERO_STORAGE_CHECK_ATTENTION",
            ],
        )
        self.assertTrue(ok, f"Missing storage-check contract entries: {missing}")

    def test_desktop_entry_targets_storage_check(self) -> None:
        text = read_text(DESKTOP_FILE)
        ok, missing = contains_all(
            text,
            [
                "Type=Application",
                "Name=Senior Zero Storage Check",
                "Exec=lxterminal -e senior-zero-storage-check",
            ],
        )
        self.assertTrue(ok, f"Storage-check desktop entry mismatch: {missing}")


if __name__ == "__main__":
    unittest.main()
