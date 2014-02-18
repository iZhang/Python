'''
Created on Mar 1, 2013

@author: Jimmy
'''
def countall(words):
    
    firstLetters = [w[0].lower() for w in words]
    
    print firstLetters
    
    alliterations = 0
    
    for i in range(0,len(firstLetters)):
        if len(firstLetters) == 1:
            return 0
        if i > 0 and i != len(firstLetters) - 1:
            if firstLetters[i] == firstLetters[i-1] and firstLetters[i] != firstLetters[i+1]:
                alliterations += 1
        if i == len(firstLetters) - 1 and firstLetters[i] == firstLetters[i-1]:
            alliterations += 1
    
    return alliterations