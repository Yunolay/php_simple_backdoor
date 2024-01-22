#!/usr/bin/env python3
import os

def main():
    for i, line in enumerate(open('intruder_php_backdoor_wordlist.txt', 'r')):
        for ext in open('extensions_list.txt', 'r'):
            ext = ext.strip()
            p = open(f'shell/shell_{i}{ext}', 'w')
            p.write(line)
            print(f'[*] Generated shell_{i}{ext} to shell directory.')

if __name__ == '__main__':
    main()