'''
Created on Jan 28, 2013

@author: Jimmy
'''
def numberTimesAppear(number,digit):
    count = 0
    count = str(number).count(str(digit))
    return count