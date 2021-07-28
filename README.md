# dupremove
dupremove is a multithreaded tool that reads file from `stdin` and removes all the duplicate `strings`, `integers` and lot more.

[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![GitHub release](https://img.shields.io/github/release/DevanshRaghav75/dupremove.svg)](https://GitHub.com/DevanshRaghav75/dupremove/releases/)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)
[![Open Source Love svg1](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[![GitHub license](https://img.shields.io/github/license/DevanshRaghav75/dupremove.svg)](https://github.com/DevanshRaghav75/dupremove/blob/master/LICENSE.md)

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
┌──(root💀devansh)-[~]
└─# cat dups.txt
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
