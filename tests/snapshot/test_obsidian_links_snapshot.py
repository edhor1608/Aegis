import os
from pathlib import Path
import unittest

from tests.lib.markdown_checks import extract_section, normalize_markdown, read_text


DEFAULT_NOTES_PATH = (
    "/Users/jonas/Library/Mobile Documents/iCloud~md~obsidian/Documents/Coding/Projekte/P18 Senior Zero Linux/docs/notes.md"
)
DEFAULT_WORKSPACE_ROOT = "/Users/jonas/repos/senior-zero-linux"
OBSIDIAN_NOTES = Path(os.environ.get("OBSIDIAN_NOTES_PATH", DEFAULT_NOTES_PATH))
WORKSPACE_ROOT = Path(os.environ.get("SENIOR_ZERO_WORKSPACE_ROOT", DEFAULT_WORKSPACE_ROOT))
REPO_ROOT = Path(__file__).resolve().parents[2]
SNAPSHOT = REPO_ROOT / "tests" / "snapshots" / "obsidian-sprint0-links.md.snap"


class ObsidianLinksSnapshotTests(unittest.TestCase):
    @staticmethod
    def _normalize_workspace_paths(text: str) -> str:
        normalized = text.replace(str(DEFAULT_WORKSPACE_ROOT), "__WORKSPACE_ROOT__")
        normalized = normalized.replace(str(WORKSPACE_ROOT), "__WORKSPACE_ROOT__")
        return normalized

    def test_sprint0_links_section_snapshot(self) -> None:
        if not OBSIDIAN_NOTES.exists():
            self.skipTest(f"Missing notes file: {OBSIDIAN_NOTES}")
        notes_text = read_text(OBSIDIAN_NOTES)
        actual_section = normalize_markdown(extract_section(notes_text, "Sprint-0 Workspace Links"))
        actual_section = self._normalize_workspace_paths(actual_section)
        expected_section = normalize_markdown(read_text(SNAPSHOT))
        expected_section = self._normalize_workspace_paths(expected_section)
        self.assertEqual(actual_section, expected_section, "Obsidian sprint-0 links section mismatch")


if __name__ == "__main__":
    unittest.main()
