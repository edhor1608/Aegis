from pathlib import Path
import unittest

from tests.lib.markdown_checks import normalize_markdown, read_text


REPO_ROOT = Path(__file__).resolve().parents[2]
BIN_DIR = REPO_ROOT / "build" / "live-build" / "config" / "includes.chroot" / "usr" / "local" / "bin"
SNAP_DIR = REPO_ROOT / "tests" / "snapshots"


class UserPathShimsInImageSnapshotTests(unittest.TestCase):
    def test_preflight_wrapper_snapshot(self) -> None:
        actual = normalize_markdown(read_text(BIN_DIR / "senior-zero-preflight-report"))
        expected = normalize_markdown(read_text(SNAP_DIR / "user-path-shim-preflight.snap"))
        self.assertEqual(actual, expected, "Snapshot mismatch for preflight wrapper in /usr/local/bin")


if __name__ == "__main__":
    unittest.main()
