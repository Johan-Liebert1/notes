#!/bin/bash

if [[ "$PWD" != "$HOME/notes/bootc" ]]; then
    echo "Run this command from $HOME/notes/bootc"
    exit 1
fi

sudo umount -R /mnt

set -ex

rm -f test.img composefs-only.qcow2
truncate -s 10G test.img

BOOTFS_UUID="96d15588-3596-4b3c-adca-a2ff7279ea63"
ROOTFS_UUID="4f68bce3-e8cd-4db1-96e7-fbcaf984b709"

cat > buf <<EOF
    label: gpt
    label-id: $(uuidgen)
    size=512MiB, type=C12A7328-F81F-11D2-BA4B-00A0C93EC93B, name="EFI-SYSTEM"
    size=512MiB, type=0FC63DAF-8483-4772-8E79-3D69D8477DE4, name="boot"
                 type=4F68BCE3-E8CD-4DB1-96E7-FBCAF984B709, name="root"
EOF

sudo losetup /dev/loop0 test.img
sudo sfdisk --wipe=always /dev/loop0 < buf

# To make sure kernel updates
sudo partprobe /dev/loop0

sudo mkfs.fat /dev/loop0p1
sudo mkfs.ext4 /dev/loop0p2           -L boot -U $BOOTFS_UUID
sudo mkfs.ext4 /dev/loop0p3 -O verity -L root -U $ROOTFS_UUID

sudo mount /dev/loop0p3 /mnt
sudo mkdir /mnt/boot

./install-to-fs.sh

sudo umount -R /mnt

sudo mount /dev/loop0p1 /mnt
sudo cp /usr/lib/systemd/boot/efi/systemd-bootx64.efi /mnt/EFI/fedora/grubx64.efi
sudo sed -i "s;options ;options console=tty0 console=ttyS0,115000n enforcing=0 audit=0 ;" /mnt/loader/entries/bootc-composefs-1.conf
# sudo sed -i "s;6523f8ae-3eb1-4e2a-a05a-18b695ae656f ; ;" /mnt/loader/entries/bootc-composefs-1.conf
sudo umount -R /mnt

sudo losetup -d /dev/loop0

qemu-img convert -f raw -O qcow2 test.img composefs-only.qcow2
