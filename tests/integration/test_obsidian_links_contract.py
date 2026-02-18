import os
from pathlib import Path
import unittest

from tests.lib.markdown_checks import contains_all, read_text


DEFAULT_NOTES_PATH = (
    "/Users/jonas/Library/Mobile Documents/iCloud~md~obsidian/Documents/Coding/Projekte/P18 Senior Zero Linux/docs/notes.md"
)
DEFAULT_WORKSPACE_ROOT = "/Users/jonas/repos/senior-zero-linux"
OBSIDIAN_NOTES = Path(os.environ.get("OBSIDIAN_NOTES_PATH", DEFAULT_NOTES_PATH))
WORKSPACE_ROOT = Path(os.environ.get("SENIOR_ZERO_WORKSPACE_ROOT", DEFAULT_WORKSPACE_ROOT))


class ObsidianLinksContractTests(unittest.TestCase):
    @unittest.skipUnless(OBSIDIAN_NOTES.exists(), f"Missing notes file: {OBSIDIAN_NOTES}")
    def test_notes_file_exists(self) -> None:
        self.assertTrue(OBSIDIAN_NOTES.exists(), f"Missing notes file: {OBSIDIAN_NOTES}")

    @unittest.skipUnless(OBSIDIAN_NOTES.exists(), f"Missing notes file: {OBSIDIAN_NOTES}")
    def test_notes_contains_sprint0_workspace_links(self) -> None:
        text = read_text(OBSIDIAN_NOTES)
        ok, missing = contains_all(
            text,
            [
                "## Sprint-0 Workspace Links",
                f"[system-model.md]({WORKSPACE_ROOT / 'docs/architecture/system-model.md'})",
                f"[update-and-rollback.md]({WORKSPACE_ROOT / 'docs/architecture/update-and-rollback.md'})",
                f"[app-center-policy.md]({WORKSPACE_ROOT / 'docs/architecture/app-center-policy.md'})",
                f"[sprint-0.md]({WORKSPACE_ROOT / 'docs/plan/sprint-0.md'})",
                f"[risk-register.md]({WORKSPACE_ROOT / 'docs/plan/risk-register.md'})",
            ],
        )
        self.assertTrue(ok, f"Missing Obsidian links: {missing}")


if __name__ == "__main__":
    unittest.main()
