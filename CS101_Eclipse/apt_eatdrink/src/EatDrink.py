'''
Created on Apr 3, 2013

@author: Jimmy
'''
import operator

def winners(data):
    dictionary = {}
    for y in data:
        x = y.split()
        if x[0] not in dictionary:
            dictionary[x[0]] = [0,0]
        dictionary[x[0]][0] += int(x[1].split(":")[0])*60 + int(x[1].split(":")[1])
        dictionary[x[0]][1] += 1
        
        #dictionary[name] = [time,number of tasks completed]

    timeSorted = sorted(dictionary.items(),key=lambda (k,v): v[0])
    taskSorted = sorted(timeSorted,key=lambda (k,v): v[1],reverse=True)
    
    list=[]
    for element in taskSorted:
        list.append(element[0])
  
    return list

print winners(['owen 2:00', 'jeff 1:29', 'owen 1:00', 'jeff 1:30', 'robert 0:21'])