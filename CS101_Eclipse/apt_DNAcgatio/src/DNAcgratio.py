'''
Created on Jan 28, 2013

@author: Jimmy
'''
def ratio(dna):
#     return (dna.count("c") + dna.count("g"))/float(len(dna))

    ccount = 0.0
    gcount = 0
    for ch in dna:
        if ch == "c":
            ccount +=1
        if ch == "g":
            gcount +=1
    return (ccount + gcount)/len(dna)
    