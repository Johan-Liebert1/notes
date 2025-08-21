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
/**
    * fs_name: Filesystem type (e.g., "ext4", "xfs", "overlay").
    * flags: Reserved (must be 0 for now).

    * Returns: A file descriptor (fs context) used with other syscalls like fsconfig, fsmount, etc.
*/
int fsopen(const char *fs_name, unsigned int flags);

// Example Workflow:

fsopen("ext4", 0) // get fs context.

fsconfig() // configure mount options.

fsmount() // create a mount.

move_mount() // attach it to the filesystem hierarchy (optional)
```

### == Mounting composefs ==

01. Mount the `erofs` image using `fsmount`, i.e. created a detached mount (not appearing on the filesystem)

    On pre `6.15` kernel, we mount it to a `tmpfs` using `move_mount` 

```rust
// See: https://github.com/sunfishcode/linux-mount-api-documentation
pub fn erofs_mount(image: OwnedFd) -> Result<OwnedFd> {
    // Prepares an open erofs image file for mounting.  On kernels versions after 6.12 this is a
    // simple passthrough.  On older kernels (like on RHEL 9) we need to create a loopback device.
    let image = make_erofs_mountable(image)?;

    // Creates a blank filesystem configuration context within the kernel for the filesystem named in the fsname parameter,
    // puts it into creation mode and attaches it to a file descriptor, which it then returns. 
    // The file descriptor can be marked close-on-exec by setting FSOPEN_CLOEXEC in flags.
    // 
    // After calling fsopen(), the file descriptor should be passed to the fsconfig(2)
    // system call, using that to specify the desired filesystem and security parameters. When the parameters are all set, the fsconfig()
    // system call should then be called again with FSCONFIG_CMD_CREATE (fsconfig_create) as the command argument to effect the creation.
    // 
    // 
    // NOTE:
    // Depending on the filesystem type and parameters, this may rather share an existing in-kernel filesystem representation instead of creating a new one.
    // In such a case, the parameters specified may be discarded or may overwrite the parameters set by a previous mount - at the filesystem's discretion.
    // The file descriptor also serves as a channel by which more comprehensive error, warning and information messages may be retrieved from the kernel using read(2).
    // 
    // Once the creation command has been successfully run on a context, the context will not accept further configuration. At this point, fsmount()
    // should be called to create a mount object.
    //
    let erofs = FsHandle::open("erofs")?; // equivalent to fsopen("erofs")

    // v all these call fsconfig() with various options
    // configure mount options.
    fsconfig_set_flag(erofs.as_fd(), "ro")?;
    fsconfig_set_string(erofs.as_fd(), "source", proc_self_fd(&image))?;
    fsconfig_create(erofs.as_fd())?;


    // Takes the file descriptor returned by fsopen() and creates a mount object for the filesystem root specified there.
    // The attributes of the mount object are set from the mount_attrs parameter. 
    // The attributes specify the propagation and mount restrictions to be applied to accesses through this mount.
    // 
    // The mount object is then attached to a new file descriptor that looks like one created by open(2) with O_PATH or open_tree(2).
    // This can be passed to move_mount(2) to attach the mount object to a mountpoint, thereby completing the process.
    // 
    // The file descriptor returned by fsmount() is marked close-on-exec if FSMOUNT_CLOEXEC is specified in flags.
    // 
    // After fsmount() has completed, the context created by fsopen() is reset and moved to reconfiguration state, allowing the new superblock to be reconfigured. 
    // See fspick(2) for details.
    // 
    // To use either of these calls, the caller requires the appropriate privilege (Linux: the CAP_SYS_ADMIN capability).
    Ok(fsmount(
        erofs.as_fd(),
        FsMountFlags::FSMOUNT_CLOEXEC,
        MountAttrFlags::empty(),
    )?)
}

