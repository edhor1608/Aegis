from pathlib import Path
import unittest

from tests.lib.markdown_checks import normalize_markdown, read_text


REPO_ROOT = Path(__file__).resolve().parents[2]
SNAP_DIR = REPO_ROOT / "tests" / "snapshots"
INCLUDES = REPO_ROOT / "build" / "live-build" / "config" / "includes.chroot"
SCRIPT = INCLUDES / "usr" / "local" / "sbin" / "senior-zero-app-center-policy"
CURATED = INCLUDES / "etc" / "senior-zero" / "app-center" / "curated-default-packages.txt"
WARNING = INCLUDES / "etc" / "senior-zero" / "app-center" / "more-apps-warning.txt"


class AppCenterPolicyInImageSnapshotTests(unittest.TestCase):
    def test_policy_script_snapshot(self) -> None:
        actual = normalize_markdown(read_text(SCRIPT))
        expected = normalize_markdown(read_text(SNAP_DIR / "app-center-policy-in-image-script.snap"))
        self.assertEqual(actual, expected, "Snapshot mismatch for in-image app-center policy script")

    def test_curated_default_list_snapshot(self) -> None:
        actual = normalize_markdown(read_text(CURATED))
        expected = normalize_markdown(read_text(SNAP_DIR / "app-center-curated-default-packages.snap"))
        self.assertEqual(actual, expected, "Snapshot mismatch for curated app-center list")

    def test_more_apps_warning_snapshot(self) -> None:
        actual = normalize_markdown(read_text(WARNING))
        expected = normalize_markdown(read_text(SNAP_DIR / "app-center-more-apps-warning.snap"))
        self.assertEqual(actual, expected, "Snapshot mismatch for more-apps warning text")


if __name__ == "__main__":
    unittest.main()
