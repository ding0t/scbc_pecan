#!/usr/bin/env python3

import string
import sys
from collections import deque


#abc = string.ascii_lowercase
#one_time_pad = deque(list(abc))

one_time_pad = deque(list(string.ascii_lowercase))
# random.shuffle(one_time_pad)

help = """Synopsis: otp.py -e|-d

-e encrypt
-d decrypt 
-b brute_otp"""


def encrypt(msg, key):
    ciphertext = ''
    for idx, char in enumerate(msg):
        charIdx = abc.index(char)
        keyIdx = one_time_pad.index(key[idx])

        cipher = (keyIdx + charIdx) % len(one_time_pad)
        ciphertext += abc[cipher]

    return ciphertext

def decrypt(ciphertext, key):
    if ciphertext == '' or key == '':
        return ''

    charIdx = abc.index(ciphertext[0])
    keyIdx = one_time_pad.index(key[0])

    cipher_num = (charIdx - keyIdx) % len(one_time_pad)
    char = abc[cipher_num]

    return char + decrypt(ciphertext[1:], key[1:])

def brute_decrypt(ciphertext, key):
    if ciphertext == '' or key == '':
        return ''
    
    otp = one_time_pad
    for _ in range(len(one_time_pad)):
        decrypt=[]
        otp.rotate(-1)
        print(otp)
        for idx, char in enumerate(msg):
            charIdx = otp.index(ciphertext.lower()[idx])
            keyIdx = otp.index(key.lower()[idx])
            cipher_num = (charIdx - keyIdx) % len(otp)
            char = otp[cipher_num]
            decrypt.append(char)
        print(''.join(decrypt))
    #return char + decrypt(ciphertext[1:], key[1:])
    

if __name__ == '__main__':
    availableOpt = ["-d", "-e", "-b"]
    if len(sys.argv) == 1 or sys.argv[1] not in availableOpt:
        print(help)
        exit(0)

    key = input("Key: ").lower()
    msg = input("Message: ").lower()

    if sys.argv[1] == availableOpt[1]:
        print(encrypt(msg, key))
    elif sys.argv[1] == availableOpt[0]:
        print(decrypt(msg, key))
    elif sys.argv[1] == availableOpt[2]:
        brute_decrypt(msg, key)