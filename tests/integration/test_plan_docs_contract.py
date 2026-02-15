from pathlib import Path
import unittest

from tests.lib.markdown_checks import contains_all, has_heading, read_text


REPO_ROOT = Path(__file__).resolve().parents[2]
PLAN_DIR = REPO_ROOT / "docs" / "plan"

SPRINT_PLAN = PLAN_DIR / "sprint-0.md"
RISK_REGISTER = PLAN_DIR / "risk-register.md"


class PlanDocsContractTests(unittest.TestCase):
    def test_required_plan_files_exist(self) -> None:
        required = [SPRINT_PLAN, RISK_REGISTER]
        missing = [str(path) for path in required if not path.exists()]
        self.assertEqual(missing, [], f"Missing files: {missing}")

    def test_sprint_0_contains_mandatory_workstreams(self) -> None:
        text = read_text(SPRINT_PLAN)
        for heading in ["Sprint Goal", "Deliverables", "Task Plan", "Exit Criteria"]:
            self.assertTrue(has_heading(text, heading), f"Missing heading: {heading}")

        ok, missing = contains_all(
            text,
            [
                "Debian image build pipeline",
                "Btrfs rollback integration",
                "security auto-update policy implementation",
                "low-end hardware validation matrix",
                "DE/EN localization baseline",
            ],
        )
        self.assertTrue(ok, f"Missing snippets in sprint-0.md: {missing}")

    def test_risk_register_has_required_columns_and_seed_risks(self) -> None:
        text = read_text(RISK_REGISTER)
        required_headers = [
            "Risk ID",
            "Description",
            "Likelihood",
            "Impact",
            "Trigger",
            "Mitigation",
            "Owner",
            "Status",
        ]
        ok, missing = contains_all(text, required_headers)
        self.assertTrue(ok, f"Missing risk register headers: {missing}")

        ok, missing = contains_all(
            text,
            [
                "Build reproducibility drift",
                "Rollback boot integration failure",
                "Security update regression or noisy UX",
                "Low-end hardware compatibility gaps",
                "DE/EN localization inconsistency",
            ],
        )
        self.assertTrue(ok, f"Missing seed risks in risk-register.md: {missing}")


if __name__ == "__main__":
    unittest.main()
