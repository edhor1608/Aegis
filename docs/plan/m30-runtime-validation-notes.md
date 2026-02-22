# Milestone 30 Notes (Runtime Validation Recovery)

## Problem

Runtime ISO rebuild failed in `lb chroot_install-packages install` because `grub-btrfs` could not be resolved from Debian Stable repositories.

## Change

- Removed `grub-btrfs` from `build/live-build/config/package-lists/senior-zero.list.chroot`.
- Added/updated contract expectation in `tests/integration/test_live_build_pipeline_contract.py`:
  - keep required baseline: `snapper`, `btrfs-progs`, `unattended-upgrades`, `apt-listchanges`, `task-lxqt-desktop`
  - explicitly assert `grub-btrfs` is not required in Debian Stable live-build baseline

## Validation Evidence

1. Failing test before fix:
   - `python3 -m unittest tests.integration.test_live_build_pipeline_contract.LiveBuildPipelineContractTests.test_package_list_contains_baseline_components -v`
2. Full automated gates after fix:
   - `make test`
3. Full runtime rebuild:
   - `time scripts/live_build_in_docker.sh`
   - result: `Build completed successfully`
4. Artifact evidence:
   - `out/live-build/live-image-amd64.hybrid.iso`
   - timestamp: `2026-02-22 10:06:37`
   - sha256: `3027e99bb7210b7fa8f179f31458e6c9e2ecb0905a833045c12eca5536ced4f2`
5. In-image content validation (via docker `xorriso + unsquashfs`):
   - confirmed presence of:
     - `/usr/local/sbin/senior-zero-preflight-report`
     - `/usr/local/sbin/senior-zero-acceptance-runner`
     - `/usr/local/sbin/senior-zero-rollback-rehearsal`
     - `/etc/senior-zero/app-center/curated-default-packages.txt`
     - `/etc/apt/apt.conf.d/52unattended-upgrades-senior-zero`
     - `/etc/apt/preferences.d/90-senior-zero-security.pref`
