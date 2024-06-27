# [All your base](https://pecanplus.ecusdf.org/?page=challenges&challenge=allyourbase)

This challenge can be solved a couple of ways

## We have source

The file we download is a c source code file

When you have source, it makes reverse engineering allot easier.

See if you can read the source to find the flag...

```sh
dir=re_base
mkdir $dir && cd $dir
wget https://pecanplus.ecusdf.org/challenges/allyourbase/All_your_base.c
wget https://github.com/elzoughby/Base64/raw/master/base64.c
wget https://github.com/elzoughby/Base64/raw/master/base64.h
```

## Static binary analysis

now compile it

```sh
gcc -c -g base64.c
gcc -c -g All_your_base.c
gcc -o main base64.o All_your_base.o
```

### run strings

```sh
strings main | less
```

### Objdump

```sh
objdump -drS main | less
```

### Ghidra

[install ghidra](../lessons/tools.md#ghidra)

1. Set up a new project
1. Open code browser
1. file -> import file; select our `main` program
1. analyze