#!/bin/bash

set -x 

case "$1" in 
        "m")
                mount /dev/vdb3 /mnt
                mount /dev/vdb2 /mnt/boot/efi
        ;;

        "u")
                umount -R /mnt
        ;;

        "fix-boot")
                cp -r /mnt/boot/efi/loader /mnt/boot
                cp -r /mnt/boot/efi/EFI /mnt/boot
        ;;

        *)
                echo "unknown $1"
        ;;
esac
