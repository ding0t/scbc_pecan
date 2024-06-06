---
tags:
    - picoCTF
    - web exploitation
    - server side
    - directory traversal
    - sqli
---

## Forbidden Paths

This one is a straight forward demonstration of a directory traversal vulnerability.

<details markdown>
<summary><b>Walkthrough</b></summary>

1. Read the challenge well. It tells you
    1. Where the website is served from `/usr/share/nginx/html/`
    1. The filename and location of the flag at `/flag.txt`.
1. This gives us a good hint it is looking for a directory traversal
1. Launch the instance and open up the `website`
1. Remember:
    1. to move up a directory use `../`
    1. you cannot move too high, the right number up directories is functionlly the same as too many
1. Look at the path - this is a linux system, not Windows
    1. Even try `../../../../etc/passwd`
1. Now try for the flag

</details>

