#!/usr/bin/python3

import hashlib
from termcolor import colored


plaintext = input(colored('[*] Enter plain text: ', 'blue'))
print()

# Calculate MD5 Hash
hashmd5 = hashlib.md5()
hashmd5.update(plaintext.encode())

# Calculate SHA-1 Hash
hashsha1 = hashlib.sha1()
hashsha1.update(plaintext.encode())

# Calculate SHA-224 Hash
hashsha224 = hashlib.sha224()
hashsha224.update(plaintext.encode())

# Calculate SHA-256 Hash
hashsha256 = hashlib.sha256()
hashsha256.update(plaintext.encode())

# Calculate SHA-512 Hash
hashsha512 = hashlib.sha512()
hashsha512.update(plaintext.encode())

print(colored(f'[+] MD5 Hash:         {hashmd5.hexdigest()}', 'green'))
print(colored(f'[+] SHA-1 Hash:       {hashsha1.hexdigest()}', 'green'))
print(colored(f'[+] SHA-224 Hash:     {hashsha224.hexdigest()}', 'green'))
print(colored(f'[+] SHA-256 Hash:     {hashsha256.hexdigest()}', 'green'))
print(colored(f'[+] SHA-512 Hash:     {hashsha512.hexdigest()}', 'green'))