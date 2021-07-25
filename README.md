# dupremove
Remove duplicate strings, integers and lot more with multithreading

# Installation

```
$ git clone https://github.com/DevanshRaghav75/dupremove.git
$ cd dupremove
$ python3 setup.py install 
$ dupremove
```

# Usage

for ex. I have created a file called `dups.txt` and this is the content of `dups.txt` file:

```
$ cat dups.txt
hack
fake
lol
dev
pro
boom
hell
hack
dev
lol
pro
```
as you can see `dups.txt` contains many `duplicate strings` so lets run `dupremove` and see what will be the ouput.

This is the output after runing: `cat dups.txt | dupremove` 
```
┌──(root💀devansh)-[~]
└─# cat dups.txt | dupremove 
hack
lol
fake
dev
hell
boom
pro
```
