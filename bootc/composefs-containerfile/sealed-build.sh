#!/bin/bash

set -eux

# Gen secboot keys
/home/pragyan/notes/virtual-machines/secureboot.sh

podman build \
    -t bootc-uki-sealed \
    -v "$(pwd)":/run/src \
    --skip-unused-stages=false \
    --secret=id=secureboot_key,src=secureboot/db.key \
    --secret=id=secureboot_cert,src=secureboot/db.crt \
    -f ./Containerfile.uki.sealed
