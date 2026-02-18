from pathlib import Path
import subprocess
import unittest


REPO_ROOT = Path(__file__).resolve().parents[2]


class AcceptanceRunnerInImageE2ETests(unittest.TestCase):
    def test_acceptance_runner_dry_run_gate(self) -> None:
        result = subprocess.run(
            ["bash", str(REPO_ROOT / "scripts" / "verify_acceptance_runner_in_image_e2e.sh")],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(
            result.returncode,
            0,
            f"Expected acceptance runner e2e gate to pass.\nSTDOUT:\n{result.stdout}\nSTDERR:\n{result.stderr}",
        )
        self.assertIn("E2E PASS", result.stdout)


if __name__ == "__main__":
    unittest.main()
