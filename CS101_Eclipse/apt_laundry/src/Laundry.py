'''
Created on Jan 28, 2013

@author: Jimmy
'''
def minutesNeeded(m):
    if m == 0:
        return 0
    elif m == 1:
        return 60
    elif m > 1:
        return 60 + (m-1)*25