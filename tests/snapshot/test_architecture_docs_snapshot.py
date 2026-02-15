from pathlib import Path
import unittest

from tests.lib.markdown_checks import normalize_markdown, read_text


REPO_ROOT = Path(__file__).resolve().parents[2]
SNAP_DIR = REPO_ROOT / "tests" / "snapshots"
ARCH_DIR = REPO_ROOT / "docs" / "architecture"


class ArchitectureDocsSnapshotTests(unittest.TestCase):
    def _assert_snapshot(self, doc_name: str, snapshot_name: str) -> None:
        actual = normalize_markdown(read_text(ARCH_DIR / doc_name))
        expected = normalize_markdown(read_text(SNAP_DIR / snapshot_name))
        self.assertEqual(actual, expected, f"Snapshot mismatch for {doc_name}")

    def test_system_model_snapshot(self) -> None:
        self._assert_snapshot("system-model.md", "system-model.md.snap")

    def test_update_and_rollback_snapshot(self) -> None:
        self._assert_snapshot("update-and-rollback.md", "update-and-rollback.md.snap")

    def test_app_center_policy_snapshot(self) -> None:
        self._assert_snapshot("app-center-policy.md", "app-center-policy.md.snap")


if __name__ == "__main__":
    unittest.main()
