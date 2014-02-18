'''
Created on Feb 28, 2013

@author: Jimmy
'''
def cheat(mine, friend) :
    for val in reversed(sorted(mine)): 
        beatables = [x for x in friend if x < val]
        if(len(beatables)!=0):
            friend.remove(max(beatables))
    return len(mine) - len(friend)