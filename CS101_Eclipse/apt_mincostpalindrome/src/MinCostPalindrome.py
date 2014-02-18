'''
Created on Feb 9, 2013

@author: Jimmy
'''
def getMinimum(s, oCost, xCost):
    cost = 0
    reversestring = s[::-1]
    for i in range(0,len(s)):
        if s[i] != reversestring[i]:
            if s[i] != "?" and reversestring[i] != "?":
                return -1
            if s[i] == "?":
                if reversestring[i] == "o":
                    cost += oCost
                elif reversestring[i] == "x":
                    cost += xCost
#            if reversestring[i] == "?":
#                if s[i] == "o":
#                    cost += oCost
#                elif s[i] == "x":
#                    cost += xCost

        elif s[i] == reversestring[i]:
            if s[i] == "?":
                cost += min(oCost,xCost)
    return cost
        