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
    / "senior-zero-runtime-profile"
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
    / "Senior Zero Runtime Profile.desktop"
)


class RuntimeProfileInImageContractTests(unittest.TestCase):
    def test_required_files_exist(self) -> None:
        self.assertTrue(SCRIPT.exists(), f"Missing runtime profile script: {SCRIPT}")
        self.assertTrue(DESKTOP_FILE.exists(), f"Missing runtime profile desktop entry: {DESKTOP_FILE}")

    def test_script_contract(self) -> None:
        text = read_text(SCRIPT)
        ok, missing = contains_all(
            text,
            [
                "SENIOR_ZERO_RUNTIME_PROFILE_DRY_RUN",
                "baseline_ram_mb=4096",
                "target_cpu_class=i3_legacy",
                "boot_time_seconds=",
                "memory_total_mb=",
                "memory_used_mb=",
                "memory_available_mb=",
                "cpu_model=",
                "SENIOR_ZERO_RUNTIME_PROFILE_OK",
                "SENIOR_ZERO_RUNTIME_PROFILE_WARN",
                "SENIOR_ZERO_RUNTIME_PROFILE_FAKE",
            ],
        )
        self.assertTrue(ok, f"Missing runtime profile contract entries: {missing}")

    def test_desktop_entry_targets_runtime_profile(self) -> None:
        text = read_text(DESKTOP_FILE)
        ok, missing = contains_all(
            text,
            [
                "Type=Application",
                "Name=Senior Zero Runtime Profile",
                "Exec=lxterminal -e senior-zero-runtime-profile",
            ],
        )
        self.assertTrue(ok, f"Runtime profile desktop entry mismatch: {missing}")


if __name__ == "__main__":
    unittest.main()
