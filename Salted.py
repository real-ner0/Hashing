#!/usr/bin/python3

import crypt
from termcolor import colored


def crackPwd(words):
    salt = words[:2]
    dictionary = open('dict.txt', 'r')
    for word in dictionary.readlines():
        word = word.strip('\n')
        cryptPass = crypt.crypt(word, salt)
        if cryptPass == words:
            print(colored(f'[+] Password Found: {word}\n', 'green'))
            return

    print(colored('[-] Password not found...!\n', 'red'))
    return


def main():
    passfile = open('pass.txt', 'r')

    for line in passfile.readlines():
            if ':' in line:
                user = line.split(':')[0]
                cryptword = line.split(':')[1].strip(' ').strip('\n')
                print(colored(f'[*] Cracking password for: {user}', 'yellow'))
                crackPwd(cryptword)

main()