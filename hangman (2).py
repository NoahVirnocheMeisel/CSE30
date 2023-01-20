# assignment: programming assignment 1
# author: Noah Virnoche Meisel
# date: (write the date you finished working on the program)
# file: hangman.py is a program that runs the classic word game Hangman. The object is to guess a word by guessing
# letters in a limited number of attempts.
# input: The user inputs the size of the dictionary word, and the number of attempts they will have to guess the word
# output: After each guess from the user, the program will tell the user if the letter guessed is in the word
# and update the shown parts of the word accordingly. It will also add the letter to the list of already guessed
# letters for the user to see. Once the user guesses the word, or runs out of lives, the program will output an
# appropriate message and then ask the user if they want to play again.
import random
dictionary_file = "dictionary.txt"   # make a dictionary.txt in the same folder where hangman.py is located
# write all your functions here

# make a dictionary from a dictionary file ('dictionary.txt', see above)
# dictionary keys are word sizes (1, 2, 3, 4, …, 12), and values are lists of words
# for example, dictionary = { 2 : ['Ms', 'ad'], 3 : ['cat', 'dog', 'sun'] }
# if a word has the size more than 12 letters, put it into the list with the key equal to 12

def import_dictionary (filename) :
    dictionary = {}
    try:
        with open(filename,"r") as read_file:
            list_file = read_file.readlines()
        for i in range(1,13):
            if i >= 2:
                funky_list = []
                for d in list_file:
                    if len(d.strip()) == i:
                        funky_list.append(d.strip())
                    elif i == 12 and len(d) > i:
                        funky_list.append(d)
                dictionary[i]=funky_list
    except Exception:
        print("Uh oh, something went wrong <('_'<)")
    return dictionary

# print the dictionary (use only for debugging)
def print_dictionary (dictionary) :
    max_size = 12
    print(dictionary)

# get options size and lives from the user, use try-except statements for wrong input
def get_game_options () :
    try:
        size = int(input("Please choose a size of a word to be guessed [ 3 - 12, default any size]:\n"))
        assert 3 <= size <= 12
        print(f"The word size is set to {size}.")
    except Exception:
        size = random.randint(3,12)
        print("A dictionary word of any size will be chosen.")
    try:
        lives = int(input("Please choose a number of lives [1-10, default 5]:\n"))
        assert 1 <= lives <= 10
        print(f"You have {lives} lives.")
    except:
        lives = 5
        print("You have 5 lives.")
    return (size, lives)
# MAIN
if __name__ == '__main__' :

    # make a dictionary from a dictionary file
    dictionary = import_dictionary(dictionary_file)
    letters_we_like = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

    # print a game introduction
    print("Welcome to the Hangman Game!")

    # START MAIN LOOP (OUTER PROGRAM LOOP)
    while True:
    # set up game options (the word size and number of lives)
        options = get_game_options()
        size = options[0]
        lives = int(options[1])
    # select a word from a dictionary (according to the game options)
    # use choice() function that selects an item from a list randomly, for example:
    # mylist = ['apple', 'banana', 'orange', 'strawberry']
        word = random.choice(dictionary[size]).upper()
        #Was bugged due to range oversight in GetDictionary. Think fixed but should do some more tests later.
        word_as_list = []
        for i in word:
            word_as_list.append(i)
        display_list = []
        guessed_letters = []
        used_lives = 0
        #below code sets up the displayed list thing and handles the edge case of there being a - symbol
        for i in word_as_list:
            if i == "-":
                display_list.append("-")
            else:
                display_list.append("__")
        # START GAME LOOP   (INNER PROGRAM LOOP)
        while (lives > 0) and word_as_list != display_list:
            # format and print the game interface:
            # Letters chosen: E, S, P                list of chosen letters
            # __ P P __ E    lives: 4   XOOOO        hidden word and lives

            #this code sets up the interface that the user sees. So the Letters chosen section and the Display of their guessed word and their lives.
            print("Letters chosen: ",end = '')
            if len(guessed_letters) > 0:
                for i in guessed_letters:
                    if guessed_letters.index(i) == guessed_letters.index(guessed_letters[-1]):
                        print(i)
                    else:
                        print(f"{i}",end = ', ')
            else:
                print()
            for i in display_list:
                print(f"{i}", end = " ")
            print(f" lives: {lives}", end = ' ')
            for i in range(used_lives):
                print("X",end = '')
            for i in range(lives):
                print("O", end = '')
            print()
            #copys the display_list variable into an intermediary value to detect a change in the display to use later
            previous_display_list = display_list.copy()
        # ask the user to guess a letter, checks to make sure that the input has not already been guessed and that the letter is a valid letter(not ff or ah, needs to be an english alphabet charecter)
            while True:
                try:
                    user_letter = (input("Please choose a new letter >\n").upper())
                    if user_letter in guessed_letters:
                        print("You have already chosen this letter.")
                    elif user_letter not in letters_we_like:
                       pass
                    else:
                        break
                except Exception:
                    print("Please enter a valid letter")
        # update the list of chosen letters
            guessed_letters.append(user_letter)
            index_list = []
            for i in range(len(word_as_list)):
                if user_letter == word_as_list[i]:
                    display_list[i] = user_letter
            if previous_display_list != display_list:
                print("You guessed right!")
            else:
                print("You guessed wrong, you lost one life.")
                lives -= 1
                used_lives += 1
        # if the letter is correct update the hidden word,
        # else update the number of lives
        # and print interactive messages

        # END GAME LOOP   (INNER PROGRAM LOOP)
        #Before restarting game loop, check to see if the user either has the correct word or they are at 0 lives. If either is true it exits, but not before printing out the interface one last time
        if display_list == word_as_list:
            print("Letters chosen: ", end='')
            if len(guessed_letters) > 0:
                for i in guessed_letters:
                    if guessed_letters.index(i) == guessed_letters.index(guessed_letters[-1]):
                        print(i)
                    else:
                        print(f"{i}", end=', ')
            else:
                print()
            for i in display_list:
                print(f"{i}", end=" ")
            print(f" lives: {lives}", end=' ')
            for i in range(used_lives):
                print("X", end='')
            for i in range(lives):
                print("O", end='')
            print()
            print(f"Congratulations!!! You won! The word is {word}!")
        else:
            print("Letters chosen: ", end='')
            if len(guessed_letters) > 0:
                for i in guessed_letters:
                    if guessed_letters.index(i) == guessed_letters.index(guessed_letters[-1]):
                        print(i)
                    else:
                        print(f"{i}", end=', ')
            else:
                print()
            for i in display_list:
                print(f"{i}", end=" ")
            print(f" lives: {lives}", end=' ')
            for i in range(used_lives):
                print("X", end='')
            for i in range(lives):
                print("O", end='')
            print()
            print(f"You lost! The word is {word}!")

        #prompts the user if they want to play the game again, or exit the program

        user_choice = input("Would you like to play again [Y/N]?\n").upper()

        if user_choice == "Y":
            continue
        else:
            print("Goodbye!")
            break

        # check if the user guesses the word correctly or lost all lives,
        # if yes finish the game
    # END MAIN LOOP (OUTER PROGRAM LOOP)

    # ask if the user wants to continue playing, 
    # if yes start a new game, otherwise terminate the program
