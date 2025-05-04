# The boot directory

```bash
tree /boot
.
├── 9c43679c9e8543769e9ee7d8cf4d6312
│   └── 6.14.4-200.fc41.x86_64
│       ├── initrd
│       └── linux
├── EFI
│   ├── BOOT
│   │   └── BOOTX64.EFI
│   └── systemd
│       └── systemd-bootx64.efi
├── NvVars
├── loader
│   ├── entries
│   │   └── 9c43679c9e8543769e9ee7d8cf4d6312-6.14.4-200.fc41.x86_64.conf
│   ├── loader.conf
│   └── random-seed
└── symvers-6.14.4-200.fc41.x86_64.xz

8 directories, 9 files
```

We install these

```bash
dnf --setopt keepcache=1 install --allowerasing -y systemd util-linux skopeo composefs dosfstools kernel openssh-server

# The `kernel` package when installed runs some scripts inside /usr/lib/kernel/install.d
```

## BLS Entry

* We have a file `examples/bls/extra/usr/lib/kernel/install.conf.d/37composefs.conf` with the following contents

- 37composefs.conf

```conf
layout = bls
```

We copy this to `/usr/lib/kernel/install.conf.d/37composefs.conf`, which is used when creating bootloader entries


# ============================ Dracut ==========================

`dracut` is a tool used to generate the `initramfs` (initial RAM filesystem) for Linux systems.


We have some folders that we copy to `/` inside the container. These contain our custom configuration for dracut, systemd etc


```bash
extra
├── etc
│   ├── mkinitcpio.conf
│   └── resolv.conf -> ../run/systemd/resolve/stub-resolv.conf
├── root
└── usr
    └── lib
        ├── dracut
        │   ├── dracut.conf.d
        │   │   └── 37composefs.conf
        │   └── modules.d
        │       └── 37composefs
        │           ├── composefs-setup-root
        │           ├── composefs-setup-root.service
        │           └── module-setup.sh
        ├── initcpio
        │   ├── hooks
        │   │   └── composefs
        │   └── install
        │       └── composefs
        ├── kernel
        │   └── install.conf.d
        │       └── 37composefs.conf
        └── systemd
            ├── network
            │   └── 37-wired.network
            └── system
                └── systemd-growfs-root.service.d
                    └── 37-composefs.conf

18 directories, 11 files
```

##### Dracut Confs

In `/usr/lib/dracut` we have 

`dracut.conf.d/37composefs.conf`
```bash
# we want to make sure the virtio disk drivers get included
hostonly=no

# we need to force these in via the initramfs because we don't have modules in
# the base image
force_drivers+=" virtio_net vfat "
```

It tells dracut to include the 37composefs module during initramfs generation.

##### Dracut modules

We have the same named folder `37composefs` in `dracut/modules.d`

`dracut` will run `modules-setup.sh` to

* Decide whether to include the module (`check()` function)
* Specify what to install (`install()` function)
* Copy files into initramfs based on what `install()` says

This is `dracut/modules.d/37composefs/module-setup.sh`

```bash
#!/usr/bin/bash

check() {
    return 0
}

depends() {
    return 0
}

install() {
    # inst is a dracut-provided helper function used to copy files into the initramfs.
    # has the syntax -> inst SOURCE DEST
    inst \
        "/usr/bin/strace" /bin/strace

    inst \
        "${moddir}/composefs-setup-root" /bin/composefs-setup-root


    # Installs the systemd unit file into the initramfs's unit directory.
    inst \
        "${moddir}/composefs-setup-root.service" \
        "${systemdsystemunitdir}/composefs-setup-root.service"

    $SYSTEMCTL -q --root "${initdir}" add-wants \
        'initrd-root-fs.target' 'composefs-setup-root.service'
}
```

# ================================ /dev/gpt-auto-root ==============================================

This is a udev created symlink used by `systemd-gpt-auto-generator`

`/dev/gpt-auto-root` points to the linux root partition

This is usually used when we are using systemd-boot and boot without specifying a root device (root=),
so systemd tries to auto-discover it using GPT partition types

Example

#### Composefs boot loader entry

