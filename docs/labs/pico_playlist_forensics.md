---
tags:
    - picoCTF
    - forensics
---


## []()


<details markdown>
<summary><b> Walkthrough</b></summary>

1. Make a new directory to work in  and cd into it
```sh
cd ~
dir='garden'
mkdir $dir && cd $dir 
```
1. Grab the file - your url may be different
```sh
wget
```

</details>

## Forensics I

### [Information](https://play.picoctf.org/playlists/16?m=115)

A good image forensics exercise.

<details markdown>
<summary><b> Walkthrough</b></summary>

1. Make a new directory to work in  and cd into it
```sh
cd ~
dir='information'
mkdir $dir && cd $dir 
```
1. Now grab the file of interest
```sh
# your url may differ!
wget https://mercury.picoctf.net/static/7cf6a33f90deeeac5c73407a1bdc99b6/cat.jpg
```
1. Remember a jgp has EXIF data, lets look there first
```sh
exiftool cat.jpg
```
1. you should have output like:
```txt
exiftool cat.jpg 
ExifTool Version Number         : 12.40
File Name                       : cat.jpg
Directory                       : .
File Size                       : 858 KiB
File Modification Date/Time     : 2021:03:15 18:24:46+00:00
File Access Date/Time           : 2024:06:10 07:16:40+00:00
File Inode Change Date/Time     : 2024:06:10 07:16:40+00:00
File Permissions                : -rw-rw-r--
File Type                       : JPEG
File Type Extension             : jpg
MIME Type                       : image/jpeg
JFIF Version                    : 1.02
Resolution Unit                 : None
X Resolution                    : 1
Y Resolution                    : 1
Current IPTC Digest             : 7a78f3d9cfb1ce42ab5a3aa30573d617
Copyright Notice                : PicoCTF
Application Record Version      : 4
XMP Toolkit                     : Image::ExifTool 10.80
License                         : cGljb0NURnt0aGVfbTN0YWRhdGFfMXNfbW9kaWZpZWR9
Rights                          : PicoCTF
Image Width                     : 2560
Image Height                    : 1598
Encoding Process                : Baseline DCT, Huffman coding
Bits Per Sample                 : 8
Color Components                : 3
Y Cb Cr Sub Sampling            : YCbCr4:2:0 (2 2)
Image Size                      : 2560x1598
Megapixels                      : 4.1
```
1. Notice the data that stands out? `Licence` looks interesting
    - it is not words you would expect of a licence
    - it contains base64 alphanumeric chars
1. Try and unbase64 it...

</details>

### [Glory of the Garden](https://play.picoctf.org/playlists/16?m=116)



<details markdown>
<summary><b> Walkthrough</b></summary>

1. Make a new directory to work in  and cd into it
```sh
cd ~
dir='garden'
mkdir $dir && cd $dir 
```
1. Grab the file - your url may be different
```sh
wget https://jupiter.challenges.picoctf.org/static/43c4743b3946f427e883f6b286f47467/garden.jpg
```
1. Lets look at the EXIF
```sh
exiftool garden.jpg
```
1. Nothing obvious here
1. Lets run a quick strings over the file - remember that looks through the binary data for any bytes that represent charachters.
```sh
strings garden.jpg
```
1. Flag?

</details>

### [Enhance](https://play.picoctf.org/playlists/16?m=117)

A look into SVG format, and some scripting to help wrangle the flag out of the text.

<details markdown>
<summary><b> Walkthrough</b></summary>

1. Make a new directory to work in  and cd into it
```sh
cd ~
dir='enhance'
mkdir $dir && cd $dir 
```
1. Grab the file - your url may be different
```sh
wget https://artifacts.picoctf.net/c/102/drawing.flag.svg
```
1. Do a `strings` on the file
1. Notice that it is XML - no binary data
1. The `id` field looks useful - lets grab them all and concatenate them
```txt
```
1. A script would be quicker than extracting by hand. We can ask chat gpt something like:
```txt
write python3 to extract the text of the id elements from an svg file named 'drawing.flag.svg' and concatenate them to print with no spaces
```
1. After fixing some generative AI bugs , we can get some Python like
```py
import xml.etree.ElementTree as ET

def extract_tspan_from_id(svg_file):
    tree = ET.parse(svg_file)
    root = tree.getroot()
    id_text=[]

    for elem in root.iter():
        if ('id' in elem.attrib) and (elem.text):
            id_text.append(elem.text)

    return id_text

# Replace 'drawing.flag.svg' with the path to your SVG file
svg_file = 'drawing.flag.svg'
flag = extract_tspan_from_id(svg_file)

print(''.join(flag).replace(' ',''))

```

1. You can copy nad paste this into a python file like:

```sh
nano solve.py
# Then CTRL+v
# Then CTRL+s
# Then CTRL+x

# Run it using:
python3 ./solve.py
```
</details>