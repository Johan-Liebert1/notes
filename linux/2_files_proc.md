# /proc

- /proc/mounts has all the mount information for the process.

## /proc/<pid>  

- has all information about a particular process.
- `cmdline` has the process command
- `exe` has the binary that runs

## ====================================== /proc/<pid>/ns ======================================

- Has all namespace information about this process

```bash
lrwxrwxrwx 1 root root 0 Dec 21 09:09 cgroup -> 'cgroup:[4026531835]'
lrwxrwxrwx 1 root root 0 Dec 21 15:04 ipc -> 'ipc:[4026531839]'
lrwxrwxrwx 1 root root 0 Dec 21 15:04 mnt -> 'mnt:[4026531841]'
lrwxrwxrwx 1 root root 0 Dec 21 15:04 net -> 'net:[4026531840]'
lrwxrwxrwx 1 root root 0 Dec 21 15:04 pid -> 'pid:[4026531836]'
lrwxrwxrwx 1 root root 0 Dec 21 15:04 pid_for_children -> 'pid:[4026531836]'
lrwxrwxrwx 1 root root 0 Dec 21 15:04 time -> 'time:[4026531834]'
lrwxrwxrwx 1 root root 0 Dec 21 15:04 time_for_children -> 'time:[4026531834]'
lrwxrwxrwx 1 root root 0 Dec 21 15:04 user -> 'user:[4026531837]'
lrwxrwxrwx 1 root root 0 Dec 21 15:04 uts -> 'uts:[4026531838]'
```


## ====================================== /proc/<pid>/status  ======================================

- Has all stats about the process

```bash
Name:   systemd
Umask:  0000
State:  S (sleeping)
Tgid:   1
Ngid:   0
Pid:    1
PPid:   0
TracerPid:      0
Uid:    0       0       0       0
Gid:    0       0       0       0
FDSize: 512
Groups:  
NStgid: 1
NSpid:  1 # namespaced pid if any will be here
NSpgid: 1
NSsid:  1
Kthread:        0
VmPeak:    30248 kB
VmSize:    21832 kB
VmLck:         0 kB
VmPin:         0 kB
VmHWM:     19988 kB
VmRSS:     12848 kB
...
```

## ====================================== /proc/<pid>/fd ======================================

- Contains all the files opened by the process as symlinks

```bash
lr-x------  0 -> /dev/null
lrwx------  1 -> 'socket:[21994]'
lr-x------  10 -> /usr/lib/brave-browser/resources.pak
lr-x------  11 -> /usr/lib/brave-browser/brave_resources.pak
lr-x------  12 -> /usr/lib/brave-browser/brave_100_percent.pak
lr-x------  13 -> /usr/lib/brave-browser/brave_200_percent.pak
lr-x------  14 -> /dev/urandom
lr-x------  15 -> /dev/urandom
lrwx------  16 -> 'anon_inode:[eventfd]'
lrwx------  17 -> 'anon_inode:[eventpoll]'
lrwx------  18 -> 'socket:[463356]'
lrwx------  19 -> 'socket:[28968]'
lrwx------  2 -> 'socket:[21994]'
lr-x------  20 -> /usr/lib/brave-browser/v8_context_snapshot.bin
lrwx------  21 -> 'anon_inode:[eventfd]'
lrwx------  22 -> 'socket:[469276]'
lr-x------  25 -> /home/pragyan/.config/BraveSoftware/Brave-Browser/Dictionaries/en-GB-10-1.bdic
lrwx------  3 -> 'anon_inode:[eventpoll]'
lr-x------  37 -> /proc/17809/statm
lr-x------  38 -> /proc/17809/status
lrwx------  39 -> '/tmp/.org.chromium.Chromium.F0SZQR (deleted)'
lrwx------  4 -> 'socket:[28973]'
lrwx------  40 -> 'socket:[461508]'
lr-x------  5 -> /usr/lib/brave-browser/icudtl.dat
lr-x------  6 -> /usr/lib/brave-browser/v8_context_snapshot.bin
lr-x------  7 -> /usr/lib/brave-browser/chrome_100_percent.pak
lr-x------  8 -> /usr/lib/brave-browser/chrome_200_percent.pak
lr-x------  9 -> /usr/lib/brave-browser/locales/en-GB.pak
```

## ====================================== /proc/net/* ======================================

In the above example, we see

```bash
lrwx------  19 -> 'socket:[28968]'
```

we can check `/proc/net/tcp`, `/proc/net/tcp6`, `/proc/net/udp`, `/proc/net/udp6`, `/proc/net/unix` to figure out what type of socket this is

## ====================================== /proc/<pid>/tasks ======================================

- Contains a directory for each thread of the process identified by <pid>. 
- Each thread's directory is named with its thread ID (tid), which is unique within the process.

## ====================================== /proc/<pid>/tasks/<pid>/children ======================================

- Contains all the child processes

## ===================================== /proc/<pid>/cpuset ======================================

- The file typically contains a relative path (e.g., / or /my_cgroup) indicating the cpuset cgroup assigned to the process.

Example, cpuset of pid 1

```bash
$ cat /proc/1/cpuset

/
```

cpuset for a process running inside a container with cgroups applied

```bash
$ cat /proc/24706/cpuset

/kubepods.slice/kubepods-burstable.slice/kubepods-burstable-pod2143011f_695c_49ef_a0ec_1ed4a02bec7a.slice/cri-containerd-2407514d0db7fafa2cda0bb5e2a428917acab96b66f64b5ce30c397ba956ac53.scope
```

# ========================================================= Namespace Switching ====================================

1. Get contanier id and pod id, then get the cgroup dir

```bash
    USER_APP_CONTAINER_ID=$(get_container_id) 
    USER_APP_CONTAINER_CPU_CGROUP=$(printf "/kubepods.slice/kubepods-burstable.slice/kubepods-burstable-pod%s.slice/cri-containerd-%s.scope" "$POD_UID" "$USER_APP_CONTAINER_ID") 
```

2. Inside the cgoup dir there is a file `cgroup.procs` which has all the process ids (in the HOST PID namespace) to which this cgroup should be applied to.
3. If we view the `cgroup.procs` file from within a PID namespace, then processes are running inside a container or a PID namespace, 
the PIDs in cgroup.procs may appear relative to that namespace.

4. So now we have the app-container's parent process PID in the PID namespace. Let's say this value is 7.

5. Now we find, in the /proc directory, the string "NSPid.*[[space]]". NSPid line is of the form "NSPid <PID in host PID ns> <PID in another PID ns>"

6. We find the actual process id in the host namespace. We could get multiple results as muliple namespaces can have the same PID `7` associated. 

7. Now we do `cat /proc/<pid in host ns>/cpuset` and we compare this with our original cpu cgroup value. If they match, this is our process.



