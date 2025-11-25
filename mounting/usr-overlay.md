# usr overlay

```bash
mkdir -p /tmp/usr/{upper,work}

mount -t overlay overlay -o lowerdir=/usr,upperdir=/tmp/usr/upper,workdir=/tmp/usr/work /usr
```
