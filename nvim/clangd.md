# Stupid clangd won't work. Options to fix

## 1. Make sure there's a .clangd in the root and add absolute paths to the includes

```yaml
CompileFlags:
  Add: 
    - -I/home/pragyan/RedHat/ostree/src/boot
    - -I/home/pragyan/RedHat/ostree/src/libostree
    - -I/home/pragyan/RedHat/ostree/src/libotcore
    - .. and so on
```


## 2. Use system's clangd and not mason's

```lua
if lspName == "clangd" then
    config.settings = {
        cmd = { "/usr/bin/clangd" }
    }
end
```


## 3. pkg-config is a life saver 

```bash
kg-config --cflags gio-2.0
```

## 4. If all else fails, find the thingies

```bash
find /usr/include -name giotypes.h
find /usr/lib64 -name giotypes.h
```
