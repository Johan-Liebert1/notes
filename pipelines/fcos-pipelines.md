# bump-lockfile

bumps lockfiles in the `fedora-coreos-config` repo by pulling new packages from `rpm` repo and running tests

Bumps all lockfiles, except for any that has `overrides` in it.

It clones the repo, bumps the lockfiles, tests for each and every arch, then pushes to the repo if all tests pass

If it fails, it means some package was updated and now it's causing issues


# build-fcos-buildroot

Runs every 3 days (this might be outdataed), or runs everytime the `buildroot` directory in `fedora-coreos-config` changes


# kola-aws | kola-azure | kola-gcp

they are cloud tests, triggered by `build` job

Runs `kola` on those tests as some tests are cloud specific


# seed

whole config of pipeline is in git, so we don't want to do any custom add job

There is a plugin called `config as code`. Defined in `fedora-coreos-pipeline/jenkins/config`

seed job is defined in `fedora-coreos-pipeline/jenkins/config/seed.yaml` which is basically a `dsl`

at first only the seed job will be there, as seed job is the only job that's defined as the `config as code` plugin

The `seed` job basically then generates then runs all the jobs in  `fedora-coreos-pipeline/jobs`


# koji tagger

Used to tag `rpms` for use in builds, signs the `rpms` and puts them in `coreos-pool`, then puts it in a `yum` repo

It looks for every possible lockfile in all repos, but especially in `fedora-coreos-config` all branches.

`fedora-coreos-config` has a `.repo` file somewhere 

When we do our builds we make sure that the content is in the `coreos-pool`

When we run `bump-lockfile` you can pull the content from the fedora repos, 
but when we run `testing-devel` pipeline build, the content can't come from those repos (now idk why this is).

These (openshift) projects are in `coreos/fedora-coreos-releng-automation`


# The deny list fedora-coreos-config/kola-denylist.yaml

Add a test to this yaml if the failure is not in our control


# ====================================================
# CoreOS CI
# ====================================================


