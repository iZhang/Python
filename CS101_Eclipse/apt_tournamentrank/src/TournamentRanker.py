'''
Created on Apr 3, 2013

@author: Jimmy
'''
import operator

def rankTeams(names,lostTo):
    d = {}
    for team in names:
        d[team] = d.get(team,[0,0])
        #number of opponents beaten, number of opponents that their defeater beat
    
    for team in lostTo:
        if team in d:
            d[team][0] += 1   
        
    for i,val in enumerate(lostTo):
        if lostTo[i] in d:
            d[lostTo[i]][1] += d[names[i]][0]
    
    print d
            
    x = sorted(d.items(),key=lambda(k,v):operator.itemgetter(1)(v),reverse=True)
    y = sorted(x,key=lambda(k,v):operator.itemgetter(0)(v),reverse=True)
    
    list = []
    for thing in y:
        list.append(thing[0])
        
    return list

print rankTeams(['DUKE', 'SETON HALL', 'ILLINOIS', 'CINCINNATI', 'NORTH CAROLINA', 'TEXAS', 'XAVIER', 'MISSISSIPPI STATE'], ['', 'DUKE', 'DUKE', 'ILLINOIS', 'TEXAS', 'XAVIER', 'DUKE', 'XAVIER'])
        