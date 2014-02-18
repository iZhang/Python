'''
Created on Jan 28, 2013

@author: Jimmy
'''
def acronym(phrase):
    result = ""
    for word in phrase.split():
        result += word[0]
    return result