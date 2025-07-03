# 1. Edit the VM metadata

```bash
virsh edit <vm-name>
```

```xml
<metadata>
  <libosinfo:libosinfo xmlns:libosinfo="http://libosinfo.org/xmlns/libvirt/domain/1.0">
    <libosinfo:hostname>desired-hostname</libosinfo:hostname>
  </libosinfo:libosinfo>
</metadata>
```

# 2. Edit hostname in the VM

```bash
# In the VM (this whole thing is optional)

hostnamectl set-hostname desired-hostname

echo desired-hostname > /etc/hostname

# optional (obviously)
echo "127.0.0.1  desired-hostname" >> /etc/hosts
```

# 3. Add it to host's /etc/hosts for DNS resolution

```bash
# In the host

echo "192.168.vm.ip desired-hostname" | sudo tee -a /etc/hosts
```
