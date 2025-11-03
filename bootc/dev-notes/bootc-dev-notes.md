```bash
curl http://192.168.122.1:8080/bootc -o /var/bootc && chmod +x /var/bootc && alias bootc=/var/bootc

curl http://192.168.122.1:8080/system-reinstall-bootc -o system-reinstall-bootc && chmod +x system-reinstall-bootc

mkdir -p /run/composefs && echo "906b41c625f700095717c8d9b89232f98ac6a40bf2d2e71e1b5434adfbcebf9a" > /run/composefs/staged-deployment
```

```rust
Some(ostree_ext::containers_image_proxy::ImageProxyConfig {
    insecure_skip_tls_verification: Some(true),
    ..Default::default()
})
```


```toml
[patch."https://github.com/containers/composefs-rs"]
composefs = { path = "../composefs-rs/crates/composefs" }
composefs-boot = {  path = "../composefs-rs/crates/composefs-boot"  }
composefs-oci = {  path = "../composefs-rs/crates/composefs-oci"  }
```


```log
Jun 11 05:58:26 fedora kernel: netfs: FS-Cache loaded
Jun 11 05:58:26 fedora kernel: erofs (device erofs): mounted with root inode @ nid 36.
Jun 11 05:58:26 fedora systemd[1]: tmp-.tmpsBXdmL.mount: Deactivated successfully.
Jun 11 05:58:26 fedora systemd[1]: Finished composefs-setup-root.service.
Jun 11 05:58:26 fedora systemd[1]: Reached target initrd-root-fs.target - Initrd Root File System.
Jun 11 05:58:26 fedora systemd[1]: Starting initrd-parse-etc.service - Mountpoints Configured in the Real Root...
Jun 11 05:58:26 fedora (ab-check)[709]: initrd-parse-etc.service: Unable to locate executable '/usr/lib/systemd/systemd-sysroot-fstab-check': No such file or directory
Jun 11 05:58:26 fedora (ab-check)[709]: initrd-parse-etc.service: Failed at step EXEC spawning /usr/lib/systemd/systemd-sysroot-fstab-check: No such file or directory
Jun 11 05:58:26 fedora systemd[1]: initrd-parse-etc.service: Main process exited, code=exited, status=203/EXEC
Jun 11 05:58:26 fedora systemd[1]: initrd-parse-etc.service: Failed with result 'exit-code'.
Jun 11 05:58:26 fedora systemd[1]: Failed to start initrd-parse-etc.service - Mountpoints Configured in the Real Root.
Jun 11 05:58:26 fedora systemd[1]: initrd-parse-etc.service: Triggering OnFailure= dependencies.
```

```bash
192.168.122.137 - non-uki
```

```bash
# image
podman pull quay.io/pragyanpoudyal/bootc-composefs-uki:latest
```


Errors to fix

```log
while doing bootc upgrade 
origin file

[origin]
container-image-reference = ostree-unverified-image:docker://quay.io/pragyanpoudyal/bootc-composefs-bls

DEBUG new_with_config: Spawned skopeo pid=5055 config=ImageProxyConfig { authfile: None, auth_data: None, auth_anonymous: false, certificate_directory: None, decryption_keys: None, insecure_s
kip_tls_verification: None, debug: false, skopeo_cmd: None }
DEBUG new_with_config: Remote protocol version: 0.2.6 config=ImageProxyConfig { authfile: None, auth_data: None, auth_anonymous: false, certificate_directory: None, decryption_keys: None, ins
ecure_skip_tls_verification: None, debug: false, skopeo_cmd: None }
DEBUG open_image: opening image self=ImageProxy imgref="registry:quay.io/pragyanpoudyal/bootc-composefs-bls"
ERROR Upgrading composefs: Pulling composefs repo: Opening image: failed to invoke method OpenImage: Invalid image name "registry:quay.io/pragyanpoudyal/bootc-composefs-bls", unknown transpor
t "registry"
```


TODO:

1. update stage
2. write grub user.cfg as staged while updating

## The WHY of integrating composefs into bootc

ostree sotres things in an object store with the file hash being the file data + file metadata 

so let's say depl1 has bash, and depl2 has bash, both have the same content but have different metdata, then we can't hardlink one file as the metdata are different.
We'll need double the space just because the metdata is different


If say depl-old has a vulnerable sudo and depl-new has a non vuln sudo, we can still access the setuid 0 sudo from depl-old even if depl-new is mounted, as they're hard links.

But with composfs we only store a single file and all the metadata is in Erofs file, you need to be root to mount and use the vuln sudo

