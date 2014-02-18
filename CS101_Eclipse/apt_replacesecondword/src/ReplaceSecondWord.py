'''
Created on Feb 9, 2013

@author: Jimmy
'''
def replace(phrase, repword, newword):
    phraselist = []
    for character in phrase:
        phraselist.append(character)
    secondoccuranceindex = phrase.find(repword,phrase.find(repword)+1)
    phraselist[secondoccuranceindex:secondoccuranceindex+len(repword)] = newword
    return "".join(phraselist)