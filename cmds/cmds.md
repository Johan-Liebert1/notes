# cat files with names

```bash
find . -type f -exec sh -c 'for f; do echo "==> $f <=="; cat "$f"; echo; done' _ {} +
```
