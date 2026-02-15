# Sprint-0 Plan

## Sprint Goal

Produce a documented, test-validated foundation for Senior Zero Linux that locks architecture and execution policy without implementing runtime system code yet.

## Scope

- In scope: architecture docs, sprint planning assets, risk register, and Obsidian cross-linking.
- Out of scope: remote help implementation, full installer runtime behavior, and post-v1 features.

## Deliverables

1. `docs/architecture/system-model.md`
2. `docs/architecture/update-and-rollback.md`
3. `docs/architecture/app-center-policy.md`
4. `docs/plan/sprint-0.md`
5. `docs/plan/risk-register.md`

## Task Plan

| ID | Task | Description | Depends On | Done Criteria |
|---|---|---|---|---|
| S0-01 | Debian image build pipeline | Define `live-build` pipeline blueprint, reproducibility inputs, and artifact outputs. | None | Pipeline steps, inputs, and expected ISO artifacts are documented and reviewable. |
| S0-02 | Btrfs rollback integration | Define `snapper + grub-btrfs` lifecycle: pre-update snapshot, health checks, rollback trigger. | S0-01 | Rollback flow is documented with explicit trigger conditions and user-facing outcome. |
| S0-03 | security auto-update policy implementation | Specify `unattended-upgrades + apt pinning` policy boundary for security-only automation. | S0-01 | Policy includes allowed origins, pinning intent, and low-noise notification behavior. |
| S0-04 | low-end hardware validation matrix | Create Markdown matrix for old i3/4 GB target classes and critical peripherals. | S0-01 | Matrix includes pass criteria for wifi, audio, graphics, storage, webcam, printer, and USB hot-plug. |
| S0-05 | DE/EN localization baseline | Define EN default with DE switch and baseline QA checkpoints for core flows. | S0-01 | Locale behavior, switching rule, and validation checklist are documented. |

## Exit Criteria

- All Sprint-0 docs exist and pass unit/integration/snapshot/e2e test gates.
- Mandatory workstreams are represented as concrete tasks with dependencies and done criteria.
- Locked project decisions remain consistent across all created artifacts.
