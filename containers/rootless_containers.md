# Running a DOCKER container

```sh
docker run -it --rm alpine

# inside the container
$ id
uid=0(root) gid=0(root) groups=0(root),1(bin),2(daemon),3(sys),4(adm),6(disk),10(wheel),11(floppy),20(dialout),26(tape),27(video)
```

Now, let's run a sleep process inside the container and check from the host

```sh
# in the container
$ sleep 4000


# in the host
root       10874  0.0  0.0   1588   616 pts/0    S+   20:35   0:00 sleep 4000 # this is running as root from the host's perspective
```

### NOTE: The above behaviour is by default in docker.
- We can change it by either providing a `--user` param to `docker` cmd invocation 
- Or, we can have a `USER` in the Dockerfile




