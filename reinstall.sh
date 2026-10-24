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


podman run  \
--rm  \
--privileged  \
--pid=host  \
--user=root:root  \
-e RUST_LOG=debug \
-e BOOTC_BOOTLOADER_DEBUG=1 \
-v /var/lib/containers:/var/lib/containers  \
-v /dev:/dev  \
-v /var/bootc:/usr/bin/bootc:Z,ro \
--security-opt label=type:unconfined_t  \
-v /:/target:rslave  \
$IMAGE  \
bootc install to-existing-root  \
    --acknowledge-destructive  \
    --skip-fetch-check  \
    --composefs-backend  \
    --disable-selinux 


podman run  \
--rm  \
--privileged  \
--pid=host  \
--user=root:root  \
-it \
-e RUST_LOG=debug \
-e BOOTC_BOOTLOADER_DEBUG=1 \
-v /var/lib/containers:/var/lib/containers  \
-v /dev:/dev  \
--security-opt label=type:unconfined_t  \
-v /:/target:rslave  \
$IMAGE bash
