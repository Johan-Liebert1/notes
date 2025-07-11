# Before bootc switch

```ini
# ==> /boot/loader/entries/ostree-1.conf <==
title Fedora Linux 42 (Adams) (ostree:1)
version 1
options rw $ignition_firstboot mitigations=auto,nosmt ostree=/ostree/boot.1/fedora-coreos/126b00a51488ea02ebc861dd33d413eb58f3287fd75646e8d215e46d88f81197/0 ignition.platform.id=qemu console= tty0 console=ttyS0,115200n8 root=UUID=34bfd606-f2cd-43f9-9b54-9e62aec79722 rw rootflags=prjquota boot=UUID=a0bed1a7-d1b0-4674-8117-713b2f1bff75 
linux /boot/ostree/fedora-coreos-126b00a51488ea02ebc861dd33d413eb58f3287fd75646e8d215e46d88f81197/vmlinuz-6.15.4-200.fc42.x86_64
initrd /boot/ostree/fedora-coreos-126b00a51488ea02ebc861dd33d413eb58f3287fd75646e8d215e46d88f81197/initramfs-6.15.4-200.fc42.x86_64.img
abootcfg /ostree/deploy/fedora-coreos/deploy/618524839cc27cecf195eac774641e64588b24c9bc65e2af4876fa88918a7413.0/usr/lib/ostree-boot/aboot.cfg
grub_users ""
aboot /ostree/deploy/fedora-coreos/deploy/618524839cc27cecf195eac774641e64588b24c9bc65e2af4876fa88918a7413.0/usr/lib/ostree-boot/aboot.img

# ==> /boot/loader/entries/ostree-2.conf <==
title Fedora CoreOS 42.20250708.dev.0 (ostree:0)
version 2
options rw $ignition_firstboot mitigations=auto,nosmt ostree=/ostree/boot.1/fedora-coreos/bfd59dfe9e52370fb748b959dc2ad0f1eb35b73054ced8d00bfa38065d131616/0 ignition.platform.id=qemu console= tty0 console=ttyS0,115200n8 root=UUID=34bfd606-f2cd-43f9-9b54-9e62aec79722 rw rootflags=prjquota boot=UUID=a0bed1a7-d1b0-4674-8117-713b2f1bff75
linux /boot/ostree/fedora-coreos-bfd59dfe9e52370fb748b959dc2ad0f1eb35b73054ced8d00bfa38065d131616/vmlinuz-6.14.9-300.fc42.x86_64
initrd /boot/ostree/fedora-coreos-bfd59dfe9e52370fb748b959dc2ad0f1eb35b73054ced8d00bfa38065d131616/initramfs-6.14.9-300.fc42.x86_64.img
abootcfg /ostree/deploy/fedora-coreos/deploy/5e6cc9beb75a9b4d1ff7f10b212dad93075e3b25edc7f094ccaf38802efd3cef.0/usr/lib/ostree-boot/aboot.cfg
aboot /ostree/deploy/fedora-coreos/deploy/5e6cc9beb75a9b4d1ff7f10b212dad93075e3b25edc7f094ccaf38802efd3cef.0/usr/lib/ostree-boot/aboot.img
grub_users ""
```

# After boot switch

```bash
bootc switch quay.io/fedora/fedora-bootc:43

Queued for next boot: quay.io/fedora/fedora-bootc:43
  Version: 43.20250710.0
  Digest: sha256:952d34bc42885c26c4a40df9d53d3f2f6b102a7a2799ba7741007d29665e7387

# check status
bootc status

  Staged image: quay.io/fedora/fedora-bootc:43
        Digest: sha256:952d34bc42885c26c4a40df9d53d3f2f6b102a7a2799ba7741007d29665e7387 (amd64)
       Version: 43.20250710.0 (2025-07-10T10:05:14Z)

● Booted image: quay.io/fedora/fedora-coreos:testing-devel
        Digest: sha256:ce5e7f01b97bef72ac918196da11a961ccc9e8f28ee432d2e594cdcaf71e4903 (amd64)
       Version: 42.20250708.dev.0 (2025-07-08T05:23:09Z)

  Rollback image: quay.io/fedora/fedora-bootc:42
          Digest: sha256:4c8ce6ab4716274cd7c0e5ad3979223d810bd42f3ea52f005623a240d8969913 (amd64)
         Version: 42.20250707.0 (2025-07-07T11:06:05Z)
```



```ini
# ==> /boot/loader/entries/ostree-1.conf <==
title Fedora Linux 42 (Adams) (ostree:1)
version 1
options rw $ignition_firstboot mitigations=auto,nosmt ostree=/ostree/boot.1/fedora-coreos/126b00a51488ea02ebc861dd33d413eb58f3287fd75646e8d215e46d88f81197/0 ignition.platform.id=qemu console=
tty0 console=ttyS0,115200n8 root=UUID=34bfd606-f2cd-43f9-9b54-9e62aec79722 rw rootflags=prjquota boot=UUID=a0bed1a7-d1b0-4674-8117-713b2f1bff75
linux /boot/ostree/fedora-coreos-126b00a51488ea02ebc861dd33d413eb58f3287fd75646e8d215e46d88f81197/vmlinuz-6.15.4-200.fc42.x86_64
initrd /boot/ostree/fedora-coreos-126b00a51488ea02ebc861dd33d413eb58f3287fd75646e8d215e46d88f81197/initramfs-6.15.4-200.fc42.x86_64.img
abootcfg /ostree/deploy/fedora-coreos/deploy/618524839cc27cecf195eac774641e64588b24c9bc65e2af4876fa88918a7413.0/usr/lib/ostree-boot/aboot.cfg
grub_users ""
aboot /ostree/deploy/fedora-coreos/deploy/618524839cc27cecf195eac774641e64588b24c9bc65e2af4876fa88918a7413.0/usr/lib/ostree-boot/aboot.img

# ==> /boot/loader/entries/ostree-2.conf <==
title Fedora CoreOS 42.20250708.dev.0 (ostree:0)
version 2
options rw $ignition_firstboot mitigations=auto,nosmt ostree=/ostree/boot.1/fedora-coreos/bfd59dfe9e52370fb748b959dc2ad0f1eb35b73054ced8d00bfa38065d131616/0 ignition.platform.id=qemu console=
tty0 console=ttyS0,115200n8 root=UUID=34bfd606-f2cd-43f9-9b54-9e62aec79722 rw rootflags=prjquota boot=UUID=a0bed1a7-d1b0-4674-8117-713b2f1bff75
linux /boot/ostree/fedora-coreos-bfd59dfe9e52370fb748b959dc2ad0f1eb35b73054ced8d00bfa38065d131616/vmlinuz-6.14.9-300.fc42.x86_64
initrd /boot/ostree/fedora-coreos-bfd59dfe9e52370fb748b959dc2ad0f1eb35b73054ced8d00bfa38065d131616/initramfs-6.14.9-300.fc42.x86_64.img
abootcfg /ostree/deploy/fedora-coreos/deploy/5e6cc9beb75a9b4d1ff7f10b212dad93075e3b25edc7f094ccaf38802efd3cef.0/usr/lib/ostree-boot/aboot.cfg
aboot /ostree/deploy/fedora-coreos/deploy/5e6cc9beb75a9b4d1ff7f10b212dad93075e3b25edc7f094ccaf38802efd3cef.0/usr/lib/ostree-boot/aboot.img
grub_users ""
```


















