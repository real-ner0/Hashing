*** VIEW IN RAW ***

* Hashing
Contains some scripts which are able to generate and break hashes...:)

Usages:

#1. Hasher.py
  Got ability to convert the entered plaint text to MD5, SHA-1, SHA-224, SHA-256 and SHA-512
  
  root@kali:~# python3 Hasher.py
  [*] Enter plain text: P4ssw0rd!

  [+] MD5 Hash:         8ae1dd156c62f4f0b0b31c29b46f8e48
  [+] SHA-1 Hash:       5fd9a568bde954fe6331ef16762584310158fc0d
  [+] SHA-224 Hash:     aa0a79aa7e3a2fd03ed22ecf40885d03d3faaa06b393896f709ce524
  [+] SHA-256 Hash:     45279bbc6ff0112676b4b840a495a19633f54077c8dbc8e182f37f7b96acb7cf
  [+] SHA-512 Hash:     a5b6c33382f2f1cddbfbaba65f2b892b193fa6361d481d8a12229a2d6d95d9b792f6204ea96e706fe6d6914d7f083a213706972e5831e1c7e2cf3c33642a2df9


-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


#2. MD5Cracker.py
  Can crack MD5 hashes. Requires a passwords.txt list.
  
  root@kali:~# python3 MD5Cracker.py 
  [*] Enter the MD5 Hash: e2fc714c4727ee9395f324cd2e7f331f
  [*] Enter the path to wordlist: passwords.txt
  
  [*] Trying 111111... 
  [*] Trying 123456... 
  [*] Trying 12345678... 
  [*] Trying 1qaz2wsx... 
  [*] Trying 2003... 
  [*] Trying 2008... 
  [*] Trying 95... 
  [*] Trying 98... 
  [*] Trying abc... 
  [*] Trying abcd... 
  [+] Password Found: abcd


-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


#3. SHA1Cracker.py
  Can crack SHA-1 Hashes. This script has the ability to load the password list from an URL. I hosted the password list on my
  localhost while creating this, however you could change the URL in the code or completely re-write the code to read from the
  file.

  root@kali:~# python3 SHA1Cracker.py 
  [*] Enter the SHA-1 Hash: 81fe8bfe87576c3ecb22426f8e57847382917acf
  
  [-] No match, trying next...
  [-] No match, trying next...
  [-] No match, trying next...
  [-] No match, trying next...
  [-] No match, trying next...
  [-] No match, trying next...
  [-] No match, trying next...
  [+] The password is: abcd



-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


#4. Salted.py
  Uses the crypt module of python (which uses a Modified-DES Algo to calculate hashes) to break hashes. Need to give location of
  the dictionary.txt and password.txt.
  Here the pass.txt has this format:
    root:hash
    admin:hash
    someone:hash
    anotherone:hash
    user:hash ... and so on
  
  dict.txt contains password in plain text.
  
  root@kali:~# python3 Salted.py 
  [*] Cracking password for: root
  [-] Password not found...!

  [*] Cracking password for: admin
  [-] Password not found...!

  [*] Cracking password for: password
  [-] Password not found...!

  [*] Cracking password for: heelloo
  [-] Password not found...!

  [*] Cracking password for: root
  [+] Password Found: password

  [*] Cracking password for: none
  [-] Password not found...!

  [*] Cracking password for: right
  [-] Password not found...!

-----------x----------------------x-------------------x-------------------x--------------------x---------------x-------------x--
  
