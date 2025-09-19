#!/bin/bash

set -ex

IMAGE="localhost:5000/bootc-uki"

rm -f test.img composefs-only.qcow2
truncate test.img -s 15G

sudo podman run --rm --net=host --privileged --pid=host \
    --security-opt label=type:unconfined_t \
    --env RUST_LOG=debug \
    -v /dev:/dev \
    -v /var/lib/containers:/var/lib/containers \
    -v /home/pragyan/RedHat/bootc-bak/target/release/bootc:/usr/bin/bootc:ro,Z \
    -v .:/output \
    $IMAGE \
        bootc install to-disk \
        --composefs-native \
        --bootloader=systemd \
        --source-imgref "docker://$IMAGE" \
        --generic-image --via-loopback --filesystem=ext4 --wipe \
        /output/test.img

sudo losetup /dev/loop0 ./test.img
sudo partprobe /dev/loop0
sudo mount /dev/loop0p2 /mnt
sudo cp /usr/lib/systemd/boot/efi/systemd-bootx64.efi /mnt/EFI/fedora/grubx64.efi

sudo umount /mnt
sudo losetup -d /dev/loop0

qemu-img convert -f raw -O qcow2 test.img composefs-only.qcow2
