

## [Bite my shiny metal...](https://pecanplus.ecusdf.org/?page=challenges&challenge=bite_my_shiny_metal)

Finding files we can read but are not directly linked...

<details markdown>
<summary><b>Walkthrough</b></summary>

1. Inspect the page 

1. Look at where the image is being served from <img source>

1. `Can you find the file` ok lets do that...

1. Can we do directory listing [img source](https://pecanplus.ecusdf.org/challenges/bite_my_shiny_metal) ...

1. Can we brute force ...
```sh
# check the help
gobuster help dir

# build the brute
gobuster dir -u https://pecanplus.ecusdf.org/challenges/bite_my_shiny_metal -w /usr/share/wordlists/dirbuster/directory-list-2.3-small.txt -s 200 -b ''
```

1. Did you find any files?

</details>


## [Lamb Source 1](https://pecanplus.ecusdf.org/?page=challenges&challenge=lamb_source1)

An exercise in reading page source... sauce hehe

<details markdown>
<summary><b>Walkthrough</b></summary>

1. Load the challenge page

1. Inspect the source for the page...

</details>

## [Mr Robot](https://pecanplus.ecusdf.org/?page=challenges&challenge=mr_robot)

Find a file...

<details markdown>
<summary><b>Walkthrough</b></summary>

1. Load source and notice working directory is `challenges/mr_robot/`

1. Can we dir list... https://pecanplus.ecusdf.org/challenges/mr_robot

1. lets try a gobuster

```sh
gobuster dir -u https://pecanplus.ecusdf.org/challenges/mr_robot -w /usr/share/wordlists/dirbuster/directory-list-2.3-small.txt -s 200 -b ''
```

1. Of course .. robots

1. Go to the restricted page

1. inspect source

1. Go to the newly found page

1. flag!

</details>