from pathlib import Path
import unittest

from tests.lib.markdown_checks import contains_all, read_text


REPO_ROOT = Path(__file__).resolve().parents[2]

AUTO_CONFIG = REPO_ROOT / "build" / "live-build" / "auto" / "config"
PACKAGE_LIST = REPO_ROOT / "build" / "live-build" / "config" / "package-lists" / "senior-zero.list.chroot"
UNATTENDED_CFG = (
    REPO_ROOT
    / "build"
    / "live-build"
    / "config"
    / "includes.chroot"
    / "etc"
    / "apt"
    / "apt.conf.d"
    / "52unattended-upgrades-senior-zero"
)
PINNING_CFG = (
    REPO_ROOT
    / "build"
    / "live-build"
    / "config"
    / "includes.chroot"
    / "etc"
    / "apt"
    / "preferences.d"
    / "90-senior-zero-security.pref"
)
PIPELINE_SCRIPT = REPO_ROOT / "scripts" / "live_build_pipeline.sh"


class LiveBuildPipelineContractTests(unittest.TestCase):
    def test_required_pipeline_files_exist(self) -> None:
        required = [AUTO_CONFIG, PACKAGE_LIST, UNATTENDED_CFG, PINNING_CFG, PIPELINE_SCRIPT]
        missing = [str(path) for path in required if not path.exists()]
        self.assertEqual(missing, [], f"Missing files: {missing}")

    def test_package_list_contains_baseline_components(self) -> None:
        text = read_text(PACKAGE_LIST)
        ok, missing = contains_all(
            text,
            [
                "snapper",
                "grub-btrfs",
                "unattended-upgrades",
                "apt-listchanges",
                "task-lxde-desktop",
            ],
        )
        self.assertTrue(ok, f"Missing package baseline entries: {missing}")

    def test_unattended_policy_is_security_focused(self) -> None:
        text = read_text(UNATTENDED_CFG)
        ok, missing = contains_all(
            text,
            [
                "Unattended-Upgrade::Allowed-Origins",
                "${distro_id}:${distro_codename}-security",
                "Unattended-Upgrade::Automatic-Reboot \"false\"",
            ],
        )
        self.assertTrue(ok, f"Missing unattended-upgrades policy entries: {missing}")

    def test_apt_pinning_limits_non_security_drift(self) -> None:
        text = read_text(PINNING_CFG)
        ok, missing = contains_all(
            text,
            [
                "Pin: release a=stable-security",
                "Pin-Priority: 990",
                "Pin: release a=stable",
                "Pin-Priority: 500",
            ],
        )
        self.assertTrue(ok, f"Missing apt pinning entries: {missing}")


if __name__ == "__main__":
    unittest.main()
