# cat files with names

```bash
find . -maxdepth 1 -type f -exec sh -c 'for f; do echo "==> $f <=="; cat "$f"; echo; done' _ {} +
```
