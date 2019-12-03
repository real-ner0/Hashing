#!/usr/bin/python3

import hashlib
from termcolor import colored


def tryOpen(list):

    global passwords

    try:
        passwords = open(list, 'r')
    except:
        print(colored('[-] Error reading file. Aborting...', 'red'))
        quit()


md5hash = input(colored('[*] Enter the MD5 Hash: ', 'blue'))
wordlist = input(colored('[*] Enter the path to wordlist: ', 'blue'))

tryOpen(wordlist)

for passw in passwords:
    print("[*] Trying " + passw.strip('\n') + '... ')
    enc_word = passw.encode('utf-8')
    md5digest = hashlib.md5(enc_word.strip()).hexdigest()

    if md5digest == md5hash:
        print(colored(f'[+] Password Found: {passw}', 'green'))
        quit()

print(colored('\n[!] Password not in the list...!', 'red'))
