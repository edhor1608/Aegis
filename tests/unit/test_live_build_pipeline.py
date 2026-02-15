import unittest

from tools.live_build_pipeline import build_commands, default_build_config


class LiveBuildPipelineUnitTests(unittest.TestCase):
    def test_default_config_targets_debian_stable_and_amd64(self) -> None:
        cfg = default_build_config()
        self.assertEqual(cfg["distribution"], "stable")
        self.assertEqual(cfg["arch"], "amd64")
        self.assertEqual(cfg["debian_installer"], "live")

    def test_build_commands_include_clean_config_build_sequence(self) -> None:
        cfg = default_build_config()
        commands = build_commands(cfg)
        self.assertEqual(commands[0], ["lb", "clean", "--purge"])
        self.assertEqual(commands[-1], ["lb", "build"])

        config_cmd = commands[1]
        joined = " ".join(config_cmd)
        self.assertIn("--distribution stable", joined)
        self.assertIn("--architectures amd64", joined)
        self.assertIn("--debian-installer live", joined)
        self.assertIn("--archive-areas main contrib non-free-firmware", joined)


if __name__ == "__main__":
    unittest.main()
