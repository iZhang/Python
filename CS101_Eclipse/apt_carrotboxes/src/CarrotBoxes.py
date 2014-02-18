'''
Created on Feb 25, 2013

@author: Jimmy
'''
def theIndex(carrots,amount):
    while amount > 0:
        if amount - 1 == 0:
            return carrots.index(max(carrots))
        carrots[carrots.index(max(carrots))] -= 1
        amount -=1
    return None
    
        
            