'''
Created on Mar 2, 2013

@author: Jimmy
'''
def countVisible(trophies):
    
    visible = 1
    
    currentTrophyHeight = trophies[0]
    
    for i in range(1,len(trophies)):
        if currentTrophyHeight < trophies[i]:
            visible += 1
            currentTrophyHeight = trophies[i]
    
    reverseTrophies = trophies[::-1]
    
    reverseVisible = 1
    
    currentReverseTrophyHeight = reverseTrophies[0]
    
    for i in range(1,len(reverseTrophies)):
        if currentReverseTrophyHeight < reverseTrophies[i]:
            reverseVisible += 1
            currentReverseTrophyHeight = reverseTrophies[i]
            
    return [visible,reverseVisible]
            