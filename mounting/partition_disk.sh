#!/bin/bash

if [[ "$PWD" != "$HOME/notes/bootc" ]]; then
    echo "Run this command from $HOME/notes/bootc"
    exit 1
fi

sudo umount -R /mnt

set -ex

rm -rf test.img composefs-only.qcow2
truncate -s 15G test.img

cat > buf <<EOF
    label: gpt
    label-id: $(uuidgen)
    size=512MiB, type=0FC63DAF-8483-4772-8E79-3D69D8477DE4, name="boot"
    size=512MiB, type=C12A7328-F81F-11D2-BA4B-00A0C93EC93B, name="EFI-SYSTEM"
    type=6523f8ae-3eb1-4e2a-a05a-18b695ae656f, name="root"
EOF

sudo losetup /dev/loop0 test.img
sudo sfdisk --wipe=always /dev/loop0 < buf

# To make sure kernel updates
sudo partprobe /dev/loop0

sudo mkfs.ext4 /dev/loop0p1 -L boot
sudo mkfs.fat /dev/loop0p2
sudo mkfs.ext4 /dev/loop0p3 -O verity -L root -U 6523f8ae-3eb1-4e2a-a05a-18b695ae656f

sudo mount /dev/loop0p3 /mnt
sudo mkdir /mnt/boot

./install-to-fs.sh

sudo umount -R /mnt

sudo mount /dev/loop0p2 /mnt
sudo cp /usr/lib/systemd/boot/efi/systemd-bootx64.efi /mnt/EFI/fedora/grubx64.efi
sudo umount -R /mnt

sudo losetup -d /dev/loop0

qemu-img convert -f raw -O qcow2 test.img composefs-only.qcow2
