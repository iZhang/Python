'''
Created on Feb 25, 2013

@author: Jimmy
'''
def encrypt(str):
    alphabet = "abcdefghijklmnopqrstuvwxyz" * 2
    capitalAlphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" * 2
    strtoTransform = list(str)
    output = ""
    
    for letter in strtoTransform:
        if alphabet.count(letter)!=0:
            letter = alphabet[alphabet.find(letter) + 13]
        if capitalAlphabet.count(letter)!=0:
            letter = capitalAlphabet[capitalAlphabet.find(letter) + 13]
        output += letter
        
    return output