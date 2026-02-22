# M40 Shell Branding Notes

## Context
- The runtime baseline was functionally solid but still looked and identified itself as stock Debian in too many visible places.
- We needed a high-impact, testable milestone that changes what users immediately see and interact with.

## Decision
- Add an Aegis-branded session layer on top of Debian LXQt:
  - GUI-first launcher entry (`Aegis Home`) backed by `senior-zero-launcher --gui`.
  - Session autostart branding script to apply Aegis wallpaper.
  - Branded `/etc/issue` banner.
  - Branded os identity in image (`PRETTY_NAME`, `NAME`, `ID`) via live-build hook.
- Keep Debian base, package model, and existing operational scripts unchanged.

## Rationale
- Maximizes visible differentiation without destabilizing base runtime behavior.
- Preserves zero-config priorities: branding is automatic via autostart and image hooks.
- Uses existing live-build include/hook patterns already validated in this repo.

## Consequences
- Positive:
  - Users now see Aegis identity on login/session surfaces.
  - Launcher experience is action-oriented instead of raw terminal-centric.
- Risk:
  - `os-release` mutation can break build when `/etc/os-release` links to `/usr/lib/os-release`.
  - Mitigation: hook avoids copying and edits existing target safely; test added to prevent regression.

## TDD Coverage Added
- `tests/integration/test_branding_shell_in_image_contract.py`
- `tests/snapshot/test_branding_shell_in_image_snapshot.py`
- `tests/e2e/test_branding_shell_in_image_e2e.py`
- Extended launcher contract/e2e/snapshots for GUI mode and `Aegis Home` desktop entry.

## Validation Performed
- `make test` passed.
- Full ISO rebuild passed via `scripts/live_build_in_docker.sh`.
- Built artifact inspected:
  - contains branding files in squashfs (`senior-zero-branding-apply`, autostart desktop, wallpaper, branded `issue`, branded `os-release`).
