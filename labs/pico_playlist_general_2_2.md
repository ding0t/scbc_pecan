# General skills in CTF II - problems set 2

##  First Find

```yaml
title: [First find](https://play.picoctf.org/playlists/14?m=1038)
type: general
skills: shell, find command
difficulty: easy
hint: man find - look for iname
status: done
flag: []: #
```

<details>
<summary><b>Walkthrough</b></summary>

1. Open up a terminal, you can use the picoctf webshell, and copy the output

```sh
nc mercury.picoctf.net 22902
```

2. We need to decode the output, try this recipie

```sh
wget 
find -iname ''
```

</details>

