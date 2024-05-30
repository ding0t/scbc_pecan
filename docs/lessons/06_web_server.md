---
tags:
    - lesson
    - web exploitation
---

# 06 Web hacking server side

We have learned about thinking of things server side and client side with regards to web vulnerabilities and exploitation.

Server side - means the vulenerability exists within how the server handles data we send to it.

Client side - generally the vulnerability in how the browser handles the code

## OWASP

Publish the [top ten](https://owasp.org/www-project-top-ten/) and [client side](https://owasp.org/www-project-top-10-client-side-security-risks/)


## Directory traversal

Really a form of local file inclusion, wherever we can insert a path into a web application, and have the application read the contents to us.

Finding them is generally through testing of fields where we can supply user input. If we have source for the web application we can look for calls to render a file.

[CTF101](https://ctf101.org/web-exploitation/directory-traversal/what-is-directory-traversal/) has a good write up

## local and remote file inclusion

The contents of the file will be included in the context of the web application - not great if that content is executable!

* local - the file is on the web server, maybe from an upload
* remote - the file is sourced over the network

## SQLi

[CTF101](https://ctf101.org/web-exploitation/sql-injection/what-is-sql-injection/) good explanation