'''
Created on Mar 1, 2013

@author: Jimmy
'''
def getFortunate(a,b,c):
    fortunateNums = []
    for one in a:
        for two in b:
            for three in c:
                if str(one+two+three).count('5') + str(one+two+three).count('8') == len(str(one+two+three)):
                    fortunateNums.append(one+two+three)
    return len(set(fortunateNums))