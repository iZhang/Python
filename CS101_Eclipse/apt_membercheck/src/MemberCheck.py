'''
Created on Feb 21, 2013

@author: Jimmy
'''
def whosDishonest(club1, club2, club3):
    cheats1 = [x for x in club1 if x in club2 or x in club3]
    cheats2 = [x for x in club2 if x in club1 or x in club3]
    cheats3 = [x for x in club3 if x in club2 or x in club1]
    
    return sorted(set(cheats1) | set(cheats2) | set(cheats3))