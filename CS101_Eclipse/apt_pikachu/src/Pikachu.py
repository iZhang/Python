'''
Created on Feb 25, 2013

@author: Jimmy
'''
def check(word):
    if word.count("pi")*2 + word.count("ka")*2 + word.count("chu")*3 == len(word):
        return "YES"
    else:
        return "NO"
        