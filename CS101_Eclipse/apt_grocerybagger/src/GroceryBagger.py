'''
Created on Apr 3, 2013

@author: Jimmy
'''
import math

def minimumBags(strength, itemType):
    
    dictionary = {}
    bagsRequired = 0
    
    for type in itemType:
        dictionary[type] = dictionary.get(type,0) + 1
        
    for key in dictionary.keys():
        bagsRequired += math.ceil(dictionary.get(key)/float(strength))

    return int(bagsRequired)
    
print minimumBags(2,["DAIRY","DAIRY","PRODUCE","PRODUCE","PRODUCE","MEAT"])
        
    
    
    