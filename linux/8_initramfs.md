### Extracting initramfs 


```bash
# Figure out compression
file initramfs.img

# if zstd
zstd -dc initramfs.img | cpio -idmv
```

