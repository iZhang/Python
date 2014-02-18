'''
Created on Feb 25, 2013

@author: Jimmy
'''
def theMin(room):
    numChanges = 0
    letter = room[0]
    for i in range(1,len(room)):
        if letter == room[i]:
            letter = "X"
            numChanges += 1
        else:
            letter = room[i]
            
    return numChanges