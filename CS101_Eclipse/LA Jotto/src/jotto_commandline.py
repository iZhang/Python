'''
Created on March 27,2011

@author: ola
'''
 
import jotto_model

def run_game():
    wlen = jotto_model.load_words()
    print "Playing a game with ",wlen," letter words"
    numLeft = jotto_model.start_game()
    print "Number of words is ",numLeft
    
    while True:
        word = jotto_model.get_guess()
        print "My guess is '"+word+"', how many letters does it have in common with your word: ",
        common = int(raw_input())
        if common == 6:
            print "I win! It took me",
            print jotto_model.guess_count(),"guesses!"
            break
    
        numLeft = jotto_model.process_common_last(common)
        print "Number of words left is",numLeft
        if numLeft == 0:
            print "An error was made, I have no more words to guess."
            break
        
if __name__ == "__main__":
    run_game()
