'''
Created on Feb 25, 2013

@author: Jimmy
'''
def whichOrder(available, orders):
    dummy = 0
    for i in range(0,len(orders)):
        if set(orders[i].split()).issubset(set(available)) == True:
            return i
    return -1