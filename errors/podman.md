# Issue with podman build dynamic libs

```bash
$ sudo podman build -t skopeo-unshare-test -f ./Containerfile.skopeo

/bin/sh: error while loading shared libraries: /lib64/libc.so.6: cannot apply additional memory protection after relocation: Permission denied
Error: building at STEP "RUN mkdir /var/repo": while running runtime: exit status 127
```

### Possible Issue 1 - noexec mount

Likely hitting noexec mount restrictions on the layer where the container runtime is unpacking or executing binaries.

Check if `/var/tmp`, `/tmp`, or the storage backend (like overlayfs) is mounted with noexec.

```bash
$ mount | grep noexec

devpts on /dev/pts type devpts (rw,nosuid,noexec,relatime,seclabel,gid=5,mode=620,ptmxmode=000)
sysfs on /sys type sysfs (rw,nosuid,nodev,noexec,relatime,seclabel)
securityfs on /sys/kernel/security type securityfs (rw,nosuid,nodev,noexec,relatime)
cgroup2 on /sys/fs/cgroup type cgroup2 (rw,nosuid,nodev,noexec,relatime,seclabel,nsdelegate,memory_recursiveprot)
pstore on /sys/fs/pstore type pstore (rw,nosuid,nodev,noexec,relatime,seclabel)
efivarfs on /sys/firmware/efi/efivars type efivarfs (rw,nosuid,nodev,noexec,relatime)
bpf on /sys/fs/bpf type bpf (rw,nosuid,nodev,noexec,relatime,mode=700)
configfs on /sys/kernel/config type configfs (rw,nosuid,nodev,noexec,relatime)
proc on /proc type proc (rw,nosuid,nodev,noexec,relatime)
selinuxfs on /sys/fs/selinux type selinuxfs (rw,nosuid,noexec,relatime)
debugfs on /sys/kernel/debug type debugfs (rw,nosuid,nodev,noexec,relatime,seclabel)
tracefs on /sys/kernel/tracing type tracefs (rw,nosuid,nodev,noexec,relatime,seclabel)
mqueue on /dev/mqueue type mqueue (rw,nosuid,nodev,noexec,relatime,seclabel)
tmpfs on /run/credentials/systemd-journald.service type tmpfs (ro,nosuid,nodev,noexec,relatime,nosymfollow,seclabel,size=1024k,nr_inodes=1024,mode=700,inode64,noswap)
fusectl on /sys/fs/fuse/connections type fusectl (rw,nosuid,nodev,noexec,relatime)
tmpfs on /run/credentials/systemd-resolved.service type tmpfs (ro,nosuid,nodev,noexec,relatime,nosymfollow,seclabel,size=1024k,nr_inodes=1024,mode=700,inode64,noswap)


tmpfs on /tmp type tmpfs (rw,noexec,nosuid,nodev) # This breaks dynamic linker behaviour

# Remount tmpfs with exec perms
sudo mount -o remount,exec /tmp
```

### Possible issue 2 - selinux issues

```bash
podman build --security-opt label=disable -t skopeo-unshare-test -f ./Containerfile.skopeo
```

*Rootless Podman* runs in user namespaces and doesn't apply SELinux labels to container processes or files.

*Rootful Podman*, by default, runs containers with the container_t SELinux context and enforces SELinux policy 
which can block mprotect, exec, and other memory operations inside the container.
