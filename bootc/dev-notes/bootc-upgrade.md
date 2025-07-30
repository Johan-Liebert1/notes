```bash
# Initial
$ bootc status
● Booted image: quay.io/fedora/fedora-coreos:stable
        Digest: sha256:da8486bd1571a7e101dd178eb7826e174de6810389d1f6eb3204278f1942ed53 (amd64)
       Version: 42.20250623.3.1 (2025-07-10T18:50:20Z)

  Rollback image: quay.io/fedora/fedora-coreos:stable
          Digest: sha256:906ee44ef3c21ee25c856d7c6964cba89595ff03d6454eb89b83bc7c36c2aa2b (amd64)
         Version: 42.20250609.3.0 (2025-06-23T19:16:31Z)


# Switch to a different image. This should hopefully be the same as upgrade/switch both create a 
# staged deployment
$ bootc switch 192.168.122.1:5000/composefs-bls-upgrade

# After switch
$ bootc status
root@fedora-coreos:/var/home/core# bootc status
  Staged image: 192.168.122.1:5000/composefs-bls-upgrade
        Digest: sha256:bb2295d89b083cdfdd0a6ede4023daeee0a8a1846377834969089ec6993279f5 (amd64)
       Version: 42.20250505.0 (2025-07-23T13:29:48Z)

● Booted image: quay.io/fedora/fedora-coreos:stable
        Digest: sha256:da8486bd1571a7e101dd178eb7826e174de6810389d1f6eb3204278f1942ed53 (amd64)
       Version: 42.20250623.3.1 (2025-07-10T18:50:20Z)
```
