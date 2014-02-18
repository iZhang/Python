'''
Created on Feb 9, 2013

@author: Jimmy
'''
def numberUnique(zoos):
    animals = []
    
    for element in zoos:
        animals += element.split()

    uniquezoos = 0
    uniqueanimals = 0
    for element in zoos:
        for i in range(0,len(element.split())):
            if animals.count(element.split()[i]) == 1:
                uniqueanimals += 1
        if uniqueanimals >= 1:
            uniquezoos += 1
        uniqueanimals = 0
                
    return uniquezoos
                