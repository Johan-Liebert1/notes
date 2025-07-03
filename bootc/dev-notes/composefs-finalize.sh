#!/bin/bash

if [ -f /sysroot/boot/grub2/user.cfg.staged ]; then
    echo "Migrating /sysroot/boot/grub2/user.cfg.staged"

    mv -f /sysroot/boot/grub2/user.cfg.staged /sysroot/boot/grub2/user.cfg
fi
