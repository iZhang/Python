'''
Created on Mar 27, 2013

@author: Jimmy
'''
def bestInvitation(first,second):
    interesting = 0
    list = []
    for i in range(0,len(first)):
        for j in range(0,len(first)):
            if first[i] == second[j]:
                interesting += 1
            if first[i] == first[j]:
                interesting += 1
        list.append(interesting)
        interesting = 0
        
    for i in range(0,len(first)):
        for j in range(0,len(first)):
            if second[i] == first[j]:
                interesting += 1
            if second[i] == second[j]:
                interesting += 1
        list.append(interesting)
        interesting = 0        
        
    return max(list)
                    
        