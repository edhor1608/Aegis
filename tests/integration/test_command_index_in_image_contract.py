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
    / "senior-zero-command-index"
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
    / "Senior Zero Command Index.desktop"
)


class CommandIndexInImageContractTests(unittest.TestCase):
    def test_required_files_exist(self) -> None:
        self.assertTrue(SCRIPT.exists(), f"Missing command-index script: {SCRIPT}")
        self.assertTrue(DESKTOP_FILE.exists(), f"Missing command-index desktop entry: {DESKTOP_FILE}")

    def test_script_contract(self) -> None:
        text = read_text(SCRIPT)
        ok, missing = contains_all(
            text,
            [
                "SENIOR_ZERO_COMMAND_INDEX_DRY_RUN",
                "SENIOR_ZERO_COMMAND_INDEX_FAKE",
                "cmd_preflight_report=",
                "cmd_update_check=",
                "cmd_runtime_profile=",
                "cmd_network_check=",
                "cmd_storage_check=",
                "cmd_self_check=",
                "SENIOR_ZERO_COMMAND_INDEX_READY",
                "SENIOR_ZERO_COMMAND_INDEX_PARTIAL",
            ],
        )
        self.assertTrue(ok, f"Missing command-index contract entries: {missing}")

    def test_desktop_entry_targets_command_index(self) -> None:
        text = read_text(DESKTOP_FILE)
        ok, missing = contains_all(
            text,
            [
                "Type=Application",
                "Name=Senior Zero Command Index",
                "Exec=lxterminal -e senior-zero-command-index",
            ],
        )
        self.assertTrue(ok, f"Command-index desktop entry mismatch: {missing}")


if __name__ == "__main__":
    unittest.main()
