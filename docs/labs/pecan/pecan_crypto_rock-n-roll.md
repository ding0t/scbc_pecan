---
tags:
    - pecan
    - crypto
    - programming
---

# ["Rock 'N' Roll"](https://pecanplus.ecusdf.org/?page=challenges&challenge=rocknroll)

type: cryptography
difficulty: advanced


## Challenge 

"Jerry was a racecar driver, Knock Jerry down, Build Jerry up. Captain Pierce was a strong man, Put Jerry with Captain Pierce into The Racecar."

## Facts

1. This is a crypto challenge
1. racecar is a pallindrome
1. there is unnecesary capitalisation
1. The title is a hint


<details markdown>
<summary><b>Hint</b></summary>

look for picoCTF challenge `1_wanna_b3_a_r0ck5tar` or `mus1c`

</details>


<details markdown>
<summary><b>Walkthrough</b></summary>

Use the Rockstar interpreter [here](https://codewithrockstar.com/online)

Read the [docs](https://codewithrockstar.com/docs)

## Rockstar interpritation

1. Jerry was a racecar driver,
    * A poetic number literal
    * initialise varialbe Jerry with number 1 7 6
1. Knock Jerry down 
    * decrement Jerry
1. Build Jerry up
    * increment Jerry
1.  Captain Pierce was a strong man
    * A poetic number literal
    * Initialise 'Captain Pierce' to: 1 6 3 
1. Put Jerry with Captain Pierce into The Racecar
    * add Jerry to Captain Pierce and assign result to The Racecar

This successfully executes but does not print, so we need to get it to print to STDOUT.

Add a write to STDOUT `Say The Racecar`

</details>
