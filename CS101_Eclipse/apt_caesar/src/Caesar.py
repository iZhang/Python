'''
Created on Mar 27, 2013

@author: Jimmy
'''
def decode(cipher, shift):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    return "".join([alphabet[alphabet.index(letter,25)-shift] for letter in cipher])