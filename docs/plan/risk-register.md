# Sprint-0 Risk Register

## Risk Table

| Risk ID | Description | Likelihood | Impact | Trigger | Mitigation | Owner | Status |
|---|---|---|---|---|---|---|---|
| R-01 | Build reproducibility drift | Medium | High | Two image builds produce non-matching package manifests or artifacts. | Lock build inputs, record package manifest checksum, and run reproducibility comparison in CI gate. | Build Lead | Open |
| R-02 | Rollback boot integration failure | Medium | High | Snapshot exists but rollback entry is missing or fails to boot. | Validate `grub-btrfs` entry generation on each update scenario and include rollback boot test in validation runbook. | Platform Lead | Open |
| R-03 | Security update regression or noisy UX | Medium | High | Security update causes app regression or repeated noisy prompts. | Restrict scope with `apt pinning`, keep unattended security origin rules strict, and apply low-noise notification policy. | Ops Lead | Open |
| R-04 | Low-end hardware compatibility gaps | High | High | Gold/Silver criteria fail on representative old i3/4 GB devices. | Execute matrix-based hardware validation early and maintain known-issues list with non-terminal workarounds. | Hardware Lead | Open |
| R-05 | DE/EN localization inconsistency | Medium | Medium | Core flow strings differ between EN and DE or fallback is broken. | Enforce localization checklist for browser/call/photo/document/help/settings flows before Sprint-0 signoff. | UX Lead | Open |
| R-06 | Storage pressure from snapshots on small disks | Medium | Medium | Disk usage spikes on 64 GB devices after repeated update cycles. | Define bounded retention policy and automatic pruning with one known-good snapshot retained. | Platform Lead | Open |
