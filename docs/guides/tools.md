---
tags:
    - guide
---

# Tools - handy ones

<div class="grid cards" markdown>

- :material-clock-fast:{ .lg .middle } __Multi tool__

    ---
    - Your go to tool is [CyberChef](https://gchq.github.io/CyberChef/)
        1. Load input
        1. Add recipies
        1. Load an existing recipie



- :fontawesome-brands-markdown:{ .lg .middle } __Crypto Tools__

    ---
    Use these tools to identify encoding or encryption

    - [boxentriq - cipher identifier](https://www.boxentriq.com/code-breaking/cipher-identifier)
        - good for identifying standsard encoding or encryption
    - [dcode - multi puzzle tool](https://www.dcode.fr/en)
        - a bit finicky
        - useful for specific puzzle types



- :material-format-font:{ .lg .middle } __Web Tools__

    ---

    - Web inspector on the browser (easy)
        - view page source
        - cookies
        - scripts
    - Gobuster (kali)
        - directory enumeration (moderate)
    - BurpSuite (kali)
        - request inspection and modification (challenging)


- :material-magnify-scan:{ .lg .middle } __Analysing Files__
    Use a linux terminal

    ---
    - Strings
    - ExifTool


- :material-script:{ .lg .middle } __Scripting__
Use Python

    ---
    1. Execute python
    1. Use the Python interactive shell


- :material-scale-balance:{ .lg .middle } __Connect__

    ---


</div>




### Gobuster

A tool to enumerate web sites

[Handy guide](https://sohvaxus.github.io/content/gobuster.html)

### Burpsuite

This tool is for web testing. A [startup guide](https://portswigger.net/burp/documentation/desktop/getting-started)

## Reversing

### Objdump

### Ghidra

Is an open source software reverse engineering suite of tools.

Find the tool site [here](https://ghidra-sre.org/)

```sh
sudo apt install -y openjdk-17-jdk
wget https://github.com/NationalSecurityAgency/ghidra/releases/download/Ghidra_11.1.1_build/ghidra_11.1.1_PUBLIC_20240614.zip
unzip ghidra_11.1.1_PUBLIC_20240614.zip 
# lets run ghidra
./ghidra_11.1.1_PUBLIC_20240614/ghidraRun
```
