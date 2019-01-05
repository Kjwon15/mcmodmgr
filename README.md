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
  veinminer: 'VeinMiner 0.38.2 [MC1.12; rev 647]'
  journeymap: 'journeymap-1.12.2-5.5.3'
```

mc_version is Minecraft version.
`mod_list` contains `mod_name` as key and `mod_version` as value

mod_name can be extracted from curseforge. For example:
`https://minecraft.curseforge/projects/veinminer/`: `veinminer` as mod_name

mod_version can be extracted from download page. For example:
Goto https://minecraft.curseforge/projects/veinminer/files
**name** field from that table is the `mod_version`
