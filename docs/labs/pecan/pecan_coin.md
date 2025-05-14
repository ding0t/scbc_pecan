---
tags:
    - pecan
    - crypto
---

# Pecan Challenge Coin 2022

title: [2022 Challenge Coin](https://pecanplus.ecusdf.org/?page=challenges&challenge=coin-2022)
link: [link]()
type: cryptography
difficulty: advanced
status: unsolved
flag:

Coins usually work outer to inner

# outer

WMHD35RA3NIDSXTOHR3MTA0YUHCE4LNP

boxentriq - likely columnar trnsposition cipher

```json
Caesar_Box_Cipher(2)
```

`WH3R3ISTH3T0UC4NMD5ANDXORMAYHELP`

Where is the toucan md5 and xor may help

1. where is toucan
    - [toucan](https://github.com/penguingovernor/toucan)
    - gaurenteed not secure
    - look at the algorithm on github
1. md5
    - 32 hexadecimal characters equal 16 bytes IV
    - key or IV?

    ```sh
    echo 'WH3R3ISTH3T0UC4NMD5ANDXORMAYHELP' | md5sum     
    184b39d37e9b3603bfe26c70d14373c1
    ```

1. xor
    - key or IV
    - weakness in the cipher?

```sh
./toucan decrypt msgFile keyFile IVFile [outputFile]

echo -n "key" | ./toucan decrypt file.out /dev/stdin IV file.decrypted
```

1. msgFile
    - likely `89F72F41AB9001F122B63E244BEDB0C7BFEA661DFC8241A36B955B01666C2E3B08AD6017DF4`
    - save as bytes to file
1. keyFile
    - a secret
1. IV file
    - a secondary key that does not have to be secret
    - MD5 of something fits the 16byte IV for 128bit

# INNER

89F72F41
AB9001F122B63E
244BEDB0C7BFEA66

1DFC8241A36B955B
01666C2E3B08AD6
017DF4

89F72F41AB9001F122B63E244BEDB0C7BFEA661DFC8241A36B955B01666C2E3B08AD6017DF4

## dcode

Comes up as [ASCCI shift cipher](https://www.dcode.fr/ascii-shift-cipher)
 +40 is closest? but none really

# HEIRO

ABCDEDBF
GAHDB

ABCDEDBFGAHDB

# try

dcode.fr

## using part as a key

1. looks like the main inner is encryptin - use outer as key
