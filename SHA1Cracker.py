#!/usr/bin/python3

import hashlib
from termcolor import colored
from urllib.request import urlopen

sha1hash = input(colored('[*] Enter the SHA-1 Hash: ', 'blue'))
passlist = str(urlopen('http://localhost/passwords.txt').read(), 'utf-8')

for i in passlist.split('\n'):
    hashguess = hashlib.sha1(bytes(i, 'utf-8')).hexdigest()

    if hashguess == sha1hash:
        print(colored(f'[+] The password is: {i}', 'green'))
        quit(0)
    else:
        print(colored('[-] No match, trying next...', 'red'))

print(colored('\n[-] Failed to crack the hash.', 'red'))
