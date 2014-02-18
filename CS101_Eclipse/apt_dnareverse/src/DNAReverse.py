'''
Created on Jan 31, 2013

@author: Jimmy
'''
def reverse(dna):
    reverselist = []
    result = ""
    for i in range(0,len(dna)):
        reverselist.append(dna[i])
    reverselist.reverse()
    
    for i in range(0,len(reverselist)):
        result += reverselist[i]
    return result
    