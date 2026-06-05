# change cmdline

```bash
objcopy --dump-section .cmdline=cmdline.txt my.efi

objcopy \
  --update-section .cmdline=cmdline.txt \
  my.efi new.efi
```
