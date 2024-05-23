---
tags:
    - lesson
    - web exploitation
---

# Lesson 05 - Web hacking introduction


## News

* Introducing the new [site](https://ding0t.github.io/scbc_pecan/)
* [CTF101](https://ctf101.org/) - great for learning CTF skills

## Objectives 

* An introduction to web hacking/explotation

## Labs

1. Today focus on [web hacking](../labs/pico_web_exploitation.md)

Foundation hacker skills...

1. Python [playlist](../labs/pico_playlist_python.md)
1. Complete all in [general 2](../labs/pico_playlist_general_2.md)

## Web Exploitation

Visiting a web site through a browser started as just static sites like this one to share informatioon globally, 
but has grown now to the delivery of interactive applications, tracking, and advertising models.

This extra functionality has significantly incrfeased the amount of complexity and code required for applications. 
Hence building a web site now is significantly abstracted from the underlying complexity.

That means - to run a web service, one needs to trust a whole heap of people and their code that you do not know.

Either accidentaly or deliberatly, the complexity and absrtaction, means that there is allot of vulnerabilities in web applications.

Web hacking is presently a significant hacking vector.

### How the web works

First - think in terms of:

1. A client - your computer and browser
1. A server  - the remote system(s) serving the content

When you request a web resource:

1. Your computer resolves the human name (like `scbc.wa.edu.au`) to an IP address (DNS resoplution), and then establishes a connection to that server.
1. Your browser makes a HTTP(s) request to that server. This is the primary web transport protocol.
1. The server receives the request, processes it, and returns data based on the request.
1. Your browser receives the data, and renders it in the browser.

In the above, code is being run on both the client and server.

### Common web concepts

#### 🍦 Web server

The web server will serve out a particualr directory contents from the filesystem. And it can execute code in the context of the web server.

The web server will provide a service on a particualr port - typically 80 and 443

#### 🤖 Robots

Search engines work by visiting all the web pages with a `bot` often called a 🕷️ because they crawl the 🕸️.
For example [Googlebot](https://developers.google.com/search/docs/crawling-indexing/googlebot).

If you have information that you do not want appearing in global search engines - these can be excluded using the standard `robots.txt` file.

Let look at this more in a [lab](../labs/pico_web_exploitation.md#where-are-the-robots)


#### 🍪 Cookies

Cookies are little bits of data stored locally on your computer. There are differnt [types](https://www.cloudflare.com/en-gb/learning/privacy/what-are-cookies/)

There can be many of them associated with a site. Originally for maintining state for a website- they now are used allot to track web users for the purpose of advertising.

One of the best resources [about cookies](https://curl.se/docs/http-cookies.html)

##### Why

1. Session management
1. Personalisation
1. Tracking

##### Types

Session
Persistant
Authentication
Tracking

First party - created by the website itself
Third party - from a domain other than in the broser - great example is Facebook

## Tools

Today - we will use the develoepr tools - they come with documetnation:

* [Firefox](https://developer.mozilla.org/en-US/docs/Learn/Common_questions/Tools_and_setup/What_are_browser_developer_tools)
* [Edge](https://learn.microsoft.com/en-us/microsoft-edge/devtools-guide-chromium/overview)

## Resources

* [How the web works](https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/How_the_Web_works)
* [CTF101 Web Exploitation](https://ctf101.org/web-exploitation/)
