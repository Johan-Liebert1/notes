# ======================================================== UEFI Firmware Initialization ========================================================

When a modern computer is powered on, the UEFI firmware (Unified Extensible Firmware Interface) is the first thing that runs.

It performs POST (Power-On Self-Test), initializes the CPU, memory, and essential peripherals,
and then searches for a bootable device by scanning the EFI System Partition (ESP) on connected drives.

The ESP is a special partition with a FAT32 filesystem, and the firmware looks for EFI binaries (with .efi extension)
at standardized paths (like `EFI/BOOT/BOOTX64.EFI` or `EFI/<vendor>/grubx64.efi`).

In Linux systems, this ESP is usually mounted at `/boot/efi`. So the firmware reads files from `/boot/efi/EFI/<distro>/`. These include:

`grubx64.efi` – The GRUB bootloader binary compiled for UEFI systems.

`shimx64.efi` – Used with Secure Boot, it acts as a first-stage loader that validates GRUB's signature.

The firmware reads the UEFI boot entries (stored in NVRAM) to identify which EFI binary to run. 
These entries are created using efibootmgr or set during installation.

How `EFI/<vendor>/grubx64.efi` Works
UEFI firmware contains a boot manager that reads from the EFI System Partition (ESP)—a FAT32 partition usually mounted at `/boot/efi`.

When a Linux distro like Manjaro is installed, it does not modify the firmware. Instead, it:

Creates or uses an existing ESP.

Copies bootloader binaries into directories on the ESP, like:

`/boot/efi/EFI/Manjaro/grubx64.efi`
`/boot/efi/EFI/BOOT/BOOTX64.EFI` (optional fallback)

Registers a UEFI boot entry in the motherboard's NVRAM using `efibootmgr`.

## Firmware (UEFI) simply:

Scans NVRAM for boot entries (like: "Boot0001 Manjaro").

Each entry points to a specific .efi file on the ESP, e.g.:

\EFI\Manjaro\grubx64.efi

The firmware loads that file—it doesn't care what's in it. It just executes it as a PE32+ binary.

The firmware does not contain hardcoded knowledge of Manjaro, Fedora, etc. It only follows:

NVRAM boot entries (set by OS installers or manually via efibootmgr)

Or, if no entries are present, it tries fallback paths like \EFI\BOOT\BOOTX64.EFI.

# ======================================================== Bootloader Execution (GRUB or Direct EFI Stub Boot)  ========================================================
Once the appropriate .efi binary is located, the UEFI firmware loads it into memory and executes it. At this point, one of two things happens depending on your setup:

A. GRUB is used:
The firmware runs grubx64.efi, which is the UEFI version of the GRUB bootloader. 
This binary loads GRUB's configuration file grub.cfg. 
This file contains boot menu entries, timeout values, and kernel parameters.
It is typically located at `/boot/grub/grub.cfg`, though some setups place it in `/boot/efi/EFI/<distro>/grub.cfg`.

B. Direct EFI Stub Boot (no GRUB):
The firmware directly launches the Linux kernel's EFI stub from a UEFI boot entry.
The kernel image itself (`vmlinuz-<version>`) is a PE executable that the UEFI firmware can load directly.
Boot parameters and initramfs can also be specified in the boot entry. This method bypasses GRUB entirely.

In both cases, the kernel and initramfs are found in the /boot directory:

`/boot/vmlinuz-<version>` – This is the compressed kernel image.

`/boot/initrd.img-<version>` or `/boot/initramfs-<version>.img` – This is the initial RAM filesystem (initramfs) used by the kernel during early boot.

If GRUB is used, it explicitly reads these files as defined in grub.cfg.

# ======================================================== 3. GRUB Stage (When Used) ========================================================
When GRUB is launched, it operates in two stages:

GRUB core is loaded (built into grubx64.efi) and initializes the basic environment, console, and modules.

It then reads the GRUB config file (grub.cfg) to display the boot menu and determine which kernel/initramfs to load.

The grub.cfg file contains menu entries like:

```sh
menuentry 'Ubuntu' {
  linux /vmlinuz-5.15.0-91-generic root=UUID=... ro quiet splash
  initrd /initrd.img-5.15.0-91-generic
}
```

These lines tell GRUB to load the specified kernel and initrd image from `/boot`.
GRUB loads these files into memory and passes control to the Linux kernel, along with any specified kernel command-line arguments (e.g., root=, quiet, splash).

Note that GRUB also dynamically loads its modules (like ext2, normal, linux) from /boot/grub/ during this stage, which allows it to read filesystems and present a menu.

# ======================================================== 4. Kernel Execution Begins ========================================================
Once GRUB loads the kernel and initramfs into memory and passes control to the kernel entry point, the kernel decompresses itself and begins execution.
It sets up the CPU, memory management units (MMU), early console output, and parses the command-line parameters passed to it.

At this point, the kernel does not yet mount the real root filesystem.
Instead, it uses the initramfs, which is an archive that acts as a temporary root filesystem, to perform early system setup.
This helps in handling device initialization before the real root device is available (e.g., LVM, RAID, encrypted partitions).

The kernel mounts this initramfs as / and executes its /init script (or binary).

# ======================================================== 5. Initramfs (Early Userspace Execution) ======================================================== 
The initramfs image loaded earlier (`/boot/initrd.img-<version>` or `boot/initramfs-<version>.img`) is typically a gzipped or xz-compressed cpio archive.
It contains a minimal Linux userspace with the necessary tools and scripts to initialize the system.

Inside this early userspace:

Device drivers (like storage, USB, RAID, or encryption modules) are loaded via modprobe.

Any necessary setup scripts (e.g., for LUKS decryption or LVM activation) are run.

It detects and mounts the real root filesystem (based on the root= parameter in the kernel command line).

Once the real root is available, the initramfs executes switch_root or pivot_root, 
which replaces the temporary root with the actual system root (usually `/dev/sda2`, `/dev/nvme0n1p2`, etc.).

After this switch, control is passed to the system's init system.


# ======================================================== 6. System Init (systemd or init) ======================================================== 
With the real root filesystem now mounted, the system's primary init process is started.
On modern systems, this is usually systemd, located at /sbin/init or /lib/systemd/systemd.

From here:

systemd parses its configuration (/etc/systemd/) and starts services according to the default target (usually graphical.target or multi-user.target).

All standard boot processes (mounting filesystems, networking, login managers, etc.) now begin.

From this point on, /boot is just a regular directory unless a kernel upgrade occurs.

