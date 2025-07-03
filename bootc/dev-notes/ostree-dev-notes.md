Used to write back deployemnts after a rollback

```c
gboolean
ostree_sysroot_write_deployments_with_options (OstreeSysroot *self, GPtrArray *new_deployments,
                                               OstreeSysrootWriteDeploymentsOpts *opts,
                                               GCancellable *cancellable, GError **error)
```


