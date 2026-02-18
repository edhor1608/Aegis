from pathlib import Path
import unittest

from tests.lib.markdown_checks import normalize_markdown, read_text


REPO_ROOT = Path(__file__).resolve().parents[2]
SNAP_DIR = REPO_ROOT / "tests" / "snapshots"


class LiveBuildPipelineSnapshotTests(unittest.TestCase):
    def _assert_snapshot(self, target_file: Path, snapshot_name: str) -> None:
        actual = normalize_markdown(read_text(target_file))
        expected = normalize_markdown(read_text(SNAP_DIR / snapshot_name))
        self.assertEqual(actual, expected, f"Snapshot mismatch for {target_file}")

    def test_auto_config_snapshot(self) -> None:
        self._assert_snapshot(
            REPO_ROOT / "build" / "live-build" / "auto" / "config",
            "live-build-auto-config.snap",
        )

    def test_pipeline_script_snapshot(self) -> None:
        self._assert_snapshot(
            REPO_ROOT / "scripts" / "live_build_pipeline.sh",
            "live-build-pipeline-script.snap",
        )


if __name__ == "__main__":
    unittest.main()
