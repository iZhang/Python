'''
Created on Mar 2, 2013

@author: Jimmy
'''
def maximumFacts(suspects):
    happymeal = [suspect.split(",") for suspect in suspects]
    
    maximumFries = 0
    
    for i in range(0, len(happymeal)):
        for j in range(0,len(happymeal)):
            if i != j:
                if maximumFries < len(set(happymeal[i]) & set(happymeal[j])):
                    maximumFries = len(set(happymeal[i]) & set(happymeal[j]))
            
    return maximumFries
        