from pathlib import Path
import unittest

from tests.lib.markdown_checks import contains_all, read_text


REPO_ROOT = Path(__file__).resolve().parents[2]
ROLLBACK_SCRIPT = REPO_ROOT / "scripts" / "rollback_readiness.sh"
ROLLBACK_E2E_VERIFY = REPO_ROOT / "scripts" / "verify_rollback_readiness_e2e.sh"


class RollbackReadinessContractTests(unittest.TestCase):
    def test_required_scripts_exist(self) -> None:
        required = [ROLLBACK_SCRIPT, ROLLBACK_E2E_VERIFY]
        missing = [str(path) for path in required if not path.exists()]
        self.assertEqual(missing, [], f"Missing files: {missing}")

    def test_readiness_script_checks_btrfs_snapper_and_timers(self) -> None:
        text = read_text(ROLLBACK_SCRIPT)
        ok, missing = contains_all(
            text,
            [
                "findmnt -n -o FSTYPE /",
                "snapper list-configs",
                "snapper-timeline.timer",
                "snapper-cleanup.timer",
                "NOT_APPLICABLE",
                "ROLLBACK_READINESS_PASS",
                "ROLLBACK_READINESS_DRY_RUN",
            ],
        )
        self.assertTrue(ok, f"Missing rollback readiness checks: {missing}")

    def test_e2e_verifier_asserts_dry_run_contract(self) -> None:
        text = read_text(ROLLBACK_E2E_VERIFY)
        ok, missing = contains_all(
            text,
            [
                "ROLLBACK_READINESS_DRY_RUN",
                "findmnt -n -o FSTYPE /",
                "snapper list-configs",
                "snapper-timeline.timer",
                "snapper-cleanup.timer",
                "E2E PASS",
            ],
        )
        self.assertTrue(ok, f"Missing rollback readiness e2e checks: {missing}")


if __name__ == "__main__":
    unittest.main()
