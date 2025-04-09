Used to limit process resources


## How to limit a processes memory (cgroupv2)


1. Create a c group

```sh
sudo touch /sys/fs/cgroup/oomdemo
```

2. Set the maximum allowed memory to 10 MB

```sh
# limit physical memory
echo 10485760 | sudo tee /sys/fs/cgroup/oomdemo/memory.max
# limit swap memory
echo 10485760 | sudo tee /sys/fs/cgroup/oomdemo/memory.swap.max
```

3. Get the process pid, and add it to `cgroup.procs`

```sh
echo <bad_pid> | sudo tee /sys/fs/cgroup/oomdemo/cgroup.procs
```
