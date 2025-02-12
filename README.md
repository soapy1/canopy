# Canopy

The goal of this project is to prove out syncing environments from (park)[github.com/soapy1/park] to a volume. 

This can be used by applications like jupyter to provision environments.

## Running

To setup canopy, you'll need to setup some env vars:
* `PARK_URL`: the full URL to the park server
* `TARGET_PATH`: the full path to sync environments to
* `WATCHED_NAMESPACES`: list of namespaces in park to watch for updates, seperated by commas, no spaces. For example, `sophia,dev,everyone`

Run the project with pixi
```
$ pixi install
$ pixi run canopy
```

