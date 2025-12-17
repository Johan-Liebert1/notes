#!/bin/bash

if [[ $1 == "vol" ]]; then
    cosa() {
        printf "\e[1;36m cosa volume \e[0m \n"

        volume_mounts=()

        # Binaries
        volume_mounts+=(-v /home/pragyan/RedHat/coreos-assembler/bin/coreos-assembler:/usr/bin/coreos-assembler)
        volume_mounts+=(-v /home/pragyan/RedHat/coreos-assembler/bin/kola:/usr/bin/kola)
        volume_mounts+=(-v /home/pragyan/RedHat/coreos-assembler/bin/ore:/usr/bin/ore)
        volume_mounts+=(-v /home/pragyan/RedHat/coreos-assembler/bin/plume:/usr/bin/plume)

        # Scripts
        volume_mounts+=(-v /home/pragyan/RedHat/coreos-assembler/src:/usr/lib/coreos-assembler)

        podman run --rm -ti --tty --security-opt=label=disable --privileged    \
                  --uidmap=1000:0:1 --uidmap=0:1:1000 --uidmap=1001:1001:64536 \
                  -v="${PWD}:/srv/" --device=/dev/kvm --device=/dev/fuse       \
                  --tmpfs=/tmp --name=cosa                                     \
                  "${volume_mounts[@]}"                                        \
                  quay.io/coreos-assembler/coreos-assembler:latest "$@"
        rc=$?; return $rc
    }
else
    cosa() {
        printf "\e[1;36m cosa NON volume \e[0m \n"

        podman run --rm -ti --security-opt=label=disable --privileged           \
                  --uidmap=1000:0:1 --uidmap=0:1:1000 --uidmap=1001:1001:64536 \
                  -v="${PWD}:/srv/" --device=/dev/kvm --device=/dev/fuse         \
                  --tmpfs=/tmp --name=cosa                                     \
                  quay.io/coreos-assembler/coreos-assembler:latest "$@"
        rc=$?; return $rc
    }
fi
