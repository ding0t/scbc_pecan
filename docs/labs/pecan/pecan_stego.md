---
tags:
    - pecan
    - forensics
---

# Pecan stego

## Head in the clouds

## Matchy Matchy

## Take note

## [The nerd](https://pecanplus.ecusdf.org/?page=challenges&challenge=thenerd)

This is a fairly simple data hiding, using standard file features...

<details markdown>
<summary><b> Walkthrough</b></summary>

1. Make a clean workspace...
1. Download the file `wget https://pecanplus.ecusdf.org/challenges/thenerd/nerd.jpg`
1. Examine the EXIF `exiftool nerd.jpg`
1. What doesnt look right...
1. What format is the text (hint there is only 0-9 a-f in the string)

</details>

## Aloha

## Steg Cat Practice

An exercise in repairing Python

<details markdown>
<summary><b> Walkthrough</b></summary>

1. Lets grab the files
```sh
cd ~
dir='stegcat'
mkdir $dir && cd $dir
wget https://pecanplus.ecusdf.org/challenges/steg-cat-practice/practice_image.png
wget https://pecanplus.ecusdf.org/challenges/steg-cat-practice/main_script_Practice.py
wget https://pecanplus.ecusdf.org/challenges/steg-cat-practice/LSBStegPractice_Script_To_Student.py
```

1. We can see from the file names this is likely an LSB challenge [(Least Significant Bit)](https://ctf101.org/forensics/what-is-stegonagraphy/#lsb-steganography)
1. Lets ahave a look at the scripts
```sh
nano -c main_script_Practice.py
nano -c LSBStegPractice_Script_To_Student.py
```
1. Great - we have an LSB implemntation run like `LSBSteg.py decode -i <input> -o <output>`
1. Have quickl look oin the internet - this looks like [LSBSteg.py](https://github.com/RobinDavid/LSB-Steganography)
1. Ok lets try running it as is
```sh
python3 main_script_Practice.py
```
1. Fails to run... now we need to troubleshoot the code...
    1.  errant '&' - try deleting it
    1. no cv2
        `pip install opencv-python`
    1. there is an exception raised that looks unreasonable
        - lets try commenting out that line
1. It may be more useful to grab the origianl code and call that

```sh
wget https://github.com/RobinDavid/LSB-Steganography/blob/master/LSBSteg.py
```

```py
from LSBSteg import *

# decoding
im = cv2.imread("practice_image.png")
steg = LSBSteg(im)
print("Text value:",steg.decode_text())
```

Bit short cutty but got us there. Encouraged to spend more time looking at why the modified library failed

</details>