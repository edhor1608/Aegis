# Update and Rollback

## Update Channels

1. Security Channel
- Automatic security updates on a scheduled unattended cycle.
2. Care Release Channel
- Planned, low-frequency release cadence every 6 months.

## Security Update Baseline

- unattended-upgrades is the execution mechanism for security updates.
- apt pinning is used to constrain package sources and prevent unintended feature drift.
- Default behavior is silent and low-noise, with user-facing messaging only on actionable failures.

## Rollback Flow

1. Pre-update snapshot is created by snapper.
2. Security update transaction runs.
3. Post-update health checks validate boot and core shell readiness.
4. grub-btrfs exposes snapshots at boot and enables managed rollback when checks fail.

## Snapshot Retention

- Keep short rolling history for recent update checkpoints.
- Preserve at least one known-good snapshot.
- Prune older snapshots on a bounded schedule to protect low-capacity disks.

## Failure Handling

- Failed update with healthy boot: mark degraded state, defer retry, show one simple notification.
- Failed update with unhealthy boot: use managed rollback path through snapshot boot entries.
- Escalation path avoids terminal instructions in standard user guidance.
