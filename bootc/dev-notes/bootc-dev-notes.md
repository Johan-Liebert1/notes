+ COMPOSEFS_FSVERITY=f2b8b798d07dfa5a5931a94e1516b028b10f040464e3f339459b03f2ec8f3ed9


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
