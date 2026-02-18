from pathlib import Path
import unittest

from tests.lib.markdown_checks import contains_all, read_text


REPO_ROOT = Path(__file__).resolve().parents[2]
IN_IMAGE_SCRIPT = (
    REPO_ROOT
    / "build"
    / "live-build"
    / "config"
    / "includes.chroot"
    / "usr"
    / "local"
    / "sbin"
    / "senior-zero-install-target-smoke"
)


class InstallTargetInImageContractTests(unittest.TestCase):
    def test_script_exists_in_image_includes(self) -> None:
        self.assertTrue(IN_IMAGE_SCRIPT.exists(), f"Missing in-image smoke script: {IN_IMAGE_SCRIPT}")

    def test_script_covers_required_install_target_checks(self) -> None:
        text = read_text(IN_IMAGE_SCRIPT)
        ok, missing = contains_all(
            text,
            [
                "INSTALL_TARGET_SMOKE_DRY_RUN",
                "findmnt -n -o FSTYPE /",
                "/etc/apt/apt.conf.d/52unattended-upgrades-senior-zero",
                "/etc/apt/preferences.d/90-senior-zero-security.pref",
                "snapper-timeline.timer",
                "snapper-cleanup.timer",
                "/var/lib/senior-zero/rollback-bootstrap.done",
                "de_DE.utf8",
                "en_US.utf8",
                "INSTALL_TARGET_SMOKE_PASS",
            ],
        )
        self.assertTrue(ok, f"Missing install-target checks: {missing}")


if __name__ == "__main__":
    unittest.main()
