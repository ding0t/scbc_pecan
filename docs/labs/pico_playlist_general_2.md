---
tags:
    - picoCTF
    - general
---

# General skills in CTF II 

## Problem set 1

###  [Nice netcat](https://play.picoctf.org/playlists/14?m=98)

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

### [Tab tab attack](https://play.picoctf.org/playlists/14?m=99)

hint: in title - use tab complete


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


### [Python Wrangling](https://play.picoctf.org/playlists/14?m=100)

hint: this mainly tests your ability to execute a python file

<details>
<summary><b>Walkthrough</b></summary>

1. First lets make a clean directory to work in, but lets try out a little shell script to copy paste this in and run
    ```sh
    newdir='py_wrangling'
    cd ~
    mkdir $newdir
    cd $newdir
    ```
1. get all three files 
    ```sh
    wget https://mercury.picoctf.net/static/1b247b1631eb377d9392bfa4871b2eb1/ende.py
    wget https://mercury.picoctf.net/static/1b247b1631eb377d9392bfa4871b2eb1/pw.txt
    wget https://mercury.picoctf.net/static/1b247b1631eb377d9392bfa4871b2eb1/flag.txt.en
    ```
1. Lets ahve a look at the script first
    ```
    nano ende.py
    ```
    * Looking over the source we get a good idea what it does. And looking at the `print()` syntax, it is python3
    * To exit nano use `CTRL + 'x'`
1. Now we know th efile looks safe, Lets run the python
    ```sh
    python3 ./ende.py
    ```
    * It is pretty basic - but looks like from reviewing the code we need to pass it an argument
1. cat the password file - we may need this
    ```sh 
    cat pw.txt
    ```
1. execute the script to see the args
    ```sh
    python3 ./ende.py -d ./flag.txt.en
    ```
    * It asks for a password, copy the one we cat' out, and paste
1. You should have a flag!

</details>

### [Magikarp Ground Mission](https://play.picoctf.org/playlists/14?m=101)



<details>
<summary><b>Walkthrough</b></summary>

1. Run the container
1. ssh into the container - the command is given and will be something like
    ```sh
    ssh ctf-player@venus.picoctf.net -p 51614
    ```
1. Use the following commands 
    ```sh
    ls
    cat
    ```
1. Cat out what we see in our home directory
    ```sh
    ls
    cat 1of3.flag.txt 
    cat 
    ```
1. The instructions tell us to go to root `/`
    ```sh
    cd /
    ls
    cat 2of3.flag.txt
    cat instructions-to-3of3.txt
    ```
1. The instructions tell us to go home ! The common abbreviation of our home is `~`
    ```sh
    cd ~
    ls
    cat 3of3.flag.txt
    ```
1. Piece together your flag componets for the flag
1. Or... Lets script a whole flag
    ```sh
    cat ~/drop-in/1of3.flag.txt /2of3.flag.txt ~/3of3.flag.txt | tr -d "\n"
    ```

</details>

## Problem set 2

### [First Grep - todo](https://play.picoctf.org/playlists/14?m=102)

###  [First find](https://play.picoctf.org/playlists/14?m=1038)

hint

```sh
man find 
/iname
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

### [Big Zip - todo](https://play.picoctf.org/playlists/14?m=104)

## Problems set 3

###  [Static ain't always noise](https://play.picoctf.org/playlists/14?m=105)

Hints

* `BASH` is mentioned - you know this is going to need a Linux terminal
* Download the files
* Examine what the files are
* Follow the instructions

Make sure you are working in a Linux terminal.

This challenge relies on terminal skills allot. 

<details>
<summary><b>Walkthrough</b></summary>

* First lets make a clean directory to work in
```sh
mkdir static
cd static
```
* lets download the files we need
```sh
wget https://mercury.picoctf.net/static/ff4e569d6b49b92d090796d4631a2577/ltdis.sh

wget https://mercury.picoctf.net/static/ff4e569d6b49b92d090796d4631a2577/static
```
* lets have a look at the shell script
```sh
cat ltdis.sh
```
* Ok looks like it will analyse an executable. Lets check what `static` is   
```sh
file static
```
* Ah - it is an executable file - we can tell that because the output says 
    `ELF 64-bit LSB pie executable`
* Ok lets make that shell script executable, otherwise we cannot run it
```sh
chmod +x ltdis.sh
```
* Now just check the permissions, looking for rwx (read write execute)
```sh
ls -lah
```
* Ok, lets run the shell script on that file
```sh
./ltdis.sh static
```
* lets check what it made, lets try out the common alias for `ls -lah`
```sh
ll
```
* Ok we can see two new files, lets examioine their contents, strings is always anice place to start 
```sh
cat static.ltdis.strings.txt
```
* What if this file was massive, Lets up the flag hunting...
```sh
grep -i picoctf static.ltdis.strings.txt
```
* Submit the flag!
* Tidy up - lets go back to our main home directory
```sh
cd ~
```

</details>

Reflection

Why not just run the executable?

### [strings it](https://play.picoctf.org/playlists/14?m=106)

* Use the linux terminal
* Download the file
* Look at the challenge namesake

<details>
<summary><b>Walkthrough</b></summary>

* First lets make a clean directory to work in
```sh
mkdir strings
cd strings
```
* lets download the files we need
```sh
wget https://jupiter.challenges.picoctf.org/static/5bd86036f013ac3b9c958499adf3e2e2/strings
```
* looks lik it downloaded ok. Lets check what this file is
```sh
file strings
```
* Another ELF!
* Last cahllenge used strings, lets do that..
```sh
strings strings
```
* Bleh, thats allot of text, lets try grep again, and pipe the output into it
```sh
    strings strings | grep -i picoctf
```
* That was easier! Ok, submit the flag and tidy up
```sh
cd ~
```

</details>

* How could they stop us using `grep` for the flag?
* Are there other ways to solve this?

### [plumbing](https://play.picoctf.org/playlists/14?m=107)

<details>
<summary><b>Walkthrough</b></summary>

* First lets make a clean directory to work in, but lets try out a little shell script to copy paste this in and run
```sh
newdir='plumbing'
cd ~
mkdir $newdir
cd $newdir
```
* If you did [nice netcat](https://play.picoctf.org/playlists/14?m=98) this should sound familiar
```sh
nc jupiter.challenges.picoctf.org 7480
```
* Ok it is sending us back a heap of text, just press enter and you will be back out of the connection
* Lets try sending that output to a file usin 
```sh
nc jupiter.challenges.picoctf.org 7480 >> out.txt
```
* Lets try the grep trick
```sh
grep -i picoctf out.txt
```
* Lets see if we can just pipe straight to grep too
```sh
nc jupiter.challenges.picoctf.org 7480 | grep -i picoctf
```
* That was actually a bit nicer, submit the flag and go home (thats what `~` means)
```sh
cd ~
```

</details>

Reflection

* Pipes connect an output of one thing, to the input of another