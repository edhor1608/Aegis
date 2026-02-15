from pathlib import Path
import unittest

from tests.lib.markdown_checks import extract_section, normalize_markdown, read_text


OBSIDIAN_NOTES = Path(
    "/Users/jonas/Library/Mobile Documents/iCloud~md~obsidian/Documents/Coding/Projekte/P18 Senior Zero Linux/docs/notes.md"
)
REPO_ROOT = Path(__file__).resolve().parents[2]
SNAPSHOT = REPO_ROOT / "tests" / "snapshots" / "obsidian-sprint0-links.md.snap"


class ObsidianLinksSnapshotTests(unittest.TestCase):
    def test_sprint0_links_section_snapshot(self) -> None:
        notes_text = read_text(OBSIDIAN_NOTES)
        actual_section = normalize_markdown(extract_section(notes_text, "Sprint-0 Workspace Links"))
        expected_section = normalize_markdown(read_text(SNAPSHOT))
        self.assertEqual(actual_section, expected_section, "Obsidian sprint-0 links section mismatch")


if __name__ == "__main__":
    unittest.main()
