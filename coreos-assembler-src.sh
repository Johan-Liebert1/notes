#!/bin/bash

COREOS_ASSEMBLER_CONTAINER_LATEST="quay.io/coreos-assembler/coreos-assembler:latest"

check_image() {
   env | grep COREOS_ASSEMBLER

   if [[ -z ${COREOS_ASSEMBLER_CONTAINER} ]] && $(podman image exists ${COREOS_ASSEMBLER_CONTAINER_LATEST}); then
       local -r cosa_build_date_str="$(podman inspect -f "{{.Created}}" ${COREOS_ASSEMBLER_CONTAINER_LATEST} | awk '{print $1}')"
       local -r cosa_build_date="$(date -d ${cosa_build_date_str} +%s)"
       if [[ $(date +%s) -ge $((cosa_build_date + 60*60*24*7)) ]] ; then
         echo -e "\e[0;33m----" >&2
         echo "The COSA container image is more than a week old and likely outdated." >&2
         echo "You should pull the latest version with:" >&2
         echo "podman pull ${COREOS_ASSEMBLER_CONTAINER_LATEST}" >&2
         echo -e "----\e[0m" >&2
       fi
   fi
}

if [[ $1 == "vol" ]]; then
    cosa() {
        printf "\e[1;36m cosa volume \e[0m \n"

        check_image

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
                  ${COREOS_ASSEMBLER_CONFIG_GIT:+-v=$COREOS_ASSEMBLER_CONFIG_GIT:/srv/src/config/:ro}     \
                  ${COREOS_ASSEMBLER_GIT:+-v=$COREOS_ASSEMBLER_GIT/src/:/usr/lib/coreos-assembler/:ro}    \
                  ${COREOS_ASSEMBLER_ADD_CERTS:+-v=/etc/pki/ca-trust:/etc/pki/ca-trust:ro}                \
                  ${COREOS_ASSEMBLER_CONTAINER_RUNTIME_ARGS}                                              \
                  ${COREOS_ASSEMBLER_CONTAINER:-$COREOS_ASSEMBLER_CONTAINER_LATEST} "$@"
        rc=$?; return $rc
    }
else
    cosa() {
        printf "\e[1;36m cosa NON volume \e[0m \n"

        check_image

        podman run --rm -ti --security-opt=label=disable --privileged           \
                  --uidmap=1000:0:1 --uidmap=0:1:1000 --uidmap=1001:1001:64536 \
                  -v="${PWD}:/srv/" --device=/dev/kvm --device=/dev/fuse         \
                  --tmpfs=/tmp --name=cosa                                     \
                  ${COREOS_ASSEMBLER_CONFIG_GIT:+-v=$COREOS_ASSEMBLER_CONFIG_GIT:/srv/src/config/:ro}     \
                  ${COREOS_ASSEMBLER_GIT:+-v=$COREOS_ASSEMBLER_GIT/src/:/usr/lib/coreos-assembler/:ro}    \
                  ${COREOS_ASSEMBLER_ADD_CERTS:+-v=/etc/pki/ca-trust:/etc/pki/ca-trust:ro}                \
                  ${COREOS_ASSEMBLER_CONTAINER_RUNTIME_ARGS}                                              \
                  ${COREOS_ASSEMBLER_CONTAINER:-$COREOS_ASSEMBLER_CONTAINER_LATEST} "$@"
        rc=$?; return $rc
    }
fi

# Building
cosa_build() {
    cosa build
    cosa osbuild qemu
}
