# Milestone 4 Notes (Live-Build Pipeline)

## Problem

Create the first runnable Debian image build pipeline step for Senior Zero Linux with test-first validation.

## What Was Added

- `tools/live_build_pipeline.py` command model and dry-run/execute CLI.
- `scripts/live_build_pipeline.sh` wrapper.
- `build/live-build` baseline config with:
  - `auto/config`
  - package baseline (`snapper`, `grub-btrfs`, `unattended-upgrades`)
  - unattended-upgrades policy file
  - apt pinning file

## What Worked

- Full TDD cycle passed (unit/integration/snapshot/e2e) via `make test`.
- Dry-run output now prints exact `lb` sequence and target VM artifact path.

## Blocker

- `lb` is not installed locally (`lb_present=no`), so actual ISO build cannot run yet.

## Next Execution Step

Install `live-build`, execute `scripts/live_build_pipeline.sh`, then boot `build/live-build/live-image-amd64.hybrid.iso` in VM.
