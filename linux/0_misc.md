## Intentionally panicking the kernel

```bash
# set auto reboot on panic
echo 10 > /proc/sys/kernel/panic

echo 1 > /proc/sys/kernel/sysrq
echo c > /proc/sysrq-trigger

# This will immediately crash the kernel with a NULL pointer dereference and reboot (if kernel.panic=... is set).
```


## Sort files in a dir in descending order of size 

```bash
find . -type f -exec du -b {} + | sort -nr
```
