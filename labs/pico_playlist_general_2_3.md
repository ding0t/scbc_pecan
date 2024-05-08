# General skills in CTF II - problems set 3

##  [Static ain't always noise](https://play.picoctf.org/playlists/14?m=105)

## Hints

1. `BASH` is mentioned - you know this is going to need a Linux terminal
1. Download the files
1. Examine what the files are
1. Follow the instructions

<details>
<summary><b>Walkthrough</b></summary>

Make sure you are working in a Linux terminal.

This challenge relies on terminal skills allot. 

1. First lets make a clean directory to work in
    ```sh
    mkdir static
    cd static
    ```
1. lets download the files we need
    ```sh
    wget https://mercury.picoctf.net/static/ff4e569d6b49b92d090796d4631a2577/ltdis.sh

    wget https://mercury.picoctf.net/static/ff4e569d6b49b92d090796d4631a2577/static
    ```
1. lets have a look at the shell script
    ```sh
    cat ltdis.sh
    ```
1. Ok looks like it will analyse an executable. Lets check what `static` is   
    ```sh
    file static
    ```
1. Ah - it is an executable file - we can tell that because the output says 
    > `ELF 64-bit LSB pie executable`
1. Ok lets make that shell script executable, otherwise we cannot run it
    ```sh
    chmod +x ltdis.sh
    ```
1. Now just check the permissions, looking for rwx (read write execute)
    ```sh
    ls -lah
    ```
1. Ok, lets run the shell script on that file
    ```sh
    ./ltdis.sh static
    ```
1. lets check what it made, lets try out the common alias for `ls -lah`
    ```sh
    ll
    ```
1. Ok we can see two new files, lets examioine their contents, strings is always anice place to start 
    ```sh
    cat static.ltdis.strings.txt
    ```
1. What if this file was massive, Lets up the flag hunting...
    ```sh
    grep -i picoctf static.ltdis.strings.txt
    ```
1. Submit the flag!
1. Tidy up - lets go back to our main home directory
    ```sh
    cd ~
    ```
</details>

### Reflection

Why not just run the executable?

## [strings it](https://play.picoctf.org/playlists/14?m=106)

### Hints

1. Use the linux terminal
1. Download the file
1. Look at the challenge namesake

<details>
<summary><b>Walkthrough</b></summary>

1. First lets make a clean directory to work in
    ```sh
    mkdir strings
    cd strings
    ```
1. lets download the files we need
    ```sh
    wget https://jupiter.challenges.picoctf.org/static/5bd86036f013ac3b9c958499adf3e2e2/strings
    ```
1. looks lik it downloaded ok. Lets check what this file is
    ```sh
    file strings
    ```
1. Another ELF!
1. Last cahllenge used strings, lets do that..
    ```sh
    strings strings
    ```
1. Bleh, thats allot of text, lets try grep again, and pipe the output into it
    ```sh
     strings strings | grep -i picoctf
    ```
1. That was easier! Ok, submit the flag and tidy up
    ```sh
    cd ~
    ```

</details>

### Reflection

1. How could they stop us using `grep` for the flag?
1. Are there other ways to solve this?

## [plumbing](https://play.picoctf.org/playlists/14?m=107)

<details>
<summary><b>Walkthrough</b></summary>

1. First lets make a clean directory to work in, but lets try out a little shell script to copy paste this in and run
    ```sh
    newdir='plumbing'
    cd ~
    mkdir $newdir
    cd $newdir
    ```
1. If you did [nice netcat](https://play.picoctf.org/playlists/14?m=98) this should sound familiar
    ```sh
    nc jupiter.challenges.picoctf.org 7480
    ```
1. Ok it is sending us back a heap of text, just press enter and you will be back out of the connection
1. Lets try sending that output to a file usin 
    ```sh
    nc jupiter.challenges.picoctf.org 7480 >> out.txt
    ```
1. Lets try the grep trick
    ```sh
    grep -i picoctf out.txt
    ```
1. Lets see if we can just pipe straight to grep too
    ```sh
    nc jupiter.challenges.picoctf.org 7480 | grep -i picoctf
    ```
1. That was actually a bit nicer, submit the flag and go home (thats what `~` means)
    ```sh
    cd ~
    ```

</details>

### Reflection

1. Pipes connect an output of one thing, to the input of another