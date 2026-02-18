# Milestone 5 Notes (Containerized ISO Build)

## Problem

macOS host does not provide native `live-build`, and direct bind-mounted Docker execution failed due architecture and filesystem constraints.

## What Was Added

- Docker builder image: `docker/live-build-builder.Dockerfile`.
- Docker wrapper: `scripts/live_build_in_docker.sh`.
- Command model: `tools/docker_live_build.py`.
- Full TDD gates for docker path (unit/integration/snapshot/e2e).

## Runtime Fixes Applied

1. Added `python3` to builder image (required by `scripts/live_build_pipeline.sh`).
2. Forced `linux/amd64` Docker build/run on Apple Silicon hosts.
3. Switched from direct bind-mounted build execution to container-local workspace copy:
- mount source as read-only `/src`
- copy to `/tmp/repo` inside container
- export ISO artifact to host-mounted `/out`

## Current Output Contract

- Expected exported ISO path: `out/live-build/live-image-amd64.hybrid.iso`.

## Remaining Practical Constraint

- First full ISO build is long-running; final artifact generation depends on host resources and emulated `amd64` build time.
- `grub-btrfs` is not available as a Debian Stable package in this environment, so the first bootable ISO baseline excludes it and keeps `snapper + btrfs-progs` until Milestone 6 integration method is finalized.
