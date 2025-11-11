#!/bin/bash

set -x

IMAGE="localhost/bootc-coreos:latest"

sudo podman run --rm --net=host --privileged --pid=host \
    --security-opt label=type:unconfined_t \
    --env RUST_LOG=debug \
    -v /dev:/dev \
    -v /var/lib/containers:/var/lib/containers \
    -v /home/pragyan/RedHat/bootc/target/release/bootc:/usr/bin/bootc:ro,Z \
    -v /mnt:/var/mnt \
    "$IMAGE" \
        bootc install to-filesystem \
            --composefs-backend \
            --karg enforcing=0 --karg console=ttyS0,115000n --karg audit=0 \
            /var/mnt --source-imgref "containers-storage:$IMAGE"
