'''
Created on Feb 7, 2013

@author: Jimmy
'''
def lovely(ingrediants,inedible):
    ingrediantslist = ingrediants.split()
    inediblelist = inedible.split()
    return len([s for s in ingrediantslist if s not in inediblelist])
    