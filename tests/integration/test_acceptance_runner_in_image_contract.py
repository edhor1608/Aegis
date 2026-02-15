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
    / "senior-zero-acceptance-runner"
)


class AcceptanceRunnerInImageContractTests(unittest.TestCase):
    def test_script_exists(self) -> None:
        self.assertTrue(SCRIPT.exists(), f"Missing in-image acceptance runner script: {SCRIPT}")

    def test_script_chains_core_acceptance_commands(self) -> None:
        text = read_text(SCRIPT)
        ok, missing = contains_all(
            text,
            [
                "ACCEPTANCE_RUNNER_DRY_RUN",
                "/usr/local/sbin/senior-zero-install-target-smoke",
                "/usr/local/sbin/senior-zero-security-audit",
                "/usr/local/sbin/senior-zero-rollback-rehearsal",
                "/usr/local/sbin/senior-zero-preflight-report",
                "/usr/local/sbin/senior-zero-app-center-policy",
                "ACCEPTANCE_RUNNER_PASS",
            ],
        )
        self.assertTrue(ok, f"Missing acceptance runner entries: {missing}")


if __name__ == "__main__":
    unittest.main()
