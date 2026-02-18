from pathlib import Path
import tempfile
import unittest

from tests.lib.markdown_checks import contains_all, extract_section, has_heading, normalize_markdown, read_text


class MarkdownCheckUnitTests(unittest.TestCase):
    def test_has_heading_detects_existing_heading(self) -> None:
        text = "## Section A\nBody\n"
        self.assertTrue(has_heading(text, "Section A"))
        self.assertFalse(has_heading(text, "Section B"))

    def test_contains_all_lists_missing_items(self) -> None:
        ok, missing = contains_all("hello world", ["hello", "linux", "world"])
        self.assertFalse(ok)
        self.assertEqual(missing, ["linux"])

    def test_normalize_markdown_strips_trailing_spaces_and_ends_with_newline(self) -> None:
        text = "A  \nB\t \n\n"
        normalized = normalize_markdown(text)
        self.assertEqual(normalized, "A\nB\n")

    def test_read_text_roundtrip(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "sample.md"
            path.write_text("sample", encoding="utf-8")
            self.assertEqual(read_text(path), "sample")

    def test_extract_section_returns_target_block(self) -> None:
        text = "# T\n\n## A\nx\n\n## B\ny\n"
        self.assertEqual(extract_section(text, "A"), "## A\nx\n")
        self.assertEqual(extract_section(text, "B"), "## B\ny\n")
        self.assertEqual(extract_section(text, "Z"), "")


if __name__ == "__main__":
    unittest.main()
