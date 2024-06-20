---
tags:
    - lesson
    - steganography
    - forensics
---

# Steganography

Hiding data in plain sight. We covered in forensics that there are file formats such as immages, pdf, even filesystems. 
Each of these formats can be abused somewhat to hide data in either legitimate structures of the format, or by overloading the format without braking it.

An excellent quote:

> Steganography is hard for the defence side, because there’s practically an infinite number of ways it could be carried out.

[Source CTF 101](https://ctf101.org/forensics/what-is-stegonagraphy/)

Good news is that practically within a finite number of bytes there is a finite number of permutations to hide data, but there is allot.

## Common CTF Steganography

1. Metadata: EXIF
1. Strings
1. Establish steg tools

## Commopn tools

* Any file metadata tool - Exiftool is a good start
* Stegdetect
