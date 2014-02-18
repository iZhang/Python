'''
Created on Feb 9, 2013

@author: Jimmy
'''
def minDistance(keyboard,word):
    distance = 0
    if len(word) >= 2:
        for i in range(1,len(word)):
            distance += abs(keyboard.find(word[i-1]) - keyboard.find(word[i]))
    return distance