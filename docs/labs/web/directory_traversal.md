---
title: Directory Traversal
tags:
    - picoCTF
    - web-exploitation
    - difficulty::medium
---


:book: An application does not sanitise user input, specifically when controlling the read of a file,
allowing a user to read arbitrary files through the web session.

:thumbsup: Remember:

- a computer filesystem is like a filing system, with things in paths
- a web application is a program running from a particular location.

## PicoCTF - Forbidden Paths

This one is a straight forward demonstration of a directory traversal vulnerability.

## Reading the challenge hints

- name tells us it is about paths
- website is filtering absolute file paths
  - absolute is like `/root/flag.txt`
  - relative is like `../../../root/flag.txt` i.e. relative to where we are in present working directory

## Understanding what the hint means

1. Read the challenge well. It tells you
    1. Where the website is served from `/usr/share/nginx/html/`
    1. The filename and location of the flag at `/flag.txt`.
1. This gives us a good hint it is looking for a directory traversal attack

So if we have shell this looks like:

```sh
$ pwd
/usr/share/nginx/html/
```

We need to move from there using a relative path. For example:

```sh
$ pwd ../../
/usr/share/
```

Now try and get flag!

## Walkthrough

<details markdown>
<summary><b>Walkthrough</b></summary>

1. Launch the instance and open up the `website`
1. Remember:
    1. to move up a directory use `../`
    1. you cannot move too high, the right number up directories is functionlly the same as too many
1. Look at the path - this is a linux system, not Windows
    1. Even try `../../../../etc/passwd`
1. Now try for the flag

</details>
