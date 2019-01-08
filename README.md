# MMM

Minecraft Mod Manager


## Installation

```sh
$ pipsi install mcmodmgr
```


## Usage

Run `mmm <mods.yaml>` on Minecraft installation directory

```sh
$ cd ~/.minecraft
mmm mods.yml
```


## File format

```yaml
mc_version: 1.12.2

mod_list:
  veinminer: release
  journeymap: release
```

mc_version is Minecraft version.
`mod_list` contains `mod_name` as key and `release_phase` as value

mod_name can be extracted from curseforge. For example:
`https://minecraft.curseforge/projects/veinminer/`: `veinminer` as mod_name

release_phase is one of these:
- release
- beta
- alpha
