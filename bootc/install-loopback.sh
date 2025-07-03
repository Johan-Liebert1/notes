#!/bin/bash

sudo podman run --rm --privileged --pid=host \
    --security-opt label=type:unconfined_t \
    --env RUST_LOG=debug \
    --env SLEEP_YO=sleep \
    -v /dev:/dev \
    -v /var/lib/containers:/var/lib/containers \
    -v /home/pragyan/RedHat/bootc/target/release/bootc:/usr/bin/bootc:ro,Z \
    -v .:/output quay.io/fedora/fedora-bootc:42 \
    bootc install to-disk --composefs-native --generic-image --karg mykarg --via-loopback --filesystem=ext4 --wipe /output/test.img


# podman run \
# --rm --privileged \
# --pid=host \
# -v /dev:/dev \
# -v /var/lib/containers:/var/lib/containers \
# -v /var/srv/bootc:/usr/bin/bootc:ro,Z \
# -v /var/tmp:/var/tmp \
# --security-opt label=type:unconfined_t \
# --env RUST_LOG=debug \
# --env RUST_BACKTRACE=1 \
# $IMAGE \
# bootc install to-disk /dev/vdb --target-imgref=$IMAGE --source-imgref="containers-storage:$IMAGE" --composefs-native --filesystem=ext4 --wipe
