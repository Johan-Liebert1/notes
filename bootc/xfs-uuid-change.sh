#!/bin/bash

if [[ $(id -u) -ne 0 ]]; then
    echo "Need to be root"
    exit 1
fi

loopdev=$(losetup -f)

losetup "$loopdev"  /home/pragyan/notes/bootc/fcos-test.img
partprobe "$loopdev"

sleep 0.3

lsblk -o name,parttype,uuid,parttypename,label,partuuid "$loopdev" > "lsblk"

mount "${loopdev}"p3 /mnt
mount "${loopdev}"p2 /mnt/boot/efi

echo 'set BOOT_UUID="910678ff-f77e-4a7d-8d53-86f2ac47a823"' > /mnt/boot/grub2/bootuuid.cfg
echo 'set BOOT_UUID="910678ff-f77e-4a7d-8d53-86f2ac47a823"' > /mnt/boot/efi/EFI/fedora/bootuuid.cfg

umount -R /mnt

xfs_admin -U 910678ff-f77e-4a7d-8d53-86f2ac47a823 "${loopdev}"p3

losetup -d "${loopdev}"
