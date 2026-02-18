from pathlib import Path
import unittest

from tests.lib.markdown_checks import normalize_markdown, read_text


REPO_ROOT = Path(__file__).resolve().parents[2]
SNAP_DIR = REPO_ROOT / "tests" / "snapshots"
PLAN_DIR = REPO_ROOT / "docs" / "plan"


class PlanDocsSnapshotTests(unittest.TestCase):
    def _assert_snapshot(self, doc_name: str, snapshot_name: str) -> None:
        actual = normalize_markdown(read_text(PLAN_DIR / doc_name))
        expected = normalize_markdown(read_text(SNAP_DIR / snapshot_name))
        self.assertEqual(actual, expected, f"Snapshot mismatch for {doc_name}")

    def test_sprint_0_snapshot(self) -> None:
        self._assert_snapshot("sprint-0.md", "sprint-0.md.snap")

    def test_risk_register_snapshot(self) -> None:
        self._assert_snapshot("risk-register.md", "risk-register.md.snap")


if __name__ == "__main__":
    unittest.main()
