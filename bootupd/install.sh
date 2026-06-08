#!/bin/bash

podman build -t bootupd-test .

sudo podman run --rm --net=host --privileged --pid=host \
    --security-opt label=type:unconfined_t \
    --env RUST_LOG=debug \
    -v /dev:/dev \
    -v /var/lib/containers:/var/lib/containers \
    -v /var/mnt:/var/mnt \
    "localhost/bootupd-test" \
    bootupctl backend install --bootloader grub-cc /var/mnt -vvvv
