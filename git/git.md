## Aliases

```sh
git config --global alias.<name> "<value>"
```

```toml
[alias]
    name = value
```


## git grep

```sh
# will search for 'some string' across all commits
git grep 'some string'

# use `-P` for regex
git grep -P '[Cc]opyright\s\d+'

# Get line number and file names
git grep -P --line '[Cc]opyright\s\d+'
```


## Reflog

```sh
# Gives you a list of all changes that happened in the git repo
git reflog --date=iso 

df34537 HEAD@{2024-12-22 00:11:44 +0530}: commit: Thingy
36fc01f HEAD@{2024-12-21 13:24:33 +0530}: pull: Fast-forward
a3e2ff6 HEAD@{2024-12-18 00:15:38 +0530}: commit: More notes
7c3f65b HEAD@{2024-11-20 10:47:21 +0530}: commit: ++
d982054 HEAD@{2024-11-19 23:20:48 +0530}: pull: Fast-forward
331e0e2 HEAD@{2024-11-19 00:15:19 +0530}: commit: idk
12f4535 HEAD@{2024-11-05 20:57:36 +0530}: commit: More
09b819a HEAD@{2024-11-01 14:01:37 +0530}: commit: NQueens
03ef733 HEAD@{2024-10-31 16:40:05 +0530}: commit (merge): Merge remote-tracking branch 'origin/thingy'
e03c1be HEAD@{2024-10-31 16:39:26 +0530}: commit: bruh
afba90b HEAD@{2024-10-21 00:41:47 +0530}: commit: Heap
ab2d9a9 HEAD@{2024-10-21 00:13:26 +0530}: commit (amend): Buncha more stuff
910eb5b HEAD@{2024-10-21 00:12:53 +0530}: commit: Buncha more stuff
e77cb7b HEAD@{2024-10-06 13:01:17 +0530}: commit: More
2c53cab HEAD@{2024-10-02 22:20:16 +0530}: commit: More
917ce2f HEAD@{2024-09-29 15:48:02 +0530}: commit: Graphs
018846a HEAD@{2024-09-28 22:32:15 +0530}: commit: Edit dist
be15609 HEAD@{2024-09-26 23:49:38 +0530}: commit: Some trees
4de82c2 HEAD@{2024-09-26 21:47:01 +0530}: commit: More
3887ac1 HEAD@{2024-09-24 19:47:38 +0530}: commit: More
88dba4d HEAD@{2024-09-15 14:32:09 +0530}: commit: Notes
```

Get all info 

```sh
git reflog --date=iso --pretty

commit d31d0be (HEAD -> master)
Reflog: HEAD@{2025-03-31 18:05:53 +0530} (Johan-Liebert1 <email>)
Reflog message: commit: Move around a lot of files
Author: Johan-Liebert1 <email>
Date:   2025-03-31 18:05:53 +0530

    Move around a lot of files

commit 902b428 (origin/master, origin/HEAD)
Reflog: HEAD@{2025-03-16 13:49:14 +0530} (Johan-Liebert1 <email>)
Reflog message: pull --rebase (finish): returning to refs/heads/master
Author: Johan-Liebert1 <email>
Date:   2025-01-17 13:56:35 +0530

    NS switch
```


## Diff

```sh
git diff

-1. Create a cgroup
+
+1. Create a c group


git diff --word-diff

1. Create a [-cgroup-]{+c group+}

```