```bash
# Boot Loader Specification type#1 entry
# File created by /usr/lib/kernel/install.d/90-loaderentry.install (systemd 256.12-1.fc41)
title      Fedora Linux 41 (Container Image)
version    6.14.4-200.fc41.x86_64
machine-id 9c43679c9e8543769e9ee7d8cf4d6312
sort-key   fedora

# Notice no "root=" here
options    systemd.machine_id=9c43679c9e8543769e9ee7d8cf4d6312 console=ttyS0,115200 composefs=db963c0091f15e6883ddf359fd11b719caa8043f433878474575a82cd3b552cf rw

linux      /9c43679c9e8543769e9ee7d8cf4d6312/6.14.4-200.fc41.x86_64/linux
initrd     /9c43679c9e8543769e9ee7d8cf4d6312/6.14.4-200.fc41.x86_64/initrd
```

#### My system's boot loader entry

```bash
title          Fedora Linux (6.14.0-63.fc42.x86_64) 42 (Workstation Edition)
version        6.14.0-63.fc42.x86_64
linux          /vmlinuz-6.14.0-63.fc42.x86_64
initrd         /initramfs-6.14.0-63.fc42.x86_64.img $tuned_initrd

# Here we have passed the root partitionuuid
options        root=UUID=d309575d-f0b4-4139-9219-84ae8bae6411 ro rootflags=subvol=root rhgb quiet  $tuned_params

grub_users     $grub_users
grub_arg       --unrestricted
grub_class     fedora
```


# ============================================ setup root ===========================================

Q. Who's mounting /sysroot?

This all happens inside the `initramfs`

We get the image name from `/proc/cmdline`

```bash
initrd=\1a9a88b3266f4ba5a5fd65dbdd525d06\6.14.4-200.fc41.x86_64\initrd systemd.machine_id=1a9a88b3266f4ba5a5fd65dbdd525d06 \
console=ttyS0,115200 composefs=6c315f5307f9d66fc98bf7d6e474b460cb8ea8b457f7667c38a066afeb91422d rw
```

This is the image name `composefs=6c315f5307f9d66fc98bf7d6e474b460cb8ea8b457f7667c38a066afeb91422d rw` (6c315f5307f9d66fc98bf7d6e474b460cb8ea8b457f7667c38a066afeb91422d)

#### fsopen
The `fsopen` syscall is used to initiate the creation of a new superblock for a filesystem in the Linux kernel.
It's primarily used with the mount API introduced in Linux 5.2+.

```c
int fsopen(const char *fs_name, unsigned int flags);

// fs_name: Filesystem type (e.g., "ext4", "xfs").
// flags: Reserved (must be 0 for now).
// Returns: A file descriptor (fs context) used with other syscalls like fsconfig, fsmount, etc.

// Example Workflow:

fsopen("ext4", 0) // get fs context.

fsconfig() // configure mount options.

fsmount() // create a mount.

move_mount() // attach it to the filesystem hierarchy (optional)
```

### == Mounting composefs ==

01. Mount the `erofs` image using `fsmount`, i.e. created a detached mount (not appearing on the filesystem)

    On pre `6.15` kernel, we mount it to a `tmpfs` using `move_mount` 

    Required before Linux 6.15: it's not possible to use detached mounts with `OPEN_TREE_CLONE` or
    `overlayfs`.  

    Convert them into a non-floating form by mounting them on a temporary directory and
    reopening them as an O_PATH fd.


02. Mount `composefs` as an `overlayfs` mount type.

```rust
// Open a filesystem context for the overlay mount type — so we're creating an overlayfs mount.
let overlayfs = FsHandle::open("overlay")?;

// This sets the source of the lowerdir to composefs:{name} — a special syntax telling overlayfs to use a composefs filesystem object as its lower layer.
fsconfig_set_string(overlayfs.as_fd(), "source", format!("composefs:{name}"))?;

// Some standard overlayfs mount options
fsconfig_set_string(overlayfs.as_fd(), "metacopy", "on")?;
fsconfig_set_string(overlayfs.as_fd(), "redirect_dir", "on")?;
fsconfig_set_string(overlayfs.as_fd(), "verity", "require")?;

overlayfs_set_fd(overlayfs.as_fd(), "lowerdir+", erofs_mnt)?;

// data dir here is the repo's objects directory
overlayfs_set_fd(overlayfs.as_fd(), "datadir+", data.as_fd())?;


// Finalize and create the overlay mount
fsconfig_create(overlayfs.as_fd())?;
```

After creating our mount, we will detach the old sysroot mount, if it exists

```rust
// empty path '""' = detatch the mount
let sysroot_clone = bind_mount(&sysroot, "")?;

// Then we mount our sysroot
mount_at(&composefs_image, CWD, &args.sysroot)?;
```





