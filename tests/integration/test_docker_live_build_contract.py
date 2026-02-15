from pathlib import Path
import unittest

from tests.lib.markdown_checks import contains_all, read_text


REPO_ROOT = Path(__file__).resolve().parents[2]
DOCKERFILE = REPO_ROOT / "docker" / "live-build-builder.Dockerfile"
DOCKER_SCRIPT = REPO_ROOT / "scripts" / "live_build_in_docker.sh"
TOOL_FILE = REPO_ROOT / "tools" / "docker_live_build.py"


class DockerLiveBuildContractTests(unittest.TestCase):
    def test_required_files_exist(self) -> None:
        required = [DOCKERFILE, DOCKER_SCRIPT, TOOL_FILE]
        missing = [str(path) for path in required if not path.exists()]
        self.assertEqual(missing, [], f"Missing files: {missing}")

    def test_dockerfile_contains_required_builder_packages(self) -> None:
        text = read_text(DOCKERFILE)
        ok, missing = contains_all(
            text,
            [
                "FROM debian:bookworm",
                "live-build",
                "debootstrap",
                "xorriso",
                "squashfs-tools",
                "dosfstools",
                "python3",
            ],
        )
        self.assertTrue(ok, f"Missing Dockerfile entries: {missing}")

    def test_wrapper_script_uses_docker_build_and_run(self) -> None:
        text = read_text(DOCKER_SCRIPT)
        ok, missing = contains_all(
            text,
            [
                "docker build",
                "docker run",
                "live_build_pipeline.sh",
                "--privileged",
                "--platform linux/amd64",
                "/src:ro",
                "/out",
                "cp -a /src",
                "--dry-run",
            ],
        )
        self.assertTrue(ok, f"Missing wrapper script entries: {missing}")


if __name__ == "__main__":
    unittest.main()
