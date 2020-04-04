import hashlib
import urllib.request

from termcolor import colored
#bruteforcing
sha1hash = input("Enter sha1 hash value :")


#74a871acbf060dda5fc7260d05a5924a34e4c0e7

passlist = str( urllib.request.urlopen('https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-1000.txt').read(),'utf-8')
print(passlist)
for password in passlist:
    hashguess = hashlib.sha1(bytes(password,'utf-8')).hexdigest()
    if hashguess == sha1hash:
        print(colored("the password is : +" +str(password),'green'))
        quit()

    else:
        print(colored("[-] password guess " + str(password) +"does not match  trying next", 'red'))





