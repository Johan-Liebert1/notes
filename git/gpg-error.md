# Error

error: gpg failed to sign the data:
gpg: Note: database_open 134217901 waiting for lock (held by 13395) ...
gpg: Note: database_open 134217901 waiting for lock (held by 13395) ...
gpg: Note: database_open 134217901 waiting for lock (held by 13395) ...
gpg: Note: database_open 134217901 waiting for lock (held by 13395) ...
gpg: Note: database_open 134217901 waiting for lock (held by 13395) ...
gpg: keydb_search failed: Connection timed out
gpg: skipped "CA5FA172E4153FFE": Connection timed out
[GNUPG:] INV_SGNR 0 CA5FA172E4153FFE
[GNUPG:] FAILURE sign 134250628
gpg: signing failed: Connection timed out

```bash
rm -f ~/.gnupg/*.lock
rm -f ~/.gnupg/public-keys.d/pubring.db.lock
rm -f ~/.gnupg/crls.d/*.lock

# Restart gpg agent
gpgconf --kill all
gpgconf --launch gpg-agent
```
