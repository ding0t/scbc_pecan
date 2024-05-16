# lesson 04

# Objectives 

1. Python fu ++

# Labs

1. Finish off the general challenges in picoCTF
    * [General 2-1 updated last two walthroughs](./labs/pico_playlist_general_2_1.md) - it was common to have issues with [python wrangling](https://play.picoctf.org/playlists/14?m=100)
    * [General 2-3](./labs/pico_playlist_general_2_3.md)
1. Get into some [crackmes](./labs/pico_general_crackme.md)
1. Try out the PECAN [Love letter](https://pecanplus.ecusdf.org/?page=challenges&challenge=loveletter)

---
---

<img src="img/python-logo.png" width="400" height="100">


## What is Python

First appearing in 1991, it is now one of the most popular programming languages in the world.  Python is a mainstay in many developer communities. Particulalry in CTF's and Cyber Security.

It is a high level language, with emphasis on code readability.

## Critical skills for Python in CTF's

1. Finding help
1. Reading Python code
1. Writing basic code

## Reading Python

If you download Python - have a look at it first. Its a good habit to do a basic traige - *"is this what I am expecting*" because plenty of malware gets distributed in dodgy code.

You can view it in a terminal using either:

```sh
# a quick basic view
cat
# or a nicer view with editing
nano 
```

## Writing Python

As challenges progress you will need to start writing some Python to help. If you are familiar with Python, sue the tool you are familiar with

In Kali we will have 

## Help in the interpreter

We have built in help - ok but often nicer online.

```sh
python3
Python 3.10.12 (main, Nov 20 2023, 15:14:05) [GCC 11.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> help(chr)
```

## Help online

There are plenty of docs online

## Help using AI

This is going to be a great place to start learning.

First a quick [intro to AI](./labs/_about_ai_coding.md)

🐧 Now ask ChatGPT what the following code does?

```py
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


flag_enc = open('level1.flag.txt.enc', 'rb').read()



def level_1_pw_check():
    user_pw = input("Please enter correct password for flag: ")
    if( user_pw == "8713"):
        print("Welcome back... your flag, user:")
        decryption = str_xor(flag_enc.decode(), user_pw)
        print(decryption)
        return
    print("That password is incorrect")



level_1_pw_check()
```

🐧 Now try [PW Crack 1](https://play.picoctf.org/practice?page=1&search=crack)

