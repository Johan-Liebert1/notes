# QEMU / COSA Networking Issue Summary

## Symptoms

Inside the VM:

```bash
ping 10.0.2.2
```

worked.

```bash
ping 1.1.1.1
```

worked.

But:

```bash
ping google.com
curl https://example.com
```

failed with DNS resolution errors.

---

# Diagnosis

## VM Networking Was Functional

Verified:

- NIC working
- DHCP working
- routing working
- outbound NAT working

Inside VM:

```bash
ip route
```

showed:

```text
default via 10.0.2.2 dev eth0
```

---

## DNS Was Broken

Inside VM:

```bash
cat /etc/resolv.conf
```

showed:

```text
nameserver 10.0.2.3
```

`10.0.2.3` is QEMU slirp’s built-in DNS proxy.

The DNS proxy was failing.

---

# Host Resolver Investigation

Host:

```bash
resolvectl status
```

showed:

```text
Global DNS Server: 127.0.0.1
DNS Servers: 127.0.0.1
```

while the Wi-Fi interface had:

```text
Current DNS Server: 1.1.1.1
```

This meant:

- systemd-resolved was using a localhost/stub resolver globally
- QEMU slirp DNS forwarding could not properly use the local resolver
- VM DNS requests forwarded to `10.0.2.3` failed

---

# Temporary Fix Attempt

Modified:

## `/etc/systemd/resolved.conf`

```ini
[Resolve]
DNS=1.1.1.1 8.8.8.8
DNSStubListener=no
```

Replaced:

```bash
/etc/resolv.conf
```

symlink with:

```bash
/run/systemd/resolve/resolv.conf
```

Restarted:

```bash
sudo systemctl restart systemd-resolved
```

This fixed VM DNS resolution.

---

# Problem With Temporary Fix

VPN configuration stopped working correctly because VPN depended on the normal systemd-resolved stub resolver.

---

# Final Host Resolver Restoration

Restored normal systemd-resolved behavior.

## `/etc/systemd/resolved.conf`

```ini
[Resolve]
DNSStubListener=yes
```

Restored `/etc/resolv.conf`:

```bash
sudo rm -f /etc/resolv.conf
sudo ln -s /run/systemd/resolve/stub-resolv.conf /etc/resolv.conf
```

Restarted:

```bash
sudo systemctl restart systemd-resolved
```

Final host resolver state:

```text
nameserver 127.0.0.53
```

---

# Recommended Permanent Fix

Do NOT modify the host resolver globally.

Instead, explicitly configure DNS in QEMU/COSA user networking.

Use QEMU arguments such as:

```text
-netdev user,id=eth0,dns=1.1.1.1
```

or:

```text
-nic user,model=virtio-net-pci,dns=1.1.1.1
```

This bypasses the broken interaction between:

- QEMU slirp DNS proxy
- systemd-resolved localhost stub resolver
- VPN-managed DNS setup

and fixes VM DNS permanently without affecting the host VPN configuration.

---

# Files Involved

## `/etc/systemd/resolved.conf`

Temporary modified state:

```ini
[Resolve]
DNS=1.1.1.1 8.8.8.8
DNSStubListener=no
```

Final restored state:

```ini
[Resolve]
DNSStubListener=yes
```

---

## `/etc/resolv.conf`

Temporary symlink:

```text
/run/systemd/resolve/resolv.conf
```

Final restored symlink:

```text
/run/systemd/resolve/stub-resolv.conf
```

Final expected content:

```text
nameserver 127.0.0.53
```

---

# Important Commands Used

## VM Tests

```bash
ping 10.0.2.2
ping 1.1.1.1
ping google.com
curl https://example.com
ip route
cat /etc/resolv.conf
```

---

## Host Resolver Investigation

```bash
resolvectl status
cat /etc/resolv.conf
```

---

## Resolver Reconfiguration

```bash
sudo systemctl restart systemd-resolved
sudo rm -f /etc/resolv.conf
sudo ln -s ...
```
