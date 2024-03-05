import sys
import random
from rich import print


"""
looks for all the words in certain file
"""
def read_all_words():

    all_words = []

    if len(sys.argv) > 1:
        lenght = sys.argv[1]
        if lenght == "5" or lenght == "6" or lenght == "7" or lenght == "8":
            with open('collections/'+lenght+'.txt', 'r') as words:
                all_words = words.read().split("\n")
        else:
            raise ValueError("Lenght not valid")
    else:
        raise ValueError("Lenght not valid")

    return all_words

"""
selects single random word
"""
def select_random_word(all_words):

    word = random.choice(all_words)
    
    return word


"""
prompts the user for input
"""
def get_guess(word):

    lenght = str(len(word))
    guess = input("PLease make a "+lenght+"-letter guess: ")
    

    return guess


"""
iterates over word and checks for correct/wrong letters
"""
def check_guess(guess, word):
    # string for color-coding the word user enters
    # example: RRGYRY (R - red, G - green, Y - yellow)
    colorized_guess = "" * len(word)
    "GYRRR"

    # loops through both letters and indices in word
    for position, letter in enumerate(guess):
        if letter in word:
            if guess[position] == word[position]:
                colorized_guess += "G"
            else:
                colorized_guess += "Y"
        else:
            colorized_guess += "R"

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

    output = ""
    n=0
    for i in colorized_guess:
        color = colors.get(i)
        output += (f"[{color}]{guess[n]}[/{color}]")
        n+=1
    print("Gueses made :" + str(guesses) + " " + str(output))

    return output


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