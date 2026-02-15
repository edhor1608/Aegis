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
LOCALE_HOOK = (
    REPO_ROOT
    / "build"
    / "live-build"
    / "config"
    / "hooks"
    / "normal"
    / "6000-configure-locales.hook.chroot"
)
VM_SMOKE_SCRIPT = REPO_ROOT / "scripts" / "vm_runtime_smoke.sh"


class LiveBuildPipelineContractTests(unittest.TestCase):
    def test_required_pipeline_files_exist(self) -> None:
        required = [
            AUTO_CONFIG,
            PACKAGE_LIST,
            UNATTENDED_CFG,
            PINNING_CFG,
            PIPELINE_SCRIPT,
            LOCALE_HOOK,
            VM_SMOKE_SCRIPT,
        ]
        missing = [str(path) for path in required if not path.exists()]
        self.assertEqual(missing, [], f"Missing files: {missing}")

    def test_package_list_contains_baseline_components(self) -> None:
        text = read_text(PACKAGE_LIST)
        ok, missing = contains_all(
            text,
            [
                "user-setup",
                "snapper",
                "btrfs-progs",
                "unattended-upgrades",
                "apt-listchanges",
                "task-lxde-desktop",
            ],
        )
        self.assertTrue(ok, f"Missing package baseline entries: {missing}")

    def test_package_list_excludes_unavailable_grub_btrfs_package(self) -> None:
        text = read_text(PACKAGE_LIST)
        self.assertNotIn("grub-btrfs", text)

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

    def test_locale_hook_generates_de_and_en_utf8(self) -> None:
        text = read_text(LOCALE_HOOK)
        ok, missing = contains_all(
            text,
            [
                "en_US.UTF-8 UTF-8",
                "de_DE.UTF-8 UTF-8",
                "locale-gen",
                "LANG=en_US.UTF-8",
            ],
        )
        self.assertTrue(ok, f"Missing locale baseline entries: {missing}")

    def test_vm_smoke_script_covers_runtime_baseline(self) -> None:
        text = read_text(VM_SMOKE_SCRIPT)
        ok, missing = contains_all(
            text,
            [
                "systemctl is-enabled unattended-upgrades",
                "systemctl is-active NetworkManager",
                "locale -a",
                "de_DE.utf8",
                "en_US.utf8",
                "whoami",
                "senior-zero-preflight-report",
                "senior-zero-app-center-policy",
                "senior-zero-acceptance-runner --dry-run",
            ],
        )
        self.assertTrue(ok, f"Missing VM smoke checks: {missing}")


if __name__ == "__main__":
    unittest.main()
