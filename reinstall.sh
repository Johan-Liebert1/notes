#!/bin/bash

podman run \
    --rm \
    --privileged \
    --pid=host \
    --user=root:root \
    -v /var/lib/containers:/var/lib/containers \
    -v /dev:/dev \
    --security-opt label=type:unconfined_t \
    -v /:/target:rslave \
    localhost/bootc-reinstall-same \
    bootc install to-existing-root \
        --acknowledge-destructive \
        --skip-fetch-check \
        --composefs-backend \
        --disable-selinux 
