---
tags:
    - picoCTF
    - crypto
---

## 'Mod 26' and '13'

Good hint here `ROT13`

<details markdown>
<summary><b> Walkthrough</b></summary>

1. open up [cyberChef](https://gchq.github.io/CyberChef/)
1. apply the recipie:
```json
ROT13(true,true,false,13)
```
1. Submit the flag!

</details>

## caesar

A good demo of caesar

<details markdown>
<summary><b> Walkthrough</b></summary>

1. We get given text like: `picoCTF{dspttjohuifsvcjdpoabrkttds}`

1. Yours will probably be different, so dont use this one.

1. Lets get just the ciphertext `dspttjohuifsvcjdpoabrkttds`

1. open up [cyberChef](https://gchq.github.io/CyberChef/)

1. Load the recipie `ROT13`

1. Paste in teh ciphertext

1. Increment/Decrement until you get some plaintext

</details>


## Easy1

This is not too bad as far as crypto goes, but will be easier with Python.

<details markdown>
<summary><b> Hint</b></summary>

This is  a [one time pad problem ](../../lessons/07_cryptography_intro.md#one-time-pad)

</details>

<details markdown>
<summary><b> Walkthrough</b></summary>


```py
import string
from collections import deque

key = 'SOLVECRYPTO'
ciphertext = 'UFJKXQZQUNB'

# deque is a handy module to handle collections
# great if we had a rotation applied
otp = deque(list(string.ascii_uppercase))

# make an empty list to storee decrypt
decrypt=[]

# loop over each charachter in the ciphertext
for idx, char in enumerate(ciphertext):
    # get the numeric value of the ciphertext char
    charIdx = otp.index(ciphertext.upper()[idx])
    # get the numeric value of the key char
    keyIdx = otp.index(key.upper()[idx])
    # Reverse the standard encryption algorithm
    # which is (cipher - key) mod 26
    cipher_num = (charIdx - keyIdx) % len(otp)
    # now lookup what char the number represents in our pad
    char = otp[cipher_num]
    # and add the char to a list
    decrypt.append(char)

# lets print out our plaintext list
print(''.join(decrypt))
```

To Brute force check out the script in the repo  `/src/Easy1.py`

</details>


## More Cookies

If you have done "Cookies" this is more of a crypto challenge

<details markdown>
<summary><b> Walkthrough</b></summary>

Under Construction

If you are here, Check out one online...

https://picoctf2021.haydenhousen.com/web-exploitation/more-cookies

</details>