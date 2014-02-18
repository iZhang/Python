'''
Created on Oct 15, 2010
Modified on March 13, 2012

@author: JIMMY GUO
'''
import random

_compGuess = ""
_guessCount = 0
_wordlist = []
_possiblewords = []

#---------------------------------

def load_words(filename="kwords5.txt"):
    """
    Given the name of a file that contains a list of words, 
    one per line and all the same length, read the contents 
    of the file into a list of strings.
    Returns length of the words contained in the file
    """
    global _wordlist
    file = open(filename)
    _wordlist = [ word.strip() for word in file ]
    file.close()
    return len(_wordlist[0])
    
def start_game():
    """
    Set up any state that your code needs to play the game. 
    This includes initializing _possiblewords as a copy
    of all the words in _wordlist. You will also need
    to initialize other state needed when a new game starts.
    For example, you could create an empty list to represent the guesses made 
    during a game (the list would be added to by other functions in the
    module).
    Returns number of words the secret word could be.
    """
    global _wordlist, _possiblewords, _guessCount
    _guessCount = 0
    if len(_wordlist) == 0:
        load_words()
    _possiblewords = _wordlist[:]
    return len(_possiblewords)


def get_guess():
    """
    Choose a random word from _possiblewords, remove it from
    _possiblewords so it won't be guessed again, and return it.
    Update all state needed to indicate a guess has been made.
    """
    global _possiblewords, _compGuess, _guessCount
    
    _compGuess = random.choice(_possiblewords)
    
    _possiblewords.remove(_compGuess)
    
    _guessCount += 1
    
    return _compGuess

    
def process_common_last(common):
    """
    common is the number of letters in common between the secret word, known
    by the human player and the computer's last guess. 
    Using this information reduce the list _possiblewords to contain only
    words that contain the proper number of letters in common with the last guess
    Returns number of words remaining that could be secret word, e.g., the new
    length of _possiblewords
    """
    
    global _possiblewords
    global _compGuess
    
    removeList = []
    
    for word in _possiblewords:
        if commonCount(word,_compGuess) != common:
            removeList.append(word)
    
    for word in removeList:
        _possiblewords.remove(word)
    
    return len(_possiblewords)

def guess_count():
    """
    Returns the number of guessed made by the computer since a new
    game was started
    """
    return _guessCount

def commonCount(a,b):
    """
    Returns number of letters in common between given strings a and b,
    no matter where those letters occur within the strings
    """
    alist = list(a)
    blist = list(b)
    for c in alist:
        if c in blist:
            blist[blist.index(c)] = '*'
    return blist.count("*")
            
