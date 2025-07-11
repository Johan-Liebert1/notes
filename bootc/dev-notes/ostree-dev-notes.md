Used to write back deployemnts after a rollback

```c
gboolean
ostree_sysroot_write_deployments_with_options (OstreeSysroot *self, GPtrArray *new_deployments,
                                               OstreeSysrootWriteDeploymentsOpts *opts,
                                               GCancellable *cancellable, GError **error)
```

## Load deployment list, bootversion, and subbootversion from the rootfs @self.

```c
gboolean ostree_sysroot_load (OstreeSysroot *self, GCancellable *cancellable, GError **error);
```

## pin a deployment

```c
gboolean ostree_sysroot_deployment_set_pinned (OstreeSysroot *self, OstreeDeployment *deployment,
                                      gboolean is_pinned, GError **error);
```


## Loads the current bootversion, subbootversion, and deployments, starting from the bootloader configs which are the source of truth.

```c
static gboolean
sysroot_load_from_bootloader_configs (OstreeSysroot *self, GCancellable *cancellable,
                                      GError **error);
```


## Get the bootversion from the `/boot/loader` symlink.

```c
static gboolean
read_current_bootversion (OstreeSysroot *self, int *out_bootversion, GCancellable *cancellable,
                          GError **error)
```
