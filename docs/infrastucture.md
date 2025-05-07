# Infrastructure for CTF

Just some thoughts on infrastructure.

## Principals

- Ability to easily re-deploy a ctf workstation
- Kali is the most commonly expected, but really just need common tools installed on a debian host.
- Full virtualisation will be more reliable than a container. There can be some issues with port mapping when doing scanning etc.

## Virtualisation

### VirtualBox

Run on a Windows or Linux host

### Vagrant

Tool to stand up a virtual machine from an already built image, good for brining a host up and re-hydrating.

### Proxmox

Open source platform to host virtual machines

- [proxmox](https://www.proxmox.com/en/products/proxmox-virtual-environment/overview)
- [proxmox howto](https://www.virtualizationhowto.com/2024/03/proxmox-ebook-free-download-for-home-labs/)
- [proxmox home lab](https://ianrenton.com/blog/setting-up-proxmox-on-the-home-lab/)



## Kali infra

Some resources for investigating kali builds

- [kali packer](https://github.com/synick/Kali-Packer)
- [packer kali](https://github.com/net-shaper/packer-kali-linux)
- [build scripts](https://gitlab.com/kalilinux/build-scripts/kali-vagrant)
