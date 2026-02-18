from pathlib import Path
import unittest

from tests.lib.markdown_checks import normalize_markdown, read_text


REPO_ROOT = Path(__file__).resolve().parents[2]
SNAP_DIR = REPO_ROOT / "tests" / "snapshots"
IN_IMAGE_SCRIPT = (
    REPO_ROOT
    / "build"
    / "live-build"
    / "config"
    / "includes.chroot"
    / "usr"
    / "local"
    / "sbin"
    / "senior-zero-install-target-smoke"
)


class InstallTargetInImageSnapshotTests(unittest.TestCase):
    def test_in_image_install_target_smoke_script_snapshot(self) -> None:
        actual = normalize_markdown(read_text(IN_IMAGE_SCRIPT))
        expected = normalize_markdown(read_text(SNAP_DIR / "install-target-in-image-script.snap"))
        self.assertEqual(actual, expected, "Snapshot mismatch for in-image install-target smoke script")


if __name__ == "__main__":
    unittest.main()
