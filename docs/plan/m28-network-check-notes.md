# Milestone 28 Notes (Network Check Command)

## Problem

Users needed a fast single command to confirm baseline network readiness without manual command sequences.

## What Was Added

- New command:
  - `/usr/local/bin/senior-zero-network-check`
- New desktop entry:
  - `/etc/skel/Desktop/Senior Zero Network Check.desktop`

## Behavior

- `--dry-run` prints the planned checks.
- Runtime mode checks:
  - NetworkManager active state
  - default route availability
  - DNS resolution (`deb.debian.org`)
  - internet ICMP reachability (`1.1.1.1`)
- Emits overall result marker (`OK` or `ATTENTION`).
- `SENIOR_ZERO_NETWORK_CHECK_FAKE=1` provides deterministic all-pass mode for tests.

## Manual VM Test

```bash
senior-zero-network-check --dry-run
senior-zero-network-check
```
