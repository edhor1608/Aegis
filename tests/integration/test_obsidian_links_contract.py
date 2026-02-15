from pathlib import Path
import unittest

from tests.lib.markdown_checks import contains_all, read_text


OBSIDIAN_NOTES = Path(
    "/Users/jonas/Library/Mobile Documents/iCloud~md~obsidian/Documents/Coding/Projekte/P18 Senior Zero Linux/docs/notes.md"
)


class ObsidianLinksContractTests(unittest.TestCase):
    def test_notes_file_exists(self) -> None:
        self.assertTrue(OBSIDIAN_NOTES.exists(), f"Missing notes file: {OBSIDIAN_NOTES}")

    def test_notes_contains_sprint0_workspace_links(self) -> None:
        text = read_text(OBSIDIAN_NOTES)
        ok, missing = contains_all(
            text,
            [
                "## Sprint-0 Workspace Links",
                "[system-model.md](/Users/jonas/repos/senior-zero-linux/docs/architecture/system-model.md)",
                "[update-and-rollback.md](/Users/jonas/repos/senior-zero-linux/docs/architecture/update-and-rollback.md)",
                "[app-center-policy.md](/Users/jonas/repos/senior-zero-linux/docs/architecture/app-center-policy.md)",
                "[sprint-0.md](/Users/jonas/repos/senior-zero-linux/docs/plan/sprint-0.md)",
                "[risk-register.md](/Users/jonas/repos/senior-zero-linux/docs/plan/risk-register.md)",
            ],
        )
        self.assertTrue(ok, f"Missing Obsidian links: {missing}")


if __name__ == "__main__":
    unittest.main()
