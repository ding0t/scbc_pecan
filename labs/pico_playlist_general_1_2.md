# Problem set 2

## Obedient Cat

```yaml
title: [Obedient Cat](https://play.picoctf.org/playlists/14?m=94)
type: general
skill: linux shell commands for file operations
difficulty: easy
hint: [ 'man cat']
status: solved
flag: []: #
```

<details>
<summary><b>Walkthrough</b></summary>

Using a Linux shell

```sh
wget 'https://mercury.picoctf.net/static/fb851c1858cc762bd4eed569013d7f00/flag'
file flag
cat flag
```

</details>

## wave a flag

```yaml
title: [wave a flag](https://play.picoctf.org/playlists/14?m=95)
type: general
skill: working with executable files in linux shell
difficulty: easy
hint: 'how do you make a file executable in linux?','-h is usually a good way to try asking for help'
status: solved
flag: []: #
```

<details>
<summary><b>Walkthrough</b></summary>

```sh
# get the file and save locally
wget 'https://mercury.picoctf.net/static/a00f554b16385d9970dae424f66ee1ab/warm'
# make the file executable
chmod +x warm
./warm -h
```

</details>


## convertme.py

```yaml
title: []()
type: 
skill: 
difficulty: 
hint: 
status: 
flag: []: #
```
<details>
<summary><b>Walkthrough</b></summary>

```chef
From_Decimal('Space',false)
To_Binary('Space',8)
```

</details>

## what's a net cat?

```yaml
title: [what's a net cat?](https://play.picoctf.org/playlists/14?m=97)
type: general
skill: linux shell
difficulty: easy    
hint: 
status: solved
flag: []: #
```

<details>
<summary><b>Walkthrough</b></summary>

```sh
man nc

```

</details>
