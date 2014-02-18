'''
Created on Mar 27, 2013

@author: Jimmy
'''
def highestScore(friends):
    twofriends = 0
    for i in range(0,len(friends)):
        dummy = []
        for j in range(0,len(friends)):
            if friends[i][j] == 'Y':
                dummy.append(j)    
                for k in range(0,len(friends)):
                    if friends[j][k] == 'Y':
                        dummy.append(k);
        twofriends = max(len(set(dummy)) - 1, twofriends)
    return twofriends;
