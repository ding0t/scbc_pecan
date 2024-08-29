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

<div class="grid cards" markdown>

-   :material-clock-fast:{ .lg .middle } __Essentials__

    ---
    - Start a terminal: `# usually <CTRL> + <SHIFT> + <t>`
    - Tab completeion - use it : `TAB`
    - Who am i `id`


-   :fontawesome-brands-markdown:{ .lg .middle } __Navigating directories__

    ---
    - Print working directory: `pwd`
    - List contents: `ls -lah`
    - List in a nice tree: `tree <dirname>`
    - Change directory: `cd <dir name>`
    - Change to home `cd ~`
    - Make a new dir: `mkdir <dirname>`
    - Many tools have a man page: `man <toolname>`

-   :material-format-font:{ .lg .middle } __File actions__

    ---
    - Finding files: `find . -type f -iname "*.txt"`
    - Show permissions: `ls -la`
    - Changing permissions: `chmod`
    - Make it executable: `chmod +x`
    - Download a file: `wget <url>`
    - Extract a file: `unzip <filename>`


-   :material-magnify-scan:{ .lg .middle } __Analysing Files__

    ---
    Remember binary files are different to text files

    - What type of file: `file <filename>`
    - Show file metadata: `exiftool <filename>`
    - Show file content: `cat <filename>`
    - Show file structure: `binwalk <filename>`
    - Find content in a file: ` grep -ir findme <filename>`
    - Show strings in a file: `strings <filename>`

-   :material-script:{ .lg .middle } __Script__

    ---
    Make a new directory for a challenge:

    ```sh
    cd ~/
    newdir='challenge_name'
    cd ~
    mkdir ~/$newdir
    cd $newdir
    ```


-   :material-scale-balance:{ .lg .middle } __Connect__

    ---
    - get a shell on another system: `ssh <user@<host>`
    - Connect to an open port with netcat: `nc <IP>  <PORT>`


</div>

## Handy guides

Do have a look at these if you are looking for more

* [Linux command line for beginners](https://ubuntu.com/tutorials/command-line-for-beginners#1-overview)
* [Essential Linux commands](https://itsfoss.com/essential-ubuntu-commands/)
* [learn unix](https://www.tutorialspoint.com/unix/index.htm)

