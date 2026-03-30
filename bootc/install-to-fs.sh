#!/bin/bash

set -xu

IMAGE=$1
BOOTLOADER=$2

sudo podman run --rm --net=host --privileged --pid=host \
    --security-opt label=type:unconfined_t \
    --env RUST_LOG=debug \
    -v /dev:/dev \
    -v /var/lib/containers:/var/lib/containers \
    -v /home/pragyan/RedHat/bootc/target/release/bootc:/usr/bin/bootc:ro,Z \
    -v /mnt:/var/mnt \
    -v .:/output \
    "$IMAGE" \
        bootc install to-filesystem \
            --bootloader "$BOOTLOADER" \
            --composefs-backend \
            --karg enforcing=0 --karg console=ttyS0,115000n --karg audit=0 \
            /var/mnt --source-imgref "oci-archive:/output/bootc-bls-gc.tar"
