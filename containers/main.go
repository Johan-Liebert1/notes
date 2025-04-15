package main

import (
	"fmt"
	"os"
	"os/exec"
	"syscall"
)

func must(err error) {
	if err != nil {
		panic(err)
	}
}

// go run main.go     run          <command> <args>
// docker             run  <image> <command> <args>
func main() {
	if len(os.Args) < 2 {
		panic("yoo bro too little args")
	}

	// a really convoluted way of doing a fork/exec but I guess better than creating all
	// the namespaces ourselves
	switch os.Args[1] {
	case "run":
		run()

	case "child":
		child()

	default:
		panic("yoo wth bro")
	}
}

func run() {
	fmt.Printf(
        "Function run: Running command %+v as user %d in process %d \n",
		os.Args[2:],
		os.Geteuid(),
		os.Getpid(),
	)

    // we call ourselves but with a different param so that the child() func will run
	cmd := exec.Command("/proc/self/exe", append([]string{"child"}, os.Args[2:]...)...)

	cmd.Stdin = os.Stdin
	cmd.Stdout = os.Stdout
	cmd.Stderr = os.Stderr

	// SysProcAttr holds optional, operating system-specific attributes.
	// Run passes it to os.StartProcess as the os.ProcAttr's Sys field.
	cmd.SysProcAttr = &syscall.SysProcAttr{
		// This doesn't work unless we invoke the parent precess as root
		// Cloneflags: syscall.CLONE_NEWUTS,

		// This will work as we are allowed to create new user namespaces whether we are root or not
		// creating a new UTS namespace still requires root prem, but this call will first create the
		// user namespace and then create the UTS ns
		Cloneflags: syscall.CLONE_NEWUTS |
			syscall.CLONE_NEWUSER |

			// a new mount namespace
			syscall.CLONE_NEWNS |

			// A new pid namespace, but this alone does not work as the container will still have
			// access to the host's /proc dir
			syscall.CLONE_NEWPID,

		UidMappings: []syscall.SysProcIDMap{
			// Map root (uid 0) inside the container, to user with uid 1000 on the host
			// Without this mapping, the default user created in the new user namespace is
			//
			// uid=65534(nobody) gid=65534(nobody) groups=65534(nobody)
			{ContainerID: 0, HostID: 1000, Size: 1},
		},

		// Same as UidMappings but for groups
		GidMappings: []syscall.SysProcIDMap{
			{ContainerID: 0, HostID: 1000, Size: 1},
		},
	}

	must(cmd.Run())
}

func child() {
	fmt.Printf(
        "Function child: Running command %+v as user %d in process %d \n",
		os.Args[2:],
		os.Geteuid(),
		os.Getpid(),
	)

    // This won't actually work unless we put all of dynamically linked libs that sh requires
    // inside here, so ultimately we'll need a tarball of a linux filesystem
    must(syscall.Chroot("/home/pragyan/C"))
    must(syscall.Chdir("/"))

    // (source string, target string, fstype string, flags uintptr, data string)
    // Without this, the kernel doesn't know what to put in /proc inside this new chrooted env
    must(syscall.Mount("proc", "proc", "proc", 0, ""))

    entries, err := os.ReadDir("/")
    must(err)
    fmt.Printf("Dir entries: %+v\n", entries)

    stat, err := os.Stat("/usr/bin/sh")

    if err != nil {
        fmt.Printf("/usr/bin/sh not found\n")
    } else {
        fmt.Printf("Stat: %+v\n", stat)
    }

    cmd := exec.Command(os.Args[2], os.Args[3:]...)
	cmd.Stdin = os.Stdin
	cmd.Stdout = os.Stdout
	cmd.Stderr = os.Stderr

    fmt.Printf("Function child: Running cmd '%s'\n", cmd.String())

    must(cmd.Run())
}
