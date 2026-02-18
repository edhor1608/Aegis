from pathlib import Path
import subprocess
import unittest


REPO_ROOT = Path(__file__).resolve().parents[2]


class RollbackReadinessE2ETests(unittest.TestCase):
    def test_rollback_readiness_dry_run_gate(self) -> None:
        result = subprocess.run(
            ["bash", str(REPO_ROOT / "scripts" / "verify_rollback_readiness_e2e.sh")],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(
            result.returncode,
            0,
            f"Expected rollback readiness e2e gate to pass.\nSTDOUT:\n{result.stdout}\nSTDERR:\n{result.stderr}",
        )
        self.assertIn("E2E PASS", result.stdout)


if __name__ == "__main__":
    unittest.main()
