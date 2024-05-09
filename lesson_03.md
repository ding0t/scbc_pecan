# lesson 03

# Labs

1. Finish off general playlist  [Skills II problems 3 has nice walkthroughs!](/labs/pico_playlist_general_2_3.md)
1. [bases](https://play.picoctf.org/practice?originalEvent=1&page=1&search=bases)

# Objectives 

1. Understand base64

<img src="img/" width="400" height="200">

# Expected base knowledge

1. A computer stores information in binary
1. Understanding number representation in computers
1. Understanding the same number can be represented in different bases (binary, octal, decimal, hexadecimal)
1. Familiar with basic charachter encding (ASCII, UTF-8)

# Expected tool skills

1. Basic Linux terminal skills
    1. Navigating directories `ls, cd, mkdir, pwd`
    1. Finding help `man man` or try `<command> -h`
    1. Viewing content of a file `cat`
    1. Viewing permissions `ls -la`
    1. Changing permissions `chmod`
    1. Downloading a file `wget`
    1. Accessing another system `nc, ssh`
    1. Examion file type `file`
    1. Using tab to complete a line
    1. Using up arrow to load the last line(s) executed

1. [CyberChef](https://gchq.github.io/CyberChef/)
    1. Load input
    1. Add recipies
    1. Load an existing recipie

1. Python
    1. Execute python
    1. Use the Python interactive shell

# But I dont feel like a 1337 hax0r?

1. Watch the pico general skills [video1](https://www.youtube.com/watch?v=3OawXnTELqA) and [video2](https://www.youtube.com/watch?v=FJ9le5rFGnA)
1. Finish all the picoCTF general skills challenges
1. Ask for help!!!


# Base64

A binary to text encoding. That means it can stuff any sequence of bits into a text representation of those bits.

### Why it exists

1. To avoid the interpritation of bytes as instructions by a system handling the data.


### Why know it

Base64 is exceptionally common in challenges. 
 
### How it is used

1. Email attachments are typically encoded
1. It is used allot in web data transfers

## Some tests

Try decoding `WW91IGFyZSBhd2Vzb21lIOKcqAo=`

With
1. [CyberChef](https://gchq.github.io/CyberChef/)
1. [ChatGPT](https://chatgpt.com/)