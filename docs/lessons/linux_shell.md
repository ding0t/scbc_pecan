## Essential skills

Allot of the picoCTF challenges require skills in the Linux command line tools. Embrace it, and practice.

During competition you will have access to a kali workstation. This is a Linux system that you will need to be familiar with.

### Gotchas

In the terminal keep in mind:

1. Your current working directory - where are you and your scripts
1. Your PATH - a script not in PATH will not be found - so run it explicitly
1. Executable - if you think you can run something but get a fail - check it is executable
1. Scripts - if not made executable can be called by the interpreter directly e.g `python3 ./my_script.py`
1. Permissions - do you need to use sudo
1. Output - know where your output will go

## Common commands

1. Shortcuts to launch a terminal
    ```sh
    # usually <CTRL> + <SHIFT> + <t>
    ```
1. Navigating directories 
    ```sh
    ls, cd, mkdir, pwd
    ```
1. Finding help 
    ```sh
    # many tools have a man page, for example
    man man

    # or try a tools inbuilt help
    `<command> -h
    ```
1. Viewing content of a file 
    ```sh
    cat
    ```
1. Viewing permissions 
    ```sh
    ls -la
    ```
1. Changing permissions 
    ```sh
    chmod

    #make it executable
    chmod +x
    ```
1. Downloading a file 
    ```sh
    wget
    ```
1. Finding files
    ```sh
    # look for files that have a txt extension, from the current working directory.
    find . -type f -iname "*.txt"
    ```
1. Grep
    ```sh
    grep
    ```
1. Extracting archives
    ```sh
    unzip <filename>
    ```
1. Accessing another system over the network 
    ```sh
    # use netcat
    nc <IP>  <PORT>

    # get a shell on another system
    ssh <user@<host>
    ```
1. Examine file type 
    ```sh
    file <filename>
    ```
1. Use shortcuts
    1. Using tab to complete a line
    1. Using up arrow to load the last line(s) executed

## Handy guides

Do have a look at these if you are struggiling

* [Linux command line for beginners](https://ubuntu.com/tutorials/command-line-for-beginners#1-overview)
* [Essential Linux commands](https://itsfoss.com/essential-ubuntu-commands/)
* [learn unix](https://www.tutorialspoint.com/unix/index.htm)

