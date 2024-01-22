#!/usr/bin/env python3
import os

def main():
    for i, line in enumerate(open('intruder_php_backdoor_wordlist.txt', 'r')):
        for ext in open('extensions_list.txt', 'r'):
            ext = ext.strip()
            
            p = open(f'shell/shell_{i}{ext}', 'w')
            p.write(line)
            p.close()
            
            print(f'[*] Generated shell_{i}{ext} to shell directory.')

            f = open(f'filename_list.txt', 'a')
            f.write(f'shell_{i}{ext}\n')
            f.close()

            print(f'[*] Appended shell_{i}{ext} to filename_list.txt.')
            
            

if __name__ == '__main__':
    main()