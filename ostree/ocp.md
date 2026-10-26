```bash
sudo setenforce 0

export IMAGE=192.168.122.1:5000/openshift-release-dev/ocp-v4.0-art-dev
export IMGAGE=192.168.122.1:5000/bootupd-fix:latest

sudo podman run --privileged -e RUST_LOG=debug --pid=host --net=host \
    -v /:/run/host \
    -v /sys/fs/selinux:/sys/fs/selinux  \
    $IMAGE \
    rpm-ostree ex deploy-from-self /run/host

sudo podman run --privileged -it -e RUST_LOG=debug --pid=host --net=host \
    -v /:/run/host \
    -v /sys/fs/selinux:/sys/fs/selinux  \
    $IMAGE bash

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

# oci image
ostree-container container image pull "$REPO" ostree-unverified-image:containers-storage:localhost:5000/bootupd
ostree-container container encapsulate --repo "$REPO" $COMMIT containers-storage:final-image

# from
# No changes in … => CHECKSUM
COMMIT=YOUR_NEW_OSTREE_COMMIT_CHECKSUM

podman run --rm --privileged \
  -v "$WORK:/work:Z" \
  --entrypoint ostree "$IMAGE" \
  container encapsulate --repo=/work/repo "$COMMIT" \
  oci-archive:/work/bootupd-fixed.oci.tar
```
