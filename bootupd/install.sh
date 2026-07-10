#!/bin/bash

# podman build -t bootupd-test .

set -ex

if [[ $1 == "status" ]]; then
        cmd=(bootupctl status)
elif [[ $1 == "meta" ]]; then
        cmd=(bootupctl backend generate-update-metadata --bootloader grub-cc)
elif [[ $1 == "shell" ]]; then
        cmd=(bash)
else
        cmd=(bootupctl backend install --bootloader grub-cc /var/mnt -vvvv)
fi

sudo podman run --rm --net=host --privileged --pid=host \
    -it \
    --security-opt label=type:unconfined_t \
    --env RUST_LOG=trace \
    -v /var/bootupd:/usr/sbin/bootupctl:Z,ro \
    -v /dev:/dev \
    -v /var/lib/containers:/var/lib/containers \
    -v /var/mnt:/var/mnt \
    "localhost/bootupd-test" \
    "${cmd[@]}"
