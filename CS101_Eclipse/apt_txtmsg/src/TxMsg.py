'''
Created on Jan 31, 2013

@author: Jimmy
'''
def isvowel(letter):
    return "aeiou".count(letter) > 0

def allvowel(word):
    vowelcount = 0
    for letter in word:
        if isvowel(letter):
            vowelcount +=1
    return vowelcount == len(word)

def textize(word):
    if allvowel(word):
        return word
    newmessage = ""
    if not isvowel(word[0]):
        newmessage = word[0]
    for i in range(1,len(word)):
        if not isvowel(word[i]) and isvowel(word[i-1]):
            newmessage += word[i]
    return newmessage 

def getMessage(original):
    newmessage = ""
    for word in original.split():
        newmessage +=" " + textize(word)
    return newmessage.strip()

        