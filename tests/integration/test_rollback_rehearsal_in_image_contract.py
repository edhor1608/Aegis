from pathlib import Path
import unittest

from tests.lib.markdown_checks import contains_all, read_text


REPO_ROOT = Path(__file__).resolve().parents[2]
SCRIPT = (
    REPO_ROOT
    / "build"
    / "live-build"
    / "config"
    / "includes.chroot"
    / "usr"
    / "local"
    / "sbin"
    / "senior-zero-rollback-rehearsal"
)


class RollbackRehearsalInImageContractTests(unittest.TestCase):
    def test_script_exists(self) -> None:
        self.assertTrue(SCRIPT.exists(), f"Missing in-image rollback rehearsal script: {SCRIPT}")

    def test_script_contains_snapshot_rehearsal_flow(self) -> None:
        text = read_text(SCRIPT)
        ok, missing = contains_all(
            text,
            [
                "ROLLBACK_REHEARSAL_DRY_RUN",
                "findmnt -n -o FSTYPE /",
                "snapper list-configs",
                "snapper -c root create",
                "snapper -c root list",
                "snapper -c root delete",
                "ROLLBACK_REHEARSAL_PASS",
            ],
        )
        self.assertTrue(ok, f"Missing rollback rehearsal entries: {missing}")


if __name__ == "__main__":
    unittest.main()
