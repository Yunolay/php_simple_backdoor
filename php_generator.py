#!/usr/bin/env python3
import os

extensions = ['.php', '.pht', '.phtm', '.phtml', '.phar', '.phpt', '.pgif', '.phps', '.phtml', '.php2', '.php3', '.php4', '.php5', '.php6', '.php7', '.php16', '.inc']

def main():
    f = open('intruder_php_backdoor_wordlist.txt', 'r')
    for i, line in enumerate(f):
        for ext in extensions:
            line = line.replace(ext, '')
            p = open(f'shell/shell_{i}{ext}', 'w')
            p.write(line)

if __name__ == '__main__':
    main()