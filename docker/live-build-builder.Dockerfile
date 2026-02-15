FROM debian:bookworm

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y --no-install-recommends \
  live-build \
  debootstrap \
  xorriso \
  squashfs-tools \
  dosfstools \
  cpio \
  python3 \
  ca-certificates \
  gnupg \
  && rm -rf /var/lib/apt/lists/*

WORKDIR /workspace
