#!/usr/bin/env python3
import os

def main():
    f = open('intruder_php_backdoor_wordlist.txt', 'r')
    for i, line in enumerate(f):
        p = open(f'shell_{i}.php', 'w')
        p.write(line)

if __name__ == '__main__':
    main()