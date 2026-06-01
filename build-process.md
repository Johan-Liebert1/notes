# Package build first 

```bash
cargo run -p xtask check-buildsys

# just package
podman build \
    --build-arg=base=quay.io/centos-bootc/centos-bootc:stream10 \
    --build-arg=variant=ostree \
    --build-arg=bootloader=grub \
    --build-arg=boot_type=bls \
    --build-arg=seal_state=unsealed \
    --build-arg=filesystem=ext4 \
    --build-arg=baseconfigs= \
    --build-arg=SOURCE_DATE_EPOCH=1780066081 \
    --build-arg=pkgversion=202605291448.g0055b6cffd \
    -t localhost/bootc-pkg \
    --target=build .

[1/8] STEP 1/2: FROM scratch AS src
[1/8] STEP 2/2: COPY . /src
--> 6b2b761576a3
[2/8] STEP 1/2: FROM scratch AS packaging
[2/8] STEP 2/2: COPY contrib/packaging /
--> 42b45a38da87
[3/8] STEP 1/6: FROM quay.io/centos-bootc/centos-bootc:stream10 AS buildroot
Trying to pull quay.io/centos-bootc/centos-bootc:stream10...
Getting image source signatures
Copying blob sha256:0397b23a10ab451b6a855faca307d97d340df99c501c06cfd9befcefd022f7e4
[...]
Copying config sha256:cb2c563c91df6ea1e82038b57cf107391a6ef6e67be241fb3726df6b20f5b904
Writing manifest to image destination
[3/8] STEP 2/6: ARG initramfs=1
--> 2897b10a5de3
[3/8] STEP 3/6: RUN --mount=type=tmpfs,target=/run --mount=type=tmpfs,target=/tmp \
--mount=type=bind,from=packaging,src=/,target=/run/packaging     /run/packaging/install-buildroot


# Part 2

cargo xtask local-rust-deps
    Finished `dev` profile [optimized + debuginfo] target(s) in 0.12s
     Running `target/debug/xtask local-rust-deps`

local_deps_args=

podman build \
    --build-arg=base=quay.io/centos-bootc/centos-bootc:stream10 \
    --build-arg=variant=ostree \
    --build-arg=bootloader=grub \
    --build-arg=boot_type=bls \
    --build-arg=seal_state=unsealed \
    --build-arg=filesystem=ext4 \
    --build-arg=baseconfigs= \
    --build-arg=SOURCE_DATE_EPOCH=1780066081 \
    --build-arg=pkgversion=202605291448.g0055b6cffd \
    -t localhost/bootc-pkg \
    --target=build .

# logs
./package.logs
```

# Second is "Unit and Container integration tests"

```bash
# just test-container

cargo xtask local-rust-deps # This rebuilds the binary again after the package step

podman build \
    --build-arg=base=quay.io/centos-bootc/centos-bootc:stream10 \
    --build-arg=variant=ostree \
    --build-arg=bootloader=grub \
    --build-arg=boot_type=bls \
    --build-arg=seal_state=unsealed \
    --build-arg=filesystem=xfs \
    --build-arg=baseconfigs= \
    --build-arg=SOURCE_DATE_EPOCH=1780066081 \
    --build-arg=pkgversion=202605291448.g0055b6cffd  \
    -t localhost/bootc-pkg \
    --target=build .

# The above command should've been the same as the `just package` one and steps are cached
# but the following isn't

[1/8] STEP 1/2: FROM scratch AS src
[1/8] STEP 2/2: COPY . /src
--> Using cache 6af8ba80d7fcd64e8198da8ffb894e579aada88853eead42766b9f3737b2bdf3
--> 6af8ba80d7fc
[2/8] STEP 1/2: FROM scratch AS packaging
[2/8] STEP 2/2: COPY contrib/packaging /
--> Using cache 36f5c395eae622687a663c30e40d1c18494fa7c5dacf94203522c38896ed8d04
--> 36f5c395eae6
[3/8] STEP 1/6: FROM quay.io/centos-bootc/centos-bootc:stream10 AS buildroot
[3/8] STEP 2/6: ARG initramfs=1
--> ce0ea47b202e
[3/8] STEP 3/6: RUN --mount=type=tmpfs,target=/run --mount=type=tmpfs,target=/tmp \
--mount=type=bind,from=packaging,src=/,target=/run/packaging     /run/packaging/install-buildroot


```
