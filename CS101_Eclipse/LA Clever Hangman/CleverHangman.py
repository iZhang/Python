'''
Created on Feb 23, 2012

@author: ola
'''
import Tools, random, operator, copy

_DEBUGisON = False

def change_knowledge(guess, secret, knowledge):
    """ Changes the knowledge that is shown to the player
        For example changes  _ e _ _ e  to  t e _ _ e  when t is guessed.
    """
    for i, ch in enumerate(secret):
        if ch == guess and knowledge[i] == '_':
            knowledge[i] = ch
    return knowledge

def display(guesses, knowledge):
    """ This function print information to the human player. """
    print "Guesses so far:", guesses
    print "Your knowledge so far:"
    print ' '.join(knowledge)

def play_game():
    global _DEBUGisON
    while True:
        try:
            sec_length = int(raw_input("Please enter the number of letters you would like in your word:"))
            whole_list = Tools.get_words("lowerwords.txt", sec_length)
            secret = random.choice(whole_list)
            break
        except ValueError:
                    print "Please enter a valid number."
        except IndexError:
                    print "Sorry there are no words of that length. Please try another number."
    
    knowledge = ["_"] * len(secret)
    guesses = []  # letters guessed so far
    misses = 0  # misses made so far
    while True:
        try:
            misses_allowed = int(raw_input("Please enter the number of guesses you would like:"))
            if misses_allowed > 0 and misses_allowed < 27:
                break
            else:
                print "Please enter a number between 1 and 26."
        except ValueError:
            print "Please enter a valid number."
    
    while misses < misses_allowed:
        display(guesses, knowledge)
        print "Guesses left: ", misses_allowed - misses
        if _DEBUGisON: print "   (Secret word is", secret.upper(), ")" + " # words possible:",len(whole_list)
        
        while True:
            try:
                guess = raw_input("Please guess a letter:").lower()
                if guess in ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']:
                    pass
                    if guess not in guesses:
                        break
                    else:
                        print ""
                        print "You already guessed that!"
                        display(guesses, knowledge)
                else:
                    print ""
                    print "Please enter a valid letter."
                    display(guesses, knowledge)
            except None:
                pass
                      
        print ""
       
        new_whole_list = []
        new_whole_list2 = []
        d = {}
        for word in whole_list:
            if guess in word:
                new_whole_list.append(word)
            if guess not in word:
                new_whole_list2.append(word)
        
        if len(new_whole_list) > len(new_whole_list2):
            knowledgeCopy = knowledge[:]
            for word in new_whole_list:
                for i in range(0, sec_length):
                    if word[i] == guess:
                        knowledgeCopy[i] = guess
                d["".join(knowledgeCopy)] = d.get("".join(knowledgeCopy), [])
                d.get("".join(knowledgeCopy), []).append(word)
                knowledgeCopy = knowledge[:]
            new_whole_list = sorted(d.items(), key=lambda x: len(x[1]), reverse=True)[0][1]
        
        if len(new_whole_list) > len(new_whole_list2):
            print "You guessed a letter!"
            whole_list = new_whole_list
            secret = random.choice(whole_list)
            knowledge = change_knowledge(guess, secret, knowledge)
            
        else:
            print "Sorry, there are no " + guess + "'s."
            misses = misses + 1
            whole_list = new_whole_list2
            secret = random.choice(whole_list)
            
        guesses.append(guess) 
        if not '_' in knowledge:
            print "Congratulations. You guessed my word:",secret
            break
          
        if misses == misses_allowed:
            print "Game over. You lose. The secret word was", secret + "."
            break

if __name__ == '__main__':
    play_game()
