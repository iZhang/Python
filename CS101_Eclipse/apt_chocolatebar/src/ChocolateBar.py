'''
Created on Feb 25, 2013

@author: Jimmy
'''
def maxLength(letters):
    
    barlengths = []
    
    for i in range(0,len(letters)):
        for j in range(i,len(letters)):
            testletters = letters[i:j+1]
            
            if len(set(testletters)) == len(testletters):
                barlengths.append(len(testletters))
                
    return max(barlengths)


