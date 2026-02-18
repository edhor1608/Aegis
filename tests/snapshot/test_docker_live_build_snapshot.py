from pathlib import Path
import unittest

from tests.lib.markdown_checks import normalize_markdown, read_text


REPO_ROOT = Path(__file__).resolve().parents[2]
SNAP_DIR = REPO_ROOT / "tests" / "snapshots"


class DockerLiveBuildSnapshotTests(unittest.TestCase):
    def _assert_snapshot(self, target_file: Path, snapshot_name: str) -> None:
        actual = normalize_markdown(read_text(target_file))
        expected = normalize_markdown(read_text(SNAP_DIR / snapshot_name))
        self.assertEqual(actual, expected, f"Snapshot mismatch for {target_file}")

    def test_dockerfile_snapshot(self) -> None:
        self._assert_snapshot(
            REPO_ROOT / "docker" / "live-build-builder.Dockerfile",
            "docker-live-build-builder.snap",
        )

    def test_docker_wrapper_snapshot(self) -> None:
        self._assert_snapshot(
            REPO_ROOT / "scripts" / "live_build_in_docker.sh",
            "docker-live-build-wrapper.snap",
        )


if __name__ == "__main__":
    unittest.main()
