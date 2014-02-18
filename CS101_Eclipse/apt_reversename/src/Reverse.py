'''
Created on Feb 25, 2013

@author: Jimmy
'''
def change (name):
    lastname = name.split(",")[0]
    firstname = name.split(",")[1].strip()
    return firstname + " " + lastname