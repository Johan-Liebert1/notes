 # libvirtd

libvirt keeps its files at /var/lib/libvirt/. There are multiple directories within.

```sh
drwxr-xr-x  2 root   root 4096 Apr  4 05:05 boot
drwxr-xr-x  2 root   root 4096 May  6 16:16 dnsmasq
drwxr-xr-x  2 root   root 4096 Apr  4 05:05 filesystems
drwxr-xr-x  2 root   root 4096 May  6 10:52 images
drwxr-xr-x  3 root   root 4096 May  6 09:55 lockd
drwxr-xr-x  2 root   root 4096 Apr  4 05:05 lxc
drwxr-xr-x  2 root   root 4096 Apr  4 05:05 network
drwxr-xr-x 11 nobody kvm  4096 May  6 16:16 qemu
drwxr-xr-x  2 root   root 4096 Apr  4 05:05 swtpm
```

# Permissions

qemu has primarily two types of URIs

- qemu:///system    -> This is basically root mode
- qemu:///session   -> This is more secure rootless mode


`virsh` by default uses the `qemu:///session`, and `virt-manager` uses `qemu:///system`

virsh, will use `qemu:///session` by default, which means CLI calls not run as sudo will be looking at a different user.
To ensure all client utilities default to `qemu:///system`, add the following configuration to your `.config` directory.

```sh
sudo cp -rv /etc/libvirt/libvirt.conf ~/.config/libvirt/
sudo chown ${YOURUSER}:${YOURGROUP} ~/.config/libvirt/libvirt.conf
```

# Create a VM using CLI

```sh
virt-install \
  --name ubuntu1804 \
  --ram 2048 \
  --disk path=/var/lib/libvirt/images/u19.qcow2,size=8 \
  --vcpus 2 \
  --os-type linux \
  --os-variant generic \
  --console pty,target_type=serial \
  --cdrom /var/lib/libvirt/isos/ubuntu-18.04.4-live-server-amd64.iso # if we we're using an ISO
```




