from pathlib import Path
import unittest

from tests.lib.markdown_checks import normalize_markdown, read_text


REPO_ROOT = Path(__file__).resolve().parents[2]
SNAP_DIR = REPO_ROOT / "tests" / "snapshots"


class VmRuntimeSmokeSnapshotTests(unittest.TestCase):
    def _assert_snapshot(self, target_file: Path, snapshot_name: str) -> None:
        actual = normalize_markdown(read_text(target_file))
        expected = normalize_markdown(read_text(SNAP_DIR / snapshot_name))
        self.assertEqual(actual, expected, f"Snapshot mismatch for {target_file}")

    def test_vm_runtime_smoke_script_snapshot(self) -> None:
        self._assert_snapshot(
            REPO_ROOT / "scripts" / "vm_runtime_smoke.sh",
            "vm-runtime-smoke-script.snap",
        )

    def test_vm_runtime_smoke_e2e_verifier_snapshot(self) -> None:
        self._assert_snapshot(
            REPO_ROOT / "scripts" / "verify_vm_runtime_smoke_e2e.sh",
            "vm-runtime-smoke-e2e-verifier.snap",
        )


if __name__ == "__main__":
    unittest.main()
