'''
Created on Apr 3, 2013

@author: Jimmy
'''
import operator

def freqs(data):
    dictionary = {}
    for fruit in data:
        dictionary[fruit] = dictionary.get(fruit,0) + 1
    alphabetically = sorted(dictionary.items(),key=operator.itemgetter(0))
    
    list = []
    for fruit in alphabetically:
        list.append(fruit[1])
        
    return list

print freqs(["apple", "pear", "cherry", "apple", "cherry", "pear", "apple", "banana"])