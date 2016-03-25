"""
cryptography.py
Author: Hagin Onyango
Credit: Living Sources around me

Assignment:

Write and submit a program that encrypts and decrypts user data.

See the detailed requirements at https://github.com/HHS-IntroProgramming/Cryptography/blob/master/README.md
"""
associations = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .,:;'\"/\\<>(){}[]-=_+?!"




def encrypt(string, key):
    messageNumber = [associations.find(a) for a in message]
    keyNumber = [associations.find(b) for b in key] 
    newvalarr = []
    c = 0
    for x in messageNumber:
        newvalarr.append(x + keyNumber(c))
        c += 1
    return [associations[d] for d in newvalarr]
    
question = input("what is the message?")
questionKey = input("what is the key?")
print(encrypt(question, questionKey))


