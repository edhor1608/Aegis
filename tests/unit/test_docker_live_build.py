import unittest

from tools.docker_live_build import build_docker_commands, default_docker_config


class DockerLiveBuildUnitTests(unittest.TestCase):
    def test_default_docker_config(self) -> None:
        cfg = default_docker_config()
        self.assertEqual(cfg["image_tag"], "senior-zero-live-build:bookworm")
        self.assertEqual(cfg["dockerfile"], "docker/live-build-builder.Dockerfile")
        self.assertEqual(cfg["workspace_mount"], "/tmp/repo")

    def test_build_docker_commands(self) -> None:
        cfg = default_docker_config()
        commands = build_docker_commands(cfg)
        self.assertEqual(commands[0][0:2], ["docker", "build"])
        self.assertEqual(commands[1][0:2], ["docker", "run"])
        self.assertIn("--platform", commands[0])
        self.assertIn("linux/amd64", commands[0])
        self.assertIn("--platform", commands[1])
        self.assertIn("linux/amd64", commands[1])
        joined = " ".join(commands[1])
        self.assertIn("/src:ro", joined)
        self.assertIn("/out", joined)
        self.assertIn("cp -a /src", joined)


if __name__ == "__main__":
    unittest.main()
