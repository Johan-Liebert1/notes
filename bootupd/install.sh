#!/bin/bash

# podman build -t bootupd-test .

set -ex

if [[ $1 == "status" ]]; then
        cmd=(bootupctl status)
elif [[ $1 == "meta" ]]; then
        cmd=(bootupctl backend generate-update-metadata --bootloader systemd)
elif [[ $1 == "shell" ]]; then
        cmd=(bash)
else
        cmd=(bootupctl backend install --bootloader systemd /var/mnt -vvvv)
fi

sudo podman run --rm --net=host --privileged --pid=host -it \
    --security-opt label=type:unconfined_t \
    --env RUST_LOG=trace \
    -v /home/pragyan/RedHat/bootupd/target/release/bootupd:/usr/sbin/bootupctl:Z,ro \
    -v /dev:/dev \
    -v /var/lib/containers:/var/lib/containers \
    -v /run/udev:/run/udev \
    -v /var/mnt:/var/mnt \
    "localhost/bootupd-bls-test:latest" \
    "${cmd[@]}"
