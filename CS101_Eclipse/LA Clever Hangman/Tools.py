'''
Created on Jan 21, 2011

Modified on Feb 22, 2012, remove use
of dictionaries and read file by lines
rather than by words --- this will
make it easier to use non-words, i.e.,
lines like "Animal Farm" or "Jackson Pollock" 
if startUp wants to guess books or artists or ... 

Modified on October 7, 2012, now a source for copying
code rather than calling code in this module

Modified April 16 2013, Lorensen. 
@author: ola
'''
import random

_DEBUGisON = True     #Set to False to remove unwanted print lines that are used for debugging.

def load_lines(filename):
    """
    read words from specified file and return a list of
    strings, each string is one line of the file
    """
    lines = []
    f = open(filename)
    for line in f.readlines():
        line = line.strip()
        lines.append(line)
    return lines
    
    
def get_words(filename, wordlength = 5):
    """
    returns a list of words having a specified length from
    the file whose name is filename.
    default length is 5 (if parameter not specified)
    """
    lines = load_lines(filename)
    wlist = [w for w in lines if len(w) == wordlength]
    return wlist

def startUp():
    global _DEBUGisON
    print "what's the word length? ",
    n = int(raw_input())
    words = get_words("lowerwords.txt",n)
    if _DEBUGisON: print "read %d words whose length is %d" % (len(words),n)
    
    one = random.choice(words)  #Handy method in random that pics a random word.  
    
    if _DEBUGisON: print "choosing at random: ",one
    
    list_TOOfew(words)



def list_TOOfew(words):
    """ Prints out the number and the words themselves if 
        there are too few of them. 
        This makes it easier to see what happens when the game is
        about to end.
    """
    if len(words) < 30:
        for i,w in enumerate(words):
            print i,"\t",w

#if __name__ == "__main__":
