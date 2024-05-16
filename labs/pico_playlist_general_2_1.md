# General skills in CTF II - problems set 1

##  Nice netcat

```yaml
title: [Nice netcat](https://play.picoctf.org/playlists/14?m=98)
type: general
skills: shell, encoding
difficulty: easy
hint: encoding
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
type: general
skills: python and shell
difficulty: easy
hint: this mainly tests your ability to execute a python file
```

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

## Magikarp Ground Mission


```yaml
title: [Magikarp Ground Mission](https://play.picoctf.org/playlists/14?m=101)
type: general
skills: shell, ssh
difficulty: easy

```

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