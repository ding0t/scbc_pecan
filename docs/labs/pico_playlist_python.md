---
tags:
    - picoCTF
    - python
---

## Crackmes

An introduction to using Python and reverse engineering. Understanding:

* Python
* how software works
* its secrets/flaws

We will use the [Python playlist](https://play.picoctf.org/playlists/15?m=108)

## Problem set 1

## Problem set 2

### PW Crack 1

<details>
<summary><b>Walkthrough</b></summary>

1. First lets make a clean directory to work in, but lets try out a little shell script to copy paste this in and run
    ```sh
    cd ~/
    newdir='pw_crack1'
    cd ~
    mkdir ~/$newdir
    cd $newdir
    ```
1. Now lets grab the files
    ```sh
    wget https://artifacts.picoctf.net/c/12/level1.py
    wget https://artifacts.picoctf.net/c/12/level1.flag.txt.enc
    ```
1. ok - take a look at the python
    ```sh
    nano level2.py
    ```
</details>


## PW Crack 2

<details>
<summary><b>Walkthrough</b></summary>


1. First lets make a clean directory to work in, but lets try out a little shell script to copy paste this in and run
    ```sh
    newdir='pw_crack2'
    cd ~
    mkdir $newdir
    cd $newdir
    ```
1. Now lets grab the files
    ```sh
    wget https://artifacts.picoctf.net/c/14/level2.py
    wget https://artifacts.picoctf.net/c/14/level2.flag.txt.enc 
    ```
1. ok - take a look at the python
    ```sh
    nano level2.py
    ```
    ```py
    ### THIS FUNCTION WILL NOT HELP YOU FIND THE FLAG --LT ########################
    def str_xor(secret, key):
        #extend key to secret length
        new_key = key
        i = 0
        while len(new_key) < len(secret):
            new_key = new_key + key[i]
            i = (i + 1) % len(key)        
        return "".join([chr(ord(secret_c) ^ ord(new_key_c)) for (secret_c,new_key_c) in zip(secret,new_key)])
    ###############################################################################

    flag_enc = open('level2.flag.txt.enc', 'rb').read()

    def level_2_pw_check():
        user_pw = input("Please enter correct password for flag: ")
        if( user_pw == chr(0x34) + chr(0x65) + chr(0x63) + chr(0x39) ):
            print("Welcome back... your flag, user:")
            decryption = str_xor(flag_enc.decode(), user_pw)
            print(decryption)
            return
        print("That password is incorrect")
    ```
1. Does chr() function call look [familiar?](https://diveintopython.org/functions/built-in/chr)
1. Lets use python to solve this one. First start a python interpreter
    ```sh
    python3
    ```
1. Now lets evaluate user_pw from the check `==` and print it
    ```py
    user_pw = chr(0x34) + chr(0x65) + chr(0x63) + chr(0x39)
    print(user_pw)
    ```
1. Remember to exit the interpreter
    ```py
    exit()
    ```
1. Now call the function, enter the password, and copy out the flag!
    ```sh
    python3 ./level2.py
    ```

</details>

### PW Crack 3

<details>
<summary><b>Walkthrough</b></summary>


1. Lets start scripting the setup...
    ```sh
    cd ~
    newdir='pw_crack3'
    cd ~
    mkdir ~/$newdir
    cd $newdir
    wget https://artifacts.picoctf.net/c/18/level3.py
    wget https://artifacts.picoctf.net/c/18/level3.flag.txt.enc
    wget https://artifacts.picoctf.net/c/18/level3.hash.bin 

    ```
1. ok - take a look at the python
1. Lets modify it to brute force the key

```py
import hashlib

### THIS FUNCTION WILL NOT HELP YOU FIND THE FLAG --LT ########################
def str_xor(secret, key):
    #extend key to secret length
    new_key = key
    i = 0
    while len(new_key) < len(secret):
        new_key = new_key + key[i]
        i = (i + 1) % len(key)        
    return "".join([chr(ord(secret_c) ^ ord(new_key_c)) for (secret_c,new_key_>
###############################################################################

flag_enc = open('level3.flag.txt.enc', 'rb').read()
correct_pw_hash = open('level3.hash.bin', 'rb').read()


def hash_pw(pw_str):
    pw_bytes = bytearray()
    pw_bytes.extend(pw_str.encode())
    m = hashlib.md5()
    m.update(pw_bytes)
    return m.digest()


def level_3_pw_check():
    user_pw = input("Please enter correct password for flag: ")
    user_pw_hash = hash_pw(user_pw)
    
    if( user_pw_hash == correct_pw_hash ):
        print("Welcome back... your flag, user:")
        decryption = str_xor(flag_enc.decode(), user_pw)
        print(decryption)
        return
    print("That password is incorrect")

# The strings below are 7 possibilities for the correct password. 
#   (Only 1 is correct)
pos_pw_list = ["8799", "d3ab", "1ea2", "acaf", "2295", "a9de", "6f3d"]


for p in pos_pw_list:
    user_hash = hash_pw(p)
    if(user_hash ==  correct_pw_hash):
        decryption = str_xor(flag_enc.decode(), p)
        print(decryption)
        exit()
# level_3_pw_check()

```
1. You can experiment with chat GPT to solve it, but you need to be very clear waht you are asking of it, so really need to know the solution in your mind, and jsut ask chatGPT to get the syntax

</details>

## Extension

### Classic Crackme 0x100 - todo

<details>
<summary><b>Walkthrough</b></summary>

1. Lets start scripting the setup...
    ```sh
    cd ~
    newdir='classic_crackme'
    cd ~
    mkdir ~/$newdir
    cd $newdir
    wget https://artifacts.picoctf.net/c_titan/107/crackme100

    ```
1. File shows its an ELF
1. nc - we get prompted for a secret password
```
nc titan.picoctf.net 61096
```

</details>