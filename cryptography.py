"""
cryptography.py
Author: Hagin Onyango
Credit: Living Sources around me

Assignment:

Write and submit a program that encrypts and decrypts user data.

See the detailed requirements at https://github.com/HHS-IntroProgramming/Cryptography/blob/master/README.md
"""
associations = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .,:;'\"/\\<>(){}[]-=_+?!"




def encrypt(string, key, method):
    messageNumber = [associations.find(a) for a in string]
    keyNumber = [associations.find(a) for a in key] 
    keyNumber = keyNumber*(len(messageNumber)//len(keyNumber))+ keyNumber[:len(messageNumber)%len(keyNumber)]
    keyNumber = [method*a for a in keyNumber]
    nxtMessage = [sum(x) for x in zip(messageNumber, keyNumber)]
    nxtMessage = ''.join([associations[x%len(associations)] for x in nxtMessage])
    print(nxtMessage)
    
pressKeys = input("Enter e to encrypt, d to decrypt, or q to quit: ")

while method != "q":
    if method == "e":
        string = input("Message: ")
        key = input("Key: ")
        encrypt(string, key, 1)
    elif method =="d":
        string = input("Key: ")
        encrypt(message, key, -1)
    else:
        print("Did not understand command, try again.")
    method = input("Enter e to encrypt, d to decrypt, or q to quit: ")
    if method == "q":
        print("GoodBye!")
        


