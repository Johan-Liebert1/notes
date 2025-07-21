# When all things are the same but versions are different

```
==> v1.conf <==
version 1

==> v0.conf <==
version 0
```

`version 1` is the one that is the first boot entry shown by grub. 

## Is it mtime?

```bash
# updating mtime for v0
touch v0.conf
```

Still, `version 1` is the first entry


## Is it `version` field?

```
==> v0.conf <==
version 2

==> v1.conf <==
version 1
```

Still, `version 1` shows up first


## Is it the file name?

YES

```
==> v2.conf <==
version 0

==> v1.conf <==
version 1
```

Now `version 0` is at the top because it's got higher file number
