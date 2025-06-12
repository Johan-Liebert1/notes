# --privelged

## Grants all Linux capabilities

Without --privileged, containers only get a limited set of capabilities. 
With it, the container gets all capabilities, including:

* CAP_SYS_ADMIN
* CAP_SYS_MODULE
* CAP_MKNOD
* CAP_SYS_RAWIO
* and others

These allow actions like mounting filesystems, managing devices, accessing /sys, etc.

## Disables cgroup limits
It lifts CPU/memory/device/etc. restrictions normally applied via cgroups.

## Mounts host devices
All /dev/* devices from the host are made available inside the container.

## Allows access to kernel filesystems
Things like /sys, /proc, and /dev behave like they do on the host, with fewer restrictions.


# --security-opt

Passing `--security-opt label=type:unconfined_t` works because it disables SELinux confinement for the container.

The default SELinux label for containers (e.g. container_t) restricts access to files outside the container, especially sensitive paths like: 
`/var/lib/containers/storage`

Under SELinux policy, access to this path is denied unless the process has the correct label.


## What label=type:unconfined_t does:

It sets the container process context to unconfined_t, which:

* bypasses SELinux policy enforcement
* gives the process unrestricted access to all files (based on DAC permissions)
