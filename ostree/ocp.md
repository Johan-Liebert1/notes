[core@localhost ~]$ systemctl enable bootloader-update.service 
==== AUTHENTICATING FOR org.freedesktop.systemd1.manage-unit-files ====
Authentication is required to manage system service or unit files.
Authenticating as: CoreOS Admin (core)
Password: 
==== AUTHENTICATION COMPLETE ====
Created symlink /etc/systemd/system/multi-user.target.wants/bootloader-update.service → /usr/lib/systemd/system/bootloader-update.service.
==== AUTHENTICATING FOR org.freedesktop.systemd1.reload-daemon ====
Authentication is required to reload the systemd state.
Authenticating as: CoreOS Admin (core)
Password: 
==== AUTHENTICATION COMPLETE ====

```bash

export IMAGE=192.168.122.1:5000/final-image
export IMAGE=192.168.122.1:5000/bootup-ocp-test-0.2.35-patched:final
export IMAGE=192.168.122.1:5000/openshift-release-dev/ocp-v4.0-art-dev:9.6
export IMAGE=192.168.122.1:5000/quay.io/openshift-release-dev/ocp-v4.0-art-dev:9.8 

sudo setenforce 0

sudo podman run --privileged -e RUST_LOG=debug --pid=host --net=host \
    -v /:/run/host \
    -v /sys/fs/selinux:/sys/fs/selinux  \
    $IMAGE \
    rpm-ostree ex deploy-from-self /run/host

sudo podman run --privileged -it -e RUST_LOG=debug --pid=host --net=host \
    -v /:/run/host \
    -v /sys/fs/selinux:/sys/fs/selinux  \
    $IMAGE bash

# another upgrade
rpm-ostree rebase \
    ostree-unverified-image:containers-storage:192.168.122.1:5000/quay.io/openshift-release-dev/ocp-v4.0-art-dev:9.8

WORK=$(mktemp -d)

podman save --format oci-archive \
  -o "$WORK/image.oci.tar" "$IMAGE"

podman run --rm --privileged \
  -v "$WORK:/work:Z" \
  --entrypoint /bin/sh "$IMAGE" -ec '
    ostree --repo=/work/repo init --mode=bare-user
    ostree container image pull \
      --ostree-digestfile=/work/imported-commit \
      /work/repo \
      ostree-unverified-image:oci-archive:/work/image.oci.tar
  '

# non-root some issue with sudo losing setuid bit
export REPO=/var/test-repo; mkdir -p $REPO; ostree init --repo $REPO --mode=bare-user


export REPO=/var/test-repo; mkdir -p $REPO; ostree init --repo $REPO

# NOTE: ostree-container was merged into bootc

# oci archive
ostree-container container image pull "$REPO" ostree-unverified-image:oci-archive:/tmp/bootupd.oci
ostree-container container encapsulate --repo "$REPO" $COMMIT oci-archive:/final-fix.tar

export IMAGE=localhost:5000/bootup-ocp-test-0.2.35-patched:old

# from
# No changes in … => CHECKSUM
export COMMIT=521990810fbc07e66412753c3421c978b3a2ba912cda7c6526e15001bc27c566
export FINAL_IMAGE=localhost:5000/bootup-ocp-test-0.2.35-patched:final

# oci image
/home/ppoudyal/RedHat/bootc/target/release/bootc internals ostree-ext container image pull "$REPO" ostree-unverified-image:containers-storage:$IMAGE
/home/ppoudyal/RedHat/bootc/target/release/bootc internals ostree-ext container encapsulate --repo "$REPO" $COMMIT containers-storage:$FINAL_IMAGE


podman run --rm --privileged \
  -v "$WORK:/work:Z" \
  --entrypoint ostree "$IMAGE" \
  container encapsulate --repo=/work/repo "$COMMIT" \
  oci-archive:/work/bootupd-fixed.oci.tar
```
