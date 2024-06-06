# Intro to cryptography

First, a good resource is [crypto-it](https://www.crypto-it.net/eng/simple/index.html)

Cryptography is used to provide confidentiality and integrity of data. 
There are a few broad cryto related concepts:


#### Hashing 

- think of it as a uniq signature of a data blob
- a one way function 
- results in a fixed length string for the algorithm
- always the same string for the same data blob
- used for integrity checking

#### Encryption

- a means of scrambling data to make it unrecoverable by those not intended to view it
- two way function - data can be recovered
- used for confidentaility and integrity

#### Encoding

- not a cipher or encryption
- intended to package data for transport

#### Steganography

- the hiding of data within other data
- intended to hide secret data inside data that appears benign
- common example is hiding data in image files


## Encryption

Standard encryption typically has four components to keep in mind:

1. Encryption algorithm
1. Message or plaintext
1. Key
1. Ciphertext

### Transposition ciphers

Shift letters left or right

#### Caesar cipher or shift cipher (ROT)

A shift of some defined length, e.g. ROT13

How to break it, iterate through shifting by a certain amount until the cipohertext becomes plaintext.

#### Caesar box cipher

The plaintext is written out into a predetermined number of rows, and padded with a `X` or `=`

HELLO SOUTH COAST in a 3 row column:

```txt
H L O H A
E O U C S
L S T O T
```

Makes the ciphertext: `HLOHAEOUCSLSTOT`

#### Atbash

The first letter of the alphabet becomes the last. Then the ciphertext is made by looking up the message in the atbash
Interstingly applied first to Hebrew language, and used in the [Bible](https://www.gotquestions.org/Atbash-code.html)

```py
import string
from collections import deque

# Make the alphabetic lists - notice only lowercase for convenmiance 
abc = deque(list(string.ascii_lowercase))
atbash = deque(list(string.ascii_lowercase))
atbash.reverse()

message = 'babylon'
ciphertext= ''
# lets iterate over each charachter in the message to make our ciphertext
for i,s in enumerate(message):
    idx = abc.index(s.lower())
    cipher_char = atbash[idx]
    ciphertext += cipher_char
print(ciphertext)
```

Outputs: `yzybolm`

### Substitution cipher

Mainly intended for plaintext ciphers. Mapping of alphabetic charachters to another charachter


#### One time pad

[Ref](https://www.geeksforgeeks.org/implementation-of-vernam-cipher-or-one-time-pad-algorithm/)

[ref with good hiostory](https://www.ciphermachinesandcryptology.com/en/onetimepad.htm)

1. plaintext
1. key - at last as long as plaintext, and random
1. one time pad - only used once, destroyed after use

Example of a pad; use only one of the rows:

Using row 'A'

H E L L O == 7 4 11 11 14
M O N E Y == 12 14 13 4 24

A+B       = 19 18 24 15 38

We only need 0 to 25 so:

 % 26 = 19 18 24 15 12 == T S Y P M


```txt
    0 1 2 3 4 5 6 7 8 9 ...
    A B C D E F G H I J K L M N O P Q R S T U V W X Y Z 
   +----------------------------------------------------
A | A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
B | B C D E F G H I J K L M N O P Q R S T U V W X Y Z A
C | C D E F G H I J K L M N O P Q R S T U V W X Y Z A B
D | D E F G H I J K L M N O P Q R S T U V W X Y Z A B C
...
```

#### Vigenère

[ref](https://www.crypto-it.net/eng/simple/vigenere-cipher.html)

Uses a `tabula recta` to transpose plaintext agains a key. Very similar to a one time pad.

#### XOR

Operates on bytes- as good as one time pad if key is same length as plaintext

```txt
1 ^ 1 = 0
1 ^ 0 = 1
0 ^ 0 = 0
```

## Breaking encryption

Good encryption is hard, and common vulnerabilities are well documented. They fall into a few catagories

1. Computational feasability
1. Implementation error
1. Algorithm error
1. Key exchange compromise