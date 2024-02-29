import sys
import random
from rich import print


"""
looks for all the words in certain file
"""
def read_all_words():

    all_words = []

    """
    TODO: 
    write a code that do the following...
    1) checks if any command line arguments present
    2) checks if argument is number between 5 and 8
    3) opens correct file from /collections for reading
    4) reads all words in list
    
    raises ValueError if number is not correct or no argument provided
    add comments where necessary
    """

    return all_words

"""
selects single random word
"""
def select_random_word(all_words):

    word = ""

    """
    TODO:
    write a code that selects one single random word and returns that word
    random.choice() library comes handy here
    add comments where necessary
    """
    
    return word


"""
prompts the user for input
"""
def get_guess(word):

    """
    TODO:
    write a code that prompts player for word in correct length
    add comments where necessary
    """

    return ...


"""
iterates over word and checks for correct/wrong letters
"""
def check_guess(guess, word):
    # string for color-coding the word user enters
    # example: RRGYRY (R - red, G - green, Y - yellow)
    colorized_guess = "" * len(word)

    """
    TODO:
    write a code that 
    1) loops over the word user entered (done)
    2) checks for letters in correct places/correct letters in wrong places/wrong letters
    3) makes color-coded string for printing out result
    4) returns color-coded string
    """

    # loops through both letters and indices in word
    for position, letter in enumerate(guess):
        ...

    return colorized_guess 


"""
prints out the word in correct colors
"""
def print_word(colorized_guess, guess, guesses):

    colors = {
        "G": "green",
        "Y": "yellow",
        "R": "red"
    }

    """
    TODO:
    write a code that 
    1) prints out number of guesses user entered
    2) prints out colorized word by looping over letters (use dictionary with defined colors)
    """

    return None


"""
main logic
"""
def main():
    try:
        all_words = read_all_words()
        word = select_random_word(all_words)
    except Exception as e:
        print(e)

    print("[green]This is WORDLE[/green]")

    # for counting user inputs
    guesses = 0 

    guess = ""

    # repeats prompting until user guess the word or no more available guesses
    while guess != word: 
        guess = ""

        # repeats prompting for input when word is too short or too long
        while len(guess) != len(word):
            guess = get_guess(word)

        # next guess
        guesses += 1 

        colorized_guess = check_guess(guess, word)

        # prints colorized word
        print_word(colorized_guess, guess, guesses)

        if guesses > 5:
            print("No luck today!")
            break
    else:
        # VICTORY!
        print("You guessed the word!")

if __name__ == "__main__":
    main()