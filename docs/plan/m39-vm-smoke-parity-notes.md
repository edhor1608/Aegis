# M39 - VM Smoke Parity

## Drift fixed

`vm_runtime_smoke.sh` only checked early helper commands and did not cover the newer support/checklist/doctor/launcher acceptance path.

## Goal

Keep VM runtime smoke aligned with the live helper surface to catch drift early.

## Delivered

- Extended `scripts/vm_runtime_smoke.sh` checks to include:
  - `senior-zero-support-bundle`
  - `senior-zero-daily-checklist`
  - `senior-zero-command-doctor`
  - `senior-zero-command-index --dry-run` includes new command surface
  - `senior-zero-launcher --dry-run` includes `action_acceptance`
- Updated coverage:
  - integration contract (`test_live_build_pipeline_contract.py`)
  - VM smoke script snapshot
  - VM smoke e2e verifier snapshot and gate behavior

## Verification

- `make test` passes with M39 included.

## Operator usage (inside VM)

- `bash /usr/local/bin/senior-zero-acceptance-runner --dry-run`
- host-side dry-run check: `./scripts/vm_runtime_smoke.sh --dry-run`
