#!/bin/bash

set -xu

IMAGE=$1
# BOOTLOADER=$2

sudo podman run --rm --net=host --privileged --pid=host \
    --security-opt label=type:unconfined_t \
    --env RUST_LOG=debug \
    -v /dev:/dev \
    -v /var/lib/containers:/var/lib/containers \
    -v /home/pragyan/RedHat/bootc-bak/target/release/bootc:/usr/bin/bootc:ro,Z \
    -v /var//mnt:/var/mnt \
    "$IMAGE" \
        bootc install to-filesystem \
            --karg enforcing=0 --karg console=ttyS0,115000n --karg audit=0 \
            --bootloader=none \
            --source-imgref "containers-storage:localhost/bootc-bls" \
            /var/mnt 