pub fn composefs_fsmount(image: OwnedFd, name: &str, basedir: impl AsFd, enable_verity: bool) -> Result<OwnedFd> {
    // Prepares a mounted filesystem for further use.  On 6.15 kernels this is a no-op, due to the
    // expanded number of operations which can be performed on "detached" mounts.  On earlier kernels
    // we need to create a temporary directory and mount the filesystem there to avoid failures,
    // making sure to detach the mount and remove the directory later.  This function returns an `impl
    // AsFd` which also implements the `Drop` trait in order to facilitate this cleanup.
    let erofs_mnt = prepare_mount(erofs_mount(image)?)?;

    let overlayfs = FsHandle::open("overlay")?;
    fsconfig_set_string(overlayfs.as_fd(), "source", format!("composefs:{name}"))?;
    fsconfig_set_string(overlayfs.as_fd(), "metacopy", "on")?;
    fsconfig_set_string(overlayfs.as_fd(), "redirect_dir", "on")?;
    if enable_verity {
        fsconfig_set_string(overlayfs.as_fd(), "verity", "require")?;
    }

    /// Sets the "lowerdir+" and "datadir+" mount options of an overlayfs mount to the provided file
    /// descriptors.  On 6.15 kernels this can be done by directly calling `fsconfig_set_fd()`.  On
    /// pre-6.15 kernels, it needs to be done by reopening the file descriptor `O_RDONLY` and calling
    /// `fsconfig_set_fd()` because `O_PATH` fds are rejected.  On very old kernels this needs to be
    /// done by calculating a `"lowerdir=lower::data"` string using `/proc/self/fd/` filenames and
    /// setting it via `fsconfig_set_string()`.
    overlayfs_set_lower_and_data_fds(&overlayfs, &erofs_mnt, Some(&basedir))?;

    let lower_fd = lower.as_fd().as_raw_fd().to_string();
    let arg = if let Some(data) = data {
        let data_fd = data.as_fd().as_raw_fd().to_string();
        format!("/proc/self/fd/{lower_fd}::/proc/self/fd/{data_fd}")
    } else {
        format!("/proc/self/fd/{lower_fd}")
    };
    rustix::mount::fsconfig_set_string(fs_fd.as_fd(), "lowerdir", arg)

    fsconfig_create(overlayfs.as_fd())?;

    Ok(fsmount(
        overlayfs.as_fd(),
        FsMountFlags::FSMOUNT_CLOEXEC,
        MountAttrFlags::empty(),
    )?)
}

// Picks the mount object specified by the pathname and attaches it to a new file descriptor or clones it and attaches the clone to the file descriptor.
// The resultant file descriptor is indistinguishable from one produced by open(2) with O_PATH.
// 
// In the case that the mount object is cloned, the clone will be "unmounted" and destroyed when the file descriptor is closed if it is not 
// otherwise mounted somewhere by calling move_mount(2).
// 
// To select a mount object, no permissions are required on the object referred to by the path, but execute (search)
// permission is required on all of the directories in pathname that lead to the object.

// OpenTreeFlags::AT_EMPTY_PATH
// 
// If pathname is an empty string, operate on the file referred to by dirfd (which may have been obtained from open(2) with
// O_PATH, from fsmount(2) or from another open_tree()).
// 
// If dirfd is AT_FDCWD, the call operates on the current working directory. In this case, dirfd
// can refer to any type of file, not just a directory. This flag is Linux-specific; define _GNU_SOURCE to obtain its definition.

fn bind_mount(fd: impl AsFd, path: &str) -> rustix::io::Result<OwnedFd> {
    open_tree(
        fd.as_fd(),
        path,
        OpenTreeFlags::OPEN_TREE_CLONE
            | OpenTreeFlags::OPEN_TREE_CLOEXEC
            | OpenTreeFlags::AT_EMPTY_PATH,
    )
}
```


02.  Required before Linux 6.15: it's not possible to use detached mounts with `OPEN_TREE_CLONE` or
    `overlayfs`.  

    Convert them into a non-floating form by mounting them on a temporary directory and
    reopening them as an O_PATH fd.


03. Mount `composefs` as an `overlayfs` mount type.

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

// this returns an OwnedFd
let composefs_image = fsmount(
    overlayfs.as_fd(),
    FsMountFlags::FSMOUNT_CLOEXEC,
    MountAttrFlags::empty(),
);
```

After creating our mount, we will detach the old sysroot mount, if it exists

```rust
// empty path "" = detatch the mount
let sysroot_clone = bind_mount(&sysroot, "")?;

// Then we mount our composefs_image at /sysroot
mount_at(&composefs_image, CWD, &args.sysroot)?;

// mount_at body vv
move_mount(
    sysroot_clone.as_fd(),
    "", // see below. This is empty as we only have transient mounts
    CWD.as_fd(),
    args.sysroot,
    MoveMountFlags::MOVE_MOUNT_F_EMPTY_PATH,
)
```

```c
int move_mount(
    int from_dfd, 
    const char *from_pathname,

    // This is the directory that the to_pathname will be relative to.
    // If this is a dirfd to "/sysroot/rootfs", and to_pathname = "thingy", then the mount will be at /sysroot/rootfs/thingy
    int to_dfd,

    // If to_pathname starts with "/" (i.e. it is absolute), then `to_dfd` is ignored
    const char *to_pathname,

    unsigned int flags
);
```


If there was an old sysroot, we move it to /sysroot/sysroot

```rust
mount_at(&sysroot_clone, &composefs_image, "sysroot");
```



add root=UUID=rootpartuuid
add rw to options
move composefs repo to root partition
