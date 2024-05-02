# pico general skills playlist

[link to pico general playlist](https://play.picoctf.org/playlists/14?m=89)

# Problem set 1

_remember to submit flags in the format `picoCTF{flag}`_

## Lets warm up

```yaml
title: []()
type: general
skill: charachter encoding
difficulty: easy
hint: look at the background reading
status: solved
flag: []: #
```

* [Background reading 1](https://dev.to/neumaneuma/decoding-the-confusing-world-of-encodings-part-1-3oke)
* [Background reading 2](https://kunststube.net/encoding/)

[_This is a lesson in charachter encoding_](https://play.picoctf.org/playlists/14?m=90) we can solve it using 


<details>
<summary><b>Walkthrough</b></summary>

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

</details>

## 2Warm

_try using an interactive Python shell to solve this_

```yaml
title: []()
type: general
skill: 
difficulty: easy
hint: 
status: unsolved
flag: []: #
```


## WarmedUp

_try using [cyberchef](https://gchq.github.io/CyberChef) to solve this_

```yaml
title: []()
type: general
skill: 
difficulty: easy
hint: 
status: unsolved
flag: []: #
```



