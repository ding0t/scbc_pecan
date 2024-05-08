# General skills in CTF II - problems set 1

##  Nice netcat

```yaml
title: [Nice netcat](https://play.picoctf.org/playlists/14?m=98)
type: general
skills: shell, encoding
difficulty: easy
hint: encoding
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

```chef
From_Decimal('Space',true)
```

</details>

## Tab tab attack

```yaml
title: [Tab tab attack](https://play.picoctf.org/playlists/14?m=99)
type: general 
skills: shell
difficulty: easy
hint: in title - use tab complete
status: done
flag: []: #
```


<details>
<summary><b>Walkthrough</b></summary>

Intended solution is to  `cd A<tab>`

We can also just do a ls -R

```sh
wget https://mercury.picoctf.net/static/3afd18a65e42b80526aa87f9766c588b/Addadshashanammu.zip
unzip A<tab>
cd <tab>

cat or execute the file
```

</details>


# Python Wrangling

```yaml
title: [Python Wrangling](https://play.picoctf.org/playlists/14?m=100)
type: 
skills: 
difficulty: 
hint: 
status: 
flag: []: #
```

<details>
<summary><b>Walkthrough</b></summary>

1. get all three files 
1. cat the password file
1. execute the script to see the args
1. decrypt flag file

```sh
wget
cat
python3
```

</details>

## Magikarp Ground Mission


```yaml
title: [Magikarp Ground Mission](https://play.picoctf.org/playlists/14?m=101)
type: general
skills: shell, ssh
difficulty: esay
status: solved
flag: []: #
```

<details>
<summary><b>Walkthrough</b></summary>

1. Run the container
1. ssh into the container

```sh
ls
cat

```

</details>