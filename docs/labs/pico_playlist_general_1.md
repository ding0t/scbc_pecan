# General skills in CTF I 

[link to pico general playlist](https://play.picoctf.org/playlists/14?m=89)

## Problem set 1

_remember to submit flags in the format `picoCTF{flag}`_

### Lets warm up


* [Background reading 1](https://dev.to/neumaneuma/decoding-the-confusing-world-of-encodings-part-1-3oke)
* [Background reading 2](https://kunststube.net/encoding/)

[_This is a lesson in charachter encoding_](https://play.picoctf.org/playlists/14?m=90) we can solve it using 

1. open up the pico `>_Webshell`
    ```sh
    # Start an interactive python session
    python3

    # assign the hexadecimal number to the variable 'ord'
    ord = 0x70

    # show me the number representation
    hex(ordinal)
    bin(ord)
    print(ord)

    # show me the charachter representation using ascii encoding
    chr(ord)

    # exit the interactive session
    exit()
    ```
1. Using cyberchef
    1. [Open cyberchef](https://gchq.github.io/)
    1. Enter `0x70` into the iput field
    1. Search for 'hex'
    1. drag and drop `from hex` onto the recipie
    1. check the output
    1. remove the '0x' in front of the input value - did it change the output?
1. Enter the flag as `picoCTF{flag}`


### 2Warm

_try using an interactive Python shell to solve this_

<details>
<summary><b>Walkthrough</b></summary>

</details>

### WarmedUp

_try using [cyberchef](https://gchq.github.io/CyberChef) to solve this_

<details>
<summary><b>Walkthrough</b></summary>

</details>

## Problem Set 2

### Obedient Cat


<details>
<summary><b>Walkthrough</b></summary>

Using a Linux shell

```sh
wget 'https://mercury.picoctf.net/static/fb851c1858cc762bd4eed569013d7f00/flag'
file flag
cat flag
```

</details>

### [wave a flag](https://play.picoctf.org/playlists/14?m=95)

skill: working with executable files in linux shell

hints: 

'how do you make a file executable in linux?'

'-h is usually a good way to try asking for help

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


### convertme.py

<details>
<summary><b>Walkthrough</b></summary>

```chef
From_Decimal('Space',false)
To_Binary('Space',8)
```

</details>

### [what's a net cat?](https://play.picoctf.org/playlists/14?m=97)


<details>
<summary><b>Walkthrough</b></summary>

```sh
man nc

```

</details>




