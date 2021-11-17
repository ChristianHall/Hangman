# this is the hangman main page
# there will be multiple levels
# All options will have RSTLNE
#       Easy - RSTLNE, 
#       Medium
#       Hard
#
# User will type a letter or the word/phrase, program will detect this and parse through the code
# TODO
# 1. Get basic app wtih menu options
# 2. Get access to dictionary (of words or phrases) https://www.mit.edu/~ecprice/wordlist.10000
# 3. Apple score system
from random import randint
import os


DICTIONARY = cwd = os.getcwd() + "/dictionary.txt"
WIDTH = 50


def main_menu():
    choice = " "
    while choice.lower() != "q":
        choice = menu("HANGMAN", ["P - Play a game", "A - About", "Q - Quit"], "Select an option: ")
        if choice.lower() == "p":
            gameplay_menu()
        elif choice.lower() == "a":
            about_menu()
        else:
            print(center_padding("!! PLEASE ENTER A VALID CHOICE !!", WIDTH))


def gameplay_menu():
    choice = " "
    while choice.lower() != "b":
        choice = menu("SELECT DIFFICULTY", ["E - Easy", "M - Medium", "D - Difficult", "B - Back to main menu"], "Select difficulty: ")
        if choice.lower() == "e" or choice.lower() == "m" or choice.lower() == "d":
            play_game(choice.lower())
        else:
            print(center_padding("!! PLEASE ENTER A VALID CHOICE !!", WIDTH))
        

def about_menu():
    choice = menu("ABOUT",
                ["This was created in November 2021 by Christian",
                 "Hall just for fun and code practice. The words",
                 "are imported from https://www.mit.edu/~ecprice",
                 "/wordlist.10000. Thanks for playing!"],
                 "press ENTER to return ")


def play_game(difficulty):
    word = get_word(difficulty)
    answer_array = [char for char in word]
    guessed_array = ["r", "s", "t", "l", "n", "e"]
    solved = False
    lives = 5
    while lives > 0 or not solved:
        coded_word = get_coded_word(answer_array, guessed_array)
        response = game_screen(coded_word, lives)
        if len(response) == 1:
            # if the letter.lower() is in the guessed array, prompt the player to try again without taking lives
            # if the letter.lower() is not in the guessed array, add it to the array
            #       If the player guessed correctly, it will be revealed
            #           Check to see if the word has been revealed, changing solved to True if it has
            #       If the player guessed incorrectly, a life will be lost
            pass
        elif len(response > 1):
            # check if the answer.lower() == word.lower(). If it does, set solved to True
            # if answer.lower() != word.lower(), a life is lost
            pass


        lives -= 1 # delete this
    if lives == 0:
        # losing print screen, goes back to gameplay_menu
        pass
    elif solved:
        # winning print screen, goes back to gameplay_menu
        pass


def get_word(difficulty):
    diffword = False
    if "e" in difficulty:
        length = [10,20]
    elif "m" in difficulty:
        length = [7,10]
    elif "d" in difficulty:
        length = [5,10]
        diffword = True

    idx = randint(1,9997)
    dictionary = open(DICTIONARY)
    lines = dictionary.readlines()
    usable_word = False
    while not usable_word:
        word = lines[idx].rstrip("\r\n")
        if len(word) >= length[0] and len(word) < length[1]:
            if not diffword:
                usable_word = True
            elif diffword:
                if "z" in word or "q" in word or "x" in word:
                    usable_word = True
        idx += 1
    return word


# ===================================================================================================
# ALL VISUAL ELEMENTS ARE BELOW HERE
# ===================================================================================================

full_spacer = "**************************************************"
empty_spacer = "*                                                *"


def menu(title, content, prompt):
    height = 10
    while height > 0:
        if height == 10 or height == 2:
            print(full_spacer)
        elif height == 9:
            print(center_padding(title, WIDTH))
        elif height == 8:
            print(empty_spacer)
        elif height == 7:
            for line in content:
                print(left_padding(line, WIDTH))
                height -= 1
        elif height < 8 and height > 3:
            print(empty_spacer)
        elif height == 3:
            print("guessed words go here")
        elif height == 1:
            choice = input(prompt)
        height -= 1
    print("\n\n")
    return choice


def game_screen(coded_word, lives):
    height = 10
    while height > 0:
        if height == 10 or height == 2:
            print(full_spacer)
        elif height == 9:
            print(center_padding(f"{lives} LIVES REMAINING", WIDTH))
        elif height == 8 or (height < 7 and height > 2):
            print(empty_spacer)
        elif height == 7:
            print(center_padding(coded_word, WIDTH))
        elif height == 1:
            guess = input("enter letter or guess: ")
        height -= 1
    return guess


def get_coded_word(answer_array, guessed_array):
    coded_word = ''
    for letter in answer_array:
        found_letter = False
        for guess in guessed_array:
            if letter == guess:
                found_letter = True
        if found_letter:
            coded_word += f"{letter.upper()} "
        elif not found_letter:
            coded_word += "? "
    return coded_word


def center_padding(content, WIDTH):
    while len(content) < WIDTH - 2:
        if len(content)%2 == 0:
            content = content + " "
        else:
            content = " " + content
    return "*" + content + "*"


def left_padding(content, WIDTH):
    content = "* " + content
    while len(content) < WIDTH - 1:
        content = content + " "
    return content + "*"


if os.path.isfile(DICTIONARY):
    main_menu()
    print("\n\n\n\n\nGoodbye\n\n\n\n\n\n\n\n\n")
else:
    print(f"\n\n\n\n\nERROR: DICTIONARY NOT FOUND\n{DICTIONARY}\n\n\n\n\n\n\n\n")
