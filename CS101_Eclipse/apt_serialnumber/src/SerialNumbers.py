'''
Created on Mar 27, 2013

@author: Jimmy
'''
import operator

def sortSerials(numbers):
    sums = []
    for number in numbers:
        value = 0
        for num in number:
            if "123456789".find(num) > -1:
                value = value + int(num)
        sums.append((number,len(number),value))            
    x = sorted(sums,key=operator.itemgetter(0))
    y = sorted(x,key=operator.itemgetter(2))
    z = sorted(y,key=operator.itemgetter(1))
    return [a[0] for a in z]