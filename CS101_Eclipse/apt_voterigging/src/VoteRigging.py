'''
Created on Mar 27, 2013

@author: Jimmy
'''
def minimumVotes(votes):
    votesBought = 0
    firstCandidate = votes[0]
    
    del votes[0]
    
    if len(votes) == 0:
        return 0
    
    while firstCandidate <= max(votes):
        firstCandidate += 1
        votes[votes.index(max(votes))] -= 1
        print votes
        print firstCandidate
        votesBought += 1
    return votesBought