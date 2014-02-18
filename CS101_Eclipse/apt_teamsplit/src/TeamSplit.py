'''
Created on Mar 27, 2013

@author: Jimmy
'''
def difference(strengths):
    strengths.sort()
    firstTeam = 0
    secondTeam = 0
    for i in range(0,len(strengths)):
        if i%2 == 0:
            firstTeam += strengths[i]
        elif i%2 == 1:
            secondTeam += strengths[i]
    return abs(firstTeam - secondTeam)
        