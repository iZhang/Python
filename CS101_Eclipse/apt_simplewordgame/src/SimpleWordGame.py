'''
Created on Mar 2, 2013

@author: Jimmy
'''
def points(player, dictionary):
    return sum([len(w)**2 for w in dictionary if w in player])