'''
Created on Feb 15, 2011, modified on Feb 26 2011
Version 3.0 on Feb 5, 2013

@author: ola
@change: Revised on Feb 4, 2013 by iosk
@author: JIMMY GUO
'''


import tkFileDialog, os
import copy


''' In this section we define the specific transform functions
    These functions should apply the respective transformation to one word only
    That means that their argument should be the 'to be transformed' word 
    and their return value should be the transformed word'''
def transform_identity(word):
    return word

def transform_upper(word):
    return word.upper()

def transform_pig(word):
    if "aeiouAEIOU".count(word[0]) > 0:
        return word + "-way"
    if word[0] == 'q' or word[0] == 'Q':
        return word[2:] + "-quay"
    for i in range(0, len(word)):
        if "aeiouAEIOU".count(word[i]) > 0:
            return word[i:] + "-" + word[:i] + "ay"
    return word + "-way"

def transform_rot13(word):
    alphabet = "abcdefghijklmnopqrstuvwxyz" * 2
    capitalAlphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" * 2
    wordtoTransform = list(word)
    output = ""
    
    for letter in wordtoTransform:
        if alphabet.count(letter)!=0:
            letter = alphabet[alphabet.find(letter) + 13]
        if capitalAlphabet.count(letter)!=0:
            letter = capitalAlphabet[capitalAlphabet.find(letter) + 13]
        output += letter
        
    return output

'''This function opens a file and returns a file descriptor which we will use to read our input.'''
def get_file_to_open():
    """
    prompt for existing file, return the file (open for reading)
    """
    datadir = os.getcwd() + "/../data/"
    fileRef = tkFileDialog.askopenfile(title="choose a file",
                                    initialdir=datadir)
    return fileRef

'''This function opens a dialog and the user chooses a file to write to.
    It returns a file descriptor which we have to use to write on that file.'''
def get_file_to_save():
    """
    prompt for new file, user enters name, return file (open for writing)
    """
    fileRef = tkFileDialog.asksaveasfile(title="save file")
    return fileRef


''' This function reads a file and returns a list of lists:
    Each element of the list corresponds to a line of the file
    Each element of the nested lists corresponds to a word in that line.'''
def get_words(fileRef):
    words = fileRef.readlines()  
    return [w.split() for w in words]


''' This function is used for users to make a choice between the available transformations '''
def choose_transform():
    
    # Create a list that contains the names of all the functions available for transformations
    funcs = [transform_identity, transform_upper, transform_pig, transform_rot13]

    # We print all functions that are available
    for i, func in enumerate(funcs):
        print "%d\t%s" % (i + 1, func.__name__)


    print "enter choice> ",
    choice = int(raw_input())

    if 0 < choice <= len(funcs):
        return funcs[choice - 1]

    return None


''' This is the heart of our program. 
    This function takes as an argument  a list of lists that contains all the original words
    and a string dictating which transformation to apply on these words.'''
# TODO: expand the code so that the 'func' argument dictates which functionality is performed.
def transform(lines, func):
    cpy = copy.deepcopy(lines)  # this makes a copy
    # We explicitly use deepcopy() because "lines" is a list of lists.

    transformedText = ""
    
    for i in range(0, len(cpy)):
        for j in range(0, len(cpy[i])):
            cpy[i][j] = func(cpy[i][j])
            
    # TODO: Each word in cpy must be transformed by the 'func' (= an argument that ends up being one 
    # of the transform functions ). Example: changedWord = func( wordToBeChanged )
    
    return cpy


'''This function writes the words found in the 'words' list to the Eclipse terminal. '''
def write_words(fd, words):
    """
    words is a list of lists,
    each sublist represents a line to write
    (e.g., of transformed words)
    file is a file open for writing
    write each sublist to the file
    with words on a line separated by whitespace
    and each sublist of words on a line
    """
    
    for line in words:
        for w in line:
            fd.write(w + " ")
        fd.write("\n")
    
    fd.close()

def transform_file():

    # We open the fileRef, and get all its words with the get_words() function
    fileRef = get_file_to_open()
    if fileRef == None:
        return
    words = get_words(fileRef)
    fileRef.close()
    
    # We choose a functionality that we will apply to the words.
    func = choose_transform()
    if func == None:
        return
    
    # Apply the transformation
    transformed_words = transform(words, func)
    print "transform done, save fileRef"
    
    # Save the transformed_words to a new fileRef
    fileRef = get_file_to_save()
    if fileRef == None:
        return
    write_words(fileRef, transformed_words)
    fileRef.close();

'''When you run the module this line will be picked out and the function 
    written under __main__": will always be executed.
    That is how you 'tell Python' where to start. '''
if __name__ == "__main__":
    transform_file()


