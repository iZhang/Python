'''
Created on Feb 9, 2013

@author: Jimmy
'''
def coins(pence):
    pounds = pence/240
    shillings = (pence%240)/12
    pennies = (pence%240)%12
    return [pounds, shillings, pennies]