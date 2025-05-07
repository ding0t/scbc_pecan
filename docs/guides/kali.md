---
tags:
	- kali
---

# Setting up kali

## Startup script for kasm

```sh
function apt_install_tools(){
	A_TOOLS=(netcat
    nano
    xxd
    binwalk
	exiftool 
	burp  
	wireshark 
	nmap 
	hashcat
	)
    for i in "${A_TOOLS[@]}"; do
        apt install -y "${i}" >/dev/null 2>&1 & disown
    done
	
}
sudo apt_install_tools
```