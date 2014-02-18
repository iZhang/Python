'''
Created on Apr 3, 2013

@author: Jimmy
'''
import operator

def sort(data):
    dictionary = {}
    for fruit in data:
        dictionary[fruit] = dictionary.get(fruit,0) + 1
    alphabetically = sorted(dictionary.items(),key=operator.itemgetter(0))
    frequency = sorted(alphabetically,key=operator.itemgetter(1),reverse=True)
    
    list = []
    for fruit in frequency:
        list.append(fruit[0])
        
    return list

print sort(["apple", "pear", "cherry", "apple", "pear", "apple", "banana"])
    