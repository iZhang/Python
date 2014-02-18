'''
Created on Feb 21, 2013

@author: Jimmy
'''
def assignNumbers(numbers,howMany,slots):
        
    total = sum(howMany[i]*len(str(val)) for i,val in enumerate(numbers))
    
    saved = [howMany[i] * len(str(val)) - 2*howMany[i] for i,val in enumerate(numbers)]
    
    saved.sort()
    
    saved_presses = saved[-slots:]
    
    dummy = 0
    for i in range(0,len(saved_presses)):
        dummy += saved_presses[i]
    
    return (total - dummy)