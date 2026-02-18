from pathlib import Path
import unittest

from tests.lib.markdown_checks import normalize_markdown, read_text


REPO_ROOT = Path(__file__).resolve().parents[2]
SCRIPT = (
    REPO_ROOT
    / "build"
    / "live-build"
    / "config"
    / "includes.chroot"
    / "usr"
    / "local"
    / "bin"
    / "senior-zero-language-switch"
)
SNAP = REPO_ROOT / "tests" / "snapshots" / "language-switch-helper.snap"


class LanguageSwitchHelperInImageSnapshotTests(unittest.TestCase):
    def test_script_snapshot(self) -> None:
        actual = normalize_markdown(read_text(SCRIPT))
        expected = normalize_markdown(read_text(SNAP))
        self.assertEqual(actual, expected, "Snapshot mismatch for language switch helper script")


if __name__ == "__main__":
    unittest.main()
