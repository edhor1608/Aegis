from pathlib import Path
import unittest

from tests.lib.markdown_checks import contains_all, has_heading, read_text


REPO_ROOT = Path(__file__).resolve().parents[2]
ARCH_DIR = REPO_ROOT / "docs" / "architecture"

SYSTEM_MODEL = ARCH_DIR / "system-model.md"
UPDATE_ROLLBACK = ARCH_DIR / "update-and-rollback.md"
APP_CENTER = ARCH_DIR / "app-center-policy.md"


class ArchitectureDocsContractTests(unittest.TestCase):
    def test_required_files_exist(self) -> None:
        required = [SYSTEM_MODEL, UPDATE_ROLLBACK, APP_CENTER]
        missing = [str(path) for path in required if not path.exists()]
        self.assertEqual(missing, [], f"Missing files: {missing}")

    def test_system_model_contains_locked_decisions(self) -> None:
        text = read_text(SYSTEM_MODEL)
        for heading in ["Goals", "System Layers", "Release Model", "Language Baseline"]:
            self.assertTrue(has_heading(text, heading), f"Missing heading: {heading}")

        ok, missing = contains_all(
            text,
            [
                "Debian Stable",
                "classic Debian apt model",
                "zero-config behavior as priority 1",
                "XFCE/LXQt + custom simplified launcher",
                "every 6 months",
            ],
        )
        self.assertTrue(ok, f"Missing snippets in system-model.md: {missing}")

    def test_update_and_rollback_contains_mandatory_stack(self) -> None:
        text = read_text(UPDATE_ROLLBACK)
        for heading in ["Update Channels", "Security Update Baseline", "Rollback Flow", "Failure Handling"]:
            self.assertTrue(has_heading(text, heading), f"Missing heading: {heading}")

        ok, missing = contains_all(
            text,
            [
                "unattended-upgrades",
                "apt pinning",
                "snapper",
                "grub-btrfs",
                "managed rollback",
            ],
        )
        self.assertTrue(ok, f"Missing snippets in update-and-rollback.md: {missing}")

    def test_app_center_policy_enforces_curated_and_more_apps(self) -> None:
        text = read_text(APP_CENTER)
        for heading in ["Policy Goal", "Catalog Structure", "Warning Gate", "Repository Rules"]:
            self.assertTrue(has_heading(text, heading), f"Missing heading: {heading}")

        ok, missing = contains_all(
            text,
            [
                "Curated default catalog",
                "More Apps",
                "warning",
                "Debian Stable repositories",
                "zero-config",
            ],
        )
        self.assertTrue(ok, f"Missing snippets in app-center-policy.md: {missing}")


if __name__ == "__main__":
    unittest.main()
