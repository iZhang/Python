'''
Created on Jan 28, 2013

@author: Jimmy
'''
def bagelCount(orders):
    total = 0
    for order in orders:
        total += order + order/12
    return total