'''
Created on Feb 28, 2013

@author: Jimmy
'''
def encrypt(numbers) :
    numbers = sorted(numbers)
    numbers[0] += 1
    product = 1
    for value in numbers:
        product *= value
    return long(product)