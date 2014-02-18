'''
Created on Feb 9, 2013

@author: Jimmy
'''
def maxPoints(toss) :
    scorelist = []
    for element in toss:
        scorelist.append(toss.count(element)*element)
    return max(scorelist)
        