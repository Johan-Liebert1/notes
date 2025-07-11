# Flow

```rust
/// Implementation of the `bootc switch` CLI command.
#[context("Switching")]
async fn switch(opts: SwitchOpts) -> Result<()> {
    let target = imgref_for_switch(&opts)?;
    let sysroot = &get_storage().await?;

}

async fn get_storage() -> Result<Storage> {
    let global_run = Dir::open_ambient_dir("/run", cap_std::ambient_authority())?;
    let sysroot = get_locked_sysroot().await?;
    crate::store::Storage::new(sysroot, &global_run)
}

async fn get_locked_sysroot() -> Result<SysrootLock> {
    // See: ./ostree-load.md:29:0
    prepare_for_write()?;

    // Returns a default Sysroot structure
    // See: ./ostree-load.md:69:0
    let sysroot = ostree::Sysroot::new_default();

    // calls ostree_sysroot_set_mount_namespace_in_use
    // which just does `self->mount_namespace_in_use = TRUE`
    sysroot.set_mount_namespace_in_use();
    
    /// #define OSTREE_SYSROOT_LOCKFILE "ostree/lock"
    /// Tries to acquire a sysroot lock on the above file
    /// Nothing in the OstreeSysroot struct changes
    let sysroot = ostree_ext::sysroot::SysrootLock::new_from_sysroot(&sysroot).await?;

    /// Calls `ostree_sysroot_load` which calls `ostree_sysroot_load_if_changed`
    /// See: 
    sysroot.load(gio::Cancellable::NONE)?;

    Ok(sysroot)
}


fn prepare_for_write() -> Result<()> {
    use std::sync::atomic::{AtomicBool, Ordering};

    // This is intending to give "at most once" semantics to this
    // function. We should never invoke this from multiple threads
    // at the same time, but verifying "on main thread" is messy.
    // Yes, using SeqCst is likely overkill, but there is nothing perf
    // sensitive about this.
    static ENTERED: AtomicBool = AtomicBool::new(false);
    if ENTERED.load(Ordering::SeqCst) {
        return Ok(());
    }
    if ostree_ext::container_utils::is_ostree_container()? {
        anyhow::bail!(
            "Detected container (ostree base); this command requires a booted host system."
        );
    }
    if ostree_ext::container_utils::running_in_container() {
        anyhow::bail!("Detected container; this command requires a booted host system.");
    }
    anyhow::ensure!(
        ostree_booted()?,
        "This command requires an ostree-booted host system"
    );
    crate::cli::require_root(false)?;
    ensure_self_unshared_mount_namespace()?;
    if crate::lsm::selinux_enabled()? && !crate::lsm::selinux_ensure_install()? {
        tracing::warn!("Do not have install_t capabilities");
    }
    ENTERED.store(true, Ordering::SeqCst);
    Ok(())
}

```

```c
gboolean ostree_sysroot_load_if_changed(OstreeSysroot *self, gboolean *out_changed, GCancellable *cancellable, GError **error) {
    // See: ./ostree-load.md:114
    if (!ostree_sysroot_initialize(self, error)) return FALSE;

    // TODO: This has a lot, A LOT of things behind it... leaving it for now
    if (!ensure_repo(self, error)) return FALSE;

    struct stat stbuf;
    if (!glnx_fstatat(self->sysroot_fd, "ostree/deploy", &stbuf, 0, error))
        return FALSE;

    if (self->has_loaded && self->loaded_ts.tv_sec == stbuf.st_mtim.tv_sec && self->loaded_ts.tv_nsec == stbuf.st_mtim.tv_nsec) {
        if (out_changed) *out_changed = FALSE;
        /* Note early return */
        return TRUE;
    }

    g_clear_pointer(&self->deployments, g_ptr_array_unref);
    g_clear_object(&self->booted_deployment);
    g_clear_object(&self->staged_deployment);

    self->bootversion = -1;
    self->subbootversion = -1;

    // See: ./ostree-load.md:167
    if (!sysroot_load_from_bootloader_configs(self, cancellable, error)) return FALSE;

    self->loaded_ts = stbuf.st_mtim;
    self->has_loaded = TRUE;

    if (out_changed) *out_changed = TRUE;
    return TRUE;
}


// Opens an FD to sysroot if not already open
// Reads /run/ostree-booted and reads it in. /run/ostree-booted has some metadata
gboolean ostree_sysroot_initialize(OstreeSysroot *self, GError **error) {
    // Open a directory file descriptor for the sysroot if we haven't yet 
    if (!ensure_sysroot_fd(self, error)) return FALSE;

    if (self->loadstate >= OSTREE_SYSROOT_LOAD_STATE_INIT) return TRUE;

    /* Gather some global state; first if we have the global ostree-booted flag;
     * we'll use it to sanity check that we found a booted deployment for example.
     * Second, we also find out whether sysroot == /.
     */
    glnx_autofd int booted_state_fd = -1;

    #define OSTREE_PATH_BOOTED "/run/ostree-booted"
    // Simply opens the path and ignores ENOENT
    if (!ot_openat_ignore_enoent(AT_FDCWD, OSTREE_PATH_BOOTED, &booted_state_fd, error)) return FALSE;

    const gboolean ostree_booted = booted_state_fd != -1;

    if (booted_state_fd != -1) {
        g_autoptr(GVariant) ostree_run_metadata_v = NULL;

        // Reading the metadata, not sure about the details
        if (!ot_variant_read_fd(booted_state_fd, 0, G_VARIANT_TYPE_VARDICT, TRUE, &ostree_run_metadata_v, error)) {
            return glnx_prefix_error(error, "failed to read %s", OTCORE_RUN_BOOTED);
        }

        self->run_ostree_metadata = g_variant_dict_new(ostree_run_metadata_v);
    }

    // Gather the root device/inode
    {
        struct stat root_stbuf;
        // This is basically same as fstatat, but with erorr retries and more
        if (!glnx_fstatat(AT_FDCWD, "/", &root_stbuf, 0, error)) return FALSE;
        self->root_device = root_stbuf.st_dev;
        self->root_inode = root_stbuf.st_ino;
    }

    struct stat self_stbuf;
    if (!glnx_fstatat(AT_FDCWD, gs_file_get_path_cached(self->path), &self_stbuf, 0, error)) return FALSE;

    const gboolean root_is_sysroot = (self->root_device == self_stbuf.st_dev && self->root_inode == self_stbuf.st_ino);

    self->root_is_ostree_booted = (ostree_booted && root_is_sysroot);
    g_debug("root_is_ostree_booted: %d", self->root_is_ostree_booted);
    self->loadstate = OSTREE_SYSROOT_LOAD_STATE_INIT;

    return TRUE;
}


static gboolean sysroot_load_from_bootloader_configs(OstreeSysroot *self, GCancellable *cancellable, GError **error) {
    struct stat stbuf;

    int bootversion = 0;
    // reads /boot/loader symlink and if it points to loader.0 version is 0, else if it points to loader.1 it's 1
    if (!read_current_bootversion(self, &bootversion, cancellable, error)) return FALSE;

    int subbootversion = 0;
    // similar to `read_current_bootversion` but reads `ostree/boot.%d`
    if (!_ostree_sysroot_read_current_subbootversion(self, bootversion, &subbootversion, cancellable, error)) return FALSE;

    g_autoptr(GPtrArray) boot_loader_configs = NULL;
    // Reads from `/sysroot/boot/loader/entries/*` and sorts the BLS files using the `version` field
    if (!_ostree_sysroot_read_boot_loader_configs(self, bootversion, &boot_loader_configs, cancellable, error)) return FALSE;

    g_autoptr(GPtrArray) deployments = g_ptr_array_new_with_free_func((GDestroyNotify)g_object_unref);

    for (guint i = 0; i < boot_loader_configs->len; i++) {
        OstreeBootconfigParser *config = boot_loader_configs->pdata[i];

        /* Note this also sets self->booted_deployment */

        // `looking_for_booted_deployment`
        // it checks the tuple (device number, inode number) for the directory to figure out which one is the 
        // booted deployment. `ostree-prepare-root` saves this in `/run/ostree-booted`
        if (!list_deployments_process_one_boot_entry(self, config, deployments, cancellable, error)) {
            return FALSE;
        }
    }

    if (self->root_is_ostree_booted && !self->booted_deployment) {
        if (!glnx_fstatat_allow_noent(self->sysroot_fd, "boot/loader", NULL, AT_SYMLINK_NOFOLLOW, error))
            return FALSE;

        if (errno == ENOENT) {
            return glnx_throw(error, "Unexpected state: %s found, but no /boot/loader directory", OSTREE_PATH_BOOTED);
        } else {
            return glnx_throw(error, "Unexpected state: %s found and in / sysroot, but bootloader entry not found", OSTREE_PATH_BOOTED);
        }
    }

    if (!_ostree_sysroot_reload_staged(self, error))
        return FALSE;

    /* Ensure the entires are sorted */
    g_ptr_array_sort(deployments, compare_deployments_by_boot_loader_version_reversed);

    /* Staged shows up first */
    if (self->staged_deployment) g_ptr_array_insert(deployments, 0, g_object_ref(self->staged_deployment));

    /* And then set their index variables */
    for (guint i = 0; i < deployments->len; i++) {
        OstreeDeployment *deployment = deployments->pdata[i];
        // v is basically -> deployment->index = i;
        ostree_deployment_set_index(deployment, i);
    }

    // something about is_physical and physical deployment here, idk it's never used

    self->bootversion = bootversion;
    self->subbootversion = subbootversion;
    self->deployments = g_steal_pointer(&deployments);

    return TRUE;
}
```


```c
OstreeSysroot x = OstreeSysroot {
  .path: /
  .sysroot_fd: -1
  .boot_fd: -1
  .boot_is_vfat: false
  .loadstate: 0
  .mount_namespace_in_use: false
  .root_is_ostree_booted: false
  .root_device: 0
  .root_inode: 0
  .is_physical: false
  .bootversion: 0
  .subbootversion: 0
  .has_loaded: false
  .loaded_ts: 0.0
  .opt_flags: 0x0
  .debug_flags: 0x0
  .staged_deployment: (OstreeDeployment *) NULL
  .booted_deployment: (OstreeDeployment *) NULL
}
```

