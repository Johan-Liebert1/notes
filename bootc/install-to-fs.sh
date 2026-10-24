#!/bin/bash

set -xu

IMAGE=$1
BOOTLOADER=$2

BOOTC_BIN=$(find /home/*/RedHat/bootc/target/release -type f -executable -name bootc)

sudo podman run --rm --net=host --privileged --pid=host \
    --security-opt label=type:unconfined_t \
    --env RUST_LOG=debug \
    --env BOOTC_BOOTLOADER_DEBUG=1 \
    -v /dev:/dev \
    -v /var/lib/containers:/var/lib/containers \
    -v "$BOOTC_BIN:/usr/bin/bootc:ro,Z" \
    -v /mnt:/var/mnt \
    "$IMAGE" \
        bootc install to-filesystem \
            --composefs-backend \
            --karg enforcing=0 --karg console=ttyS0,115000n --karg audit=0 --karg hello=hi --karg-delete hello \
            --bootloader="$BOOTLOADER" \
            --source-imgref "containers-storage:$IMAGE" \
            /var/mnt 
