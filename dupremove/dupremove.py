import sys
import threading
from concurrent.futures import ThreadPoolExecutor

cat = sys.stdin

lists = []

def remover():
    for x in cat:
        lists.append(x)

    removed_dups = list(set(lists))

    for i in removed_dups:
        print(i, sep='', end='')

def main():
    with ThreadPoolExecutor(max_workers=100) as executor:
        executor.submit(remover) 