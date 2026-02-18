# System Model

## Goals

- zero-config behavior as priority 1 for all default user paths.
- Debian Stable base with predictable long-term maintenance.
- Stable and low-noise operation on old i3-class hardware with 4 GB RAM.

## System Layers

1. Base OS Layer
- Debian Stable base system with broad firmware defaults suitable for old laptops.
2. Package and Policy Layer
- classic Debian apt model with policy controls to reduce drift.
- Normal users install apps through App Center defaults, not raw package tooling.
3. UX Shell Layer
- XFCE/LXQt + custom simplified launcher as the default interaction surface.
4. Recovery Layer
- Btrfs snapshots + managed rollback for update safety.

## User Path Policy

- No terminal dependency for normal use.
- Curated App Center catalog shown by default.
- "More Apps" path remains available behind an explicit warning.
- Advanced package operations are out of normal user flow.

## Release Model

- Security updates are automatic and silent by default.
- Care release cadence is every 6 months for non-security feature changes.
- Remote-help is post-v1 and excluded from the baseline Sprint-0 scope.

## Language Baseline

- EN default locale.
- DE locale available and validated in core flows.

## Hardware Baseline

- Target baseline: old Intel i3-class CPU, 4 GB RAM, 64+ GB storage.
- USB peripherals should work out of the box for common keyboard, mouse, storage, webcam, and headset devices.
