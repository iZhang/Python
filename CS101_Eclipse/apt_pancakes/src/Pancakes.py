'''
Created on Jan 28, 2013

@author: Jimmy
'''
def minutesNeeded (numCakes, capacity):
    if numCakes % capacity==0:
        return (numCakes/capacity)*10
    if numCakes % capacity > capacity/2:
        return int(numCakes/capacity)*10+10
    if numCakes % capacity <= capacity/2:
        return int(numCakes/capacity)*10+5