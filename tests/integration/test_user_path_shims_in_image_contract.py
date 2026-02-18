from pathlib import Path
import unittest

from tests.lib.markdown_checks import contains_all, read_text


REPO_ROOT = Path(__file__).resolve().parents[2]
BIN_DIR = REPO_ROOT / "build" / "live-build" / "config" / "includes.chroot" / "usr" / "local" / "bin"

COMMANDS = [
    "senior-zero-acceptance-runner",
    "senior-zero-app-center-policy",
    "senior-zero-install-target-smoke",
    "senior-zero-preflight-report",
    "senior-zero-rollback-bootstrap",
    "senior-zero-rollback-rehearsal",
    "senior-zero-security-audit",
]


class UserPathShimsInImageContractTests(unittest.TestCase):
    def test_all_wrapper_files_exist(self) -> None:
        missing = [str(BIN_DIR / cmd) for cmd in COMMANDS if not (BIN_DIR / cmd).exists()]
        self.assertEqual(missing, [], f"Missing /usr/local/bin wrappers: {missing}")

    def test_wrappers_delegate_to_sbin(self) -> None:
        failures = []
        for cmd in COMMANDS:
            text = read_text(BIN_DIR / cmd)
            ok, missing = contains_all(
                text,
                [
                    "#!/usr/bin/env bash",
                    "TARGET=\"/usr/local/sbin/",
                    f"/usr/local/sbin/{cmd}",
                    "exec \"$TARGET\" \"$@\"",
                ],
            )
            if not ok:
                failures.append((cmd, missing))

        self.assertEqual(failures, [], f"Wrapper delegation mismatch: {failures}")


if __name__ == "__main__":
    unittest.main()
