#!/bin/bash

# Create a disk
truncate -s 15G test.img

losetup /dev/loop0 ./test.img
sfdisk --wipe=always /dev/loop0 < ../bootc/buf

partprobe /dev/loop0
fdisk -l /dev/loop0

# Encrypting
cryptsetup -v luksFormat /dev/loop0p3
fdisk -l /dev/loop0

## Mounting

# Decrypt
cryptsetup open /dev/loop0p3 loop-test # This will create /dev/mapper/loop-test

# Make the decrypted drive ext4
mkfs.ext4 /dev/mapper/loop-test

mount /dev/mapper/loop-test /mnt

## Unmounting and closing
umount /mnt

cryptsetup close loop-test
