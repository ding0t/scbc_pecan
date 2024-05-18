title: 'Love Letter'
link: [Love letter](https://pecanplus.ecusdf.org/?page=challenges&challenge=loveletter)
type: cryptography
difficulty: basic
status: solved
flag: 

# The challenge 


# Setup
* ability to write and execute Python code
* access the challenge and download a python script

# Solving

##  Read the challenge instructions
    1. Difficulty - use this to frame complexity of the solution
    1. What to do - decrypt ciphertext back to plain text
    1. What You have
        1. ciphertext
        1. Python script

## Lets look at the python script 

After downloading the python script...

```py
def encryptionFunction():
    #Variables
    ciphertext = []
    ascii_values = []  
    
    #Prompt to enter plaintext to be encrypted
    plaintext = input('Please enter text to be encrypted: ')

    #Each letter in the message is converted to ASCII and
    #appended to a list
    for character in plaintext:
        ascii_values.append(ord(character))

    #Each ASCII character is multiplied by 3
    for element in ascii_values:
        ciphertext.append(element * 3)

    #Ciphertext is returned
    return ciphertext
```

cool it gives us the encyption algorithm

## Key skills

1. Reading python
1. Understanding ascii encoding
1. Writing python 
    1. Researching what you need
    1. Debugging

## Solve it!


# Resources

* [representation vs encoding 1](https://dev.to/neumaneuma/decoding-the-confusing-world-of-encodings-part-1-3oke)
* [Background reading 2](https://kunststube.net/encoding/)