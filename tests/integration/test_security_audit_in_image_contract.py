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
    / "sbin"
    / "senior-zero-security-audit"
)


class SecurityAuditInImageContractTests(unittest.TestCase):
    def test_script_exists(self) -> None:
        self.assertTrue(SCRIPT.exists(), f"Missing in-image security audit script: {SCRIPT}")

    def test_script_contains_security_policy_checks(self) -> None:
        text = read_text(SCRIPT)
        ok, missing = contains_all(
            text,
            [
                "SECURITY_AUDIT_DRY_RUN",
                "systemctl is-enabled unattended-upgrades",
                "/etc/apt/apt.conf.d/52unattended-upgrades-senior-zero",
                "/etc/apt/preferences.d/90-senior-zero-security.pref",
                "Allowed-Origins",
                "security",
                "Pin-Priority: 990",
                "Pin-Priority: 500",
                "Automatic-Reboot",
                "SECURITY_AUDIT_PASS",
            ],
        )
        self.assertTrue(ok, f"Missing security audit checks: {missing}")


if __name__ == "__main__":
    unittest.main()
