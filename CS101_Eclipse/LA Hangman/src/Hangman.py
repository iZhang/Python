'''
Created on Feb 27, 2013

@author: Jimmy Guo
'''
import random

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
    
    
def get_words(filename, wordlength):
    """
    returns a list of words having a specified length from
    the file whose name is filename.
    default length is 5 (if parameter not specified)
    """
    lines = load_lines(filename)
    wlist = [w for w in lines if len(w) == wordlength]
    return wlist

def playCategory():
    while True:
        category = raw_input("1 - Countries\n2 - Gangster Rap Artists\n3 - No Category\nPlease enter the number of the category you would like to play:")
       
        if int(category)==1:
            return "countries.txt"
            break
        elif int(category)==2:
            return "gangsterrap.txt"
            break
        elif int(category)==3:
            return "lowerwords.txt"
            break
        else:
            print "Please enter '1' '2' or '3'"
    return None
    
def getGuesses():
    
    #Asks user if he would like to specify the number of guesses. 
    #If so, the program makes sure the user enters a number between 1 and 26.
    #If not, the program sets the number of tries to 15.
    
    while True:
        x = raw_input("Would you like to specify the number of guesses you would like? Please enter 'Y' or 'N':").lower()
        if x == 'y': 
            while True:
                try:
                    numGuesses = int(raw_input("How many guesses would you like?"))
                    if numGuesses > 0 and numGuesses < 27:
                        break
                    else:
                        print "Please enter a number between 1 and 26."
                except ValueError:
                    print "Please enter a valid number."
            break
        
        elif x == 'n':
            numGuesses = 15
            break
        
        elif x != 'n' and x != 'y':
            print "Not a valid answer."
    
    return numGuesses

def getLetters(category):
    
    #Asks user if he would like to specify the number of letters in his word. 
    #If so, the program makes sure the user enters a number between the shortest and longest word in the file..
    #If not, the program picks a random word from the file.
    
    numLetters = 0
    secretWord = ""
    
    while True:
        x = raw_input("Would you like to specify the number of letters in your word? Please enter 'Y' or 'N':").lower()
        
        if x == 'y': 
            while True:
                try:
                    numLetters = int(raw_input("How many letters would you like in your word?"))
                    words = get_words(category,numLetters)
                    secretWord = random.choice(words)
#                    print "The word is",secretWord
#                    print "read %d words whose length is %d" % (len(words),numLetters)
                    break
                except ValueError:
                    print "Please enter a valid number."
                except IndexError:
                    print "Sorry there are no words of that length. Please try another number."
            break
        
        if x == 'n':
            words = [w for w in load_lines(category)]
            secretWord = random.choice(words)
            numLetters = len(secretWord)
#            print "choosing at random:",secretWord
            break

        elif x != 'n' and x != 'y':
            print "Not a valid answer."
    
    return numLetters, secretWord
    
def playGame():
    print "Let's play Hangman!"
    
    category = playCategory()

    correctGuesses = set([])
    incorrectGuesses = []

    #Keeping track of the word and what parts of it are displayed to the user.
    (numLetters, secretWord) = getLetters(category)
    underscores = ["_"]*numLetters
    
    #If the word contains spaces or underscores, they are displayed to the user before he guesses.
    
    for i in range(0,len(secretWord)):
        if secretWord[i] == " ":
            underscores[i] = " "
        if secretWord[i] == "-":
            underscores[i] = "-"

    numGuesses = getGuesses()
    numGuesses2 = numGuesses
    
    while numGuesses > 0:
        print " ".join(underscores)
        
        print "Correct Guesses:",
        for element in correctGuesses:
            print element,
        print
        
        print "Incorrect Guesses:",
        for element in incorrectGuesses:
            print element,
        print
        
        print "Guesses Remaining:",numGuesses
        
        while True:
            userGuess = raw_input("Please guess a letter:").lower() 

            if userGuess not in incorrectGuesses and userGuess not in correctGuesses:
                if userGuess in ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']:
                    guess = userGuess
                    break
                else:
                    print "Please enter a valid letter."
                     
                    print " ".join(underscores)
        
                    print "Correct Guesses:",
                    for element in correctGuesses:
                        print element,
                    print
                        
                    print "Incorrect Guesses:",
                    for element in incorrectGuesses:
                        print element,
                    print
                        
                    print "Guesses Remaining:",numGuesses
              
            else:
                print "You already guessed that!"
                
                print " ".join(underscores)
        
                print "Correct Guesses:",
                for element in correctGuesses:
                    print element,
                print
                
                print "Incorrect Guesses:",
                for element in incorrectGuesses:
                    print element,
                print
                
                print "Guesses Remaining:",numGuesses

        if secretWord.lower().find(guess) == -1:
            incorrectGuesses.append(guess)
            numGuesses -= 1
            print "Sorry, there are no " + guess + "'s."
                
        elif secretWord.lower().find(guess) != -1:
            for i in range(0,len(secretWord)):
                if secretWord[i].lower() == guess:
                    underscores[i] = guess
                    correctGuesses.add(guess)
            print "Good guess. The word contains " + str(secretWord.lower().count(guess)) +" " + guess + "(s)."
            
        if "_" not in underscores:
            
            print " ".join(underscores)
        
            print "Correct Guesses:",
            for element in correctGuesses:
                print element,
            print
                
            print "Incorrect Guesses:",
            for element in incorrectGuesses:
                print element,
            print
                
            print "Guesses Remaining:",numGuesses   
            
            print "Congratulations. It took you", numGuesses2 - numGuesses, "lives to guess " + secretWord + "."      
            
            break
        
        if numGuesses == 0:
            print "You have lost. Your word was:",secretWord
            
            print " ".join(underscores)
        
            print "Correct Guesses:",
            for element in correctGuesses:
                print element,
            print
                
            print "Incorrect Guesses:",
            for element in incorrectGuesses:
                print element,
            print
                
            print "Guesses Remaining:",numGuesses
            
            break

if __name__ == "__main__":
    playGame()
    
