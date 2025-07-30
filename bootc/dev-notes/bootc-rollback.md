```sh
# Initially
$ bootc status
● Booted image: quay.io/fedora/fedora-coreos:stable
        Digest: sha256:0d12b8fb8533384a2a06b60146fe3acb27c30e374cd62fee60e32ca6a0773ed1 (amd64)
       Version: 42.20250705.3.0 (2025-07-21T18:56:30Z)

  Rollback image: quay.io/fedora/fedora-coreos:stable
          Digest: sha256:da8486bd1571a7e101dd178eb7826e174de6810389d1f6eb3204278f1942ed53 (amd64)
         Version: 42.20250623.3.1 (2025-07-10T18:50:20Z)


$ bootc rollback
Next boot: rollback deployment
error: Rollback: Updating storage root mtime: update_timestamps: No such file or directory (os error 2)

# After reboot
$ bootc status
● Booted image: quay.io/fedora/fedora-coreos:stable
        Digest: sha256:da8486bd1571a7e101dd178eb7826e174de6810389d1f6eb3204278f1942ed53 (amd64)
       Version: 42.20250623.3.1 (2025-07-10T18:50:20Z)

  Rollback image: quay.io/fedora/fedora-coreos:stable
          Digest: sha256:0d12b8fb8533384a2a06b60146fe3acb27c30e374cd62fee60e32ca6a0773ed1 (amd64)
         Version: 42.20250705.3.0 (2025-07-21T18:56:30Z)


# After another reboot
$ bootc status
● Booted image: quay.io/fedora/fedora-coreos:stable
        Digest: sha256:da8486bd1571a7e101dd178eb7826e174de6810389d1f6eb3204278f1942ed53 (amd64)
       Version: 42.20250623.3.1 (2025-07-10T18:50:20Z)

  Rollback image: quay.io/fedora/fedora-coreos:stable
          Digest: sha256:0d12b8fb8533384a2a06b60146fe3acb27c30e374cd62fee60e32ca6a0773ed1 (amd64)
         Version: 42.20250705.3.0 (2025-07-21T18:56:30Z)


# This is after a switch, reboot and then selecting the old deployment from the boot list
# Notice how rollback now set the CURRENT deployment as the default one as the switched one is the
# actual default
root@fedora-coreos:/var# bootc status
● Booted image: quay.io/fedora/fedora-coreos:stable
        Digest: sha256:da8486bd1571a7e101dd178eb7826e174de6810389d1f6eb3204278f1942ed53 (amd64)
       Version: 42.20250623.3.1 (2025-07-10T18:50:20Z)

  Rollback image: 192.168.122.1:5000/composefs-bls-upgrade
          Digest: sha256:bb2295d89b083cdfdd0a6ede4023daeee0a8a1846377834969089ec6993279f5 (amd64)
         Version: 42.20250505.0 (2025-07-23T13:29:48Z)

$ bootc rollback
notice: Reverting queued rollback state
Next boot: current deployment
```
