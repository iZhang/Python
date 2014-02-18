'''
Created on Apr 2, 2013

@author: Jimmy
'''
def getWinner(events):
    dictionary = {}
    for contestant in events:
        dictionary[contestant] = dictionary.get(contestant,0) + 1
    maximum = max(dictionary.values())
    
    dictionary = {}
    for contestant in events:
        dictionary[contestant] = dictionary.get(contestant,0) + 1
        if dictionary[contestant] == maximum:
            return contestant