'''
Created on Apr 3, 2013

@author: Jimmy
'''
def documentAccess(records, userGroups, roomRights):
    documents = 0
    list = []
    for y in records:
        x = y.split()
        if x[1] in roomRights and x[2] in userGroups and x[0] not in list:
            documents += 1
            list.append(x[0])
    
    return documents