Since we can't connect via USB anymore cause fuck google

- Get `adb` tools
- Enable dev opts on android device

```shell
# search for 
$ adb devices

List of devices attached
HA1V478Y        device


$ adb shell ls storage

3361-3432
emulated
sdcard0
self

# the actual copy
$ adb push ./Link\ Click\ III/ /storage/3361-3432/

# 3361-3432 is the sdcard and not sdcard0 because fucking andoird


# Copy only contents of a directory

$ adb push ~/Anime/Monster/. /storage/3361-3432/Monster/
```
