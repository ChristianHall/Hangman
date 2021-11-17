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
    completed = False
    if difficulty == "e":
        lives = 9
    else:
        lirves = 7
    while not completed:
        coded_word = get_coded_word(answer_array, guessed_array, False)
        response = game_screen(coded_word, lives, guessed_array)
        if len(response) == 1:
            if response.lower() in "abcdefghijklmnopqrstuvwxyz":
                if response.lower() in guessed_array:
                    print(center_padding("ALREADY GUESSED LETTER, TRY AGAIN", WIDTH))
                else:
                    guessed_array.append(response.lower())
                    if response.lower() in word:
                        completed = check_for_solved(word, get_coded_word(answer_array,guessed_array, True))
                    else:
                        print(center_padding("INCORRECT GUESS", WIDTH))
                        lives -= 1
            else:
                print(center_padding("PLEASE ENTER A LETTER", WIDTH))

        elif len(response) > 1:
            if response.lower() == word.lower():
                completed = True
            else:
                print(center_padding("INCORRECT GUESS", WIDTH))
                lives -= 1

        if lives == 0:
            completed = True
            defeat(word)
    
    if lives > 0:
        victory(word)
        
    


def get_word(difficulty):
    diffword = False
    if "e" in difficulty:
        length = [10,20]
    elif "m" in difficulty:
        length = [7,10]
    elif "d" in difficulty:
        length = [5,10]
        diffword = True

    idx = randint(1,9984)
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


def get_coded_word(answer_array, guessed_array, compare):
    coded_word = ''
    for letter in answer_array:
        found_letter = False
        for guess in guessed_array:
            if letter == guess:
                found_letter = True
        if found_letter:
            coded_word += letter.upper()
        else:
            coded_word += "?"
        if not compare:
            coded_word += " "
    return coded_word


def check_for_solved(word, coded_word):
    if coded_word.lower() == word:
        return True
    else:
        return False


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
        elif height == 1:
            choice = input(prompt)
        height -= 1
    print("\n\n")
    return choice


def game_screen(coded_word, lives, guessed_array):
    height = 10
    guesses = ""
    for guess in guessed_array:
        guesses += guess.upper()
    while height > 0:
        if height == 10 or height == 2:
            print(full_spacer)
        elif height == 9:
            print(center_padding(f"{lives} LIVES REMAINING", WIDTH))
        elif height == 8 or (height < 7 and height > 3):
            print(empty_spacer)
        elif height == 7:
            print(center_padding(coded_word, WIDTH))
        elif height == 3:
            print(left_padding(guesses, WIDTH))
        elif height == 1:
            guess = input("enter letter or guess: ")
        height -= 1
    print("\n\n")
    return guess


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


def victory(word):
    print(full_spacer)
    print(empty_spacer)
    print(center_padding("CONGRATS! YOU GUESSED", WIDTH))
    print(center_padding(word.upper(), WIDTH))
    print(center_padding("CORRECTLY!", WIDTH))
    print(empty_spacer)
    print(full_spacer)
    answer = input("press ENTER to continue")
    print("\n\n")


def defeat(word):
    print(full_spacer)
    print(empty_spacer)
    print(center_padding("Good try. The word was:", WIDTH))
    print(center_padding(word.upper(), WIDTH))
    print(center_padding("Please try again!", WIDTH))
    print(empty_spacer)
    print(full_spacer)
    answer = input("press ENTER to continue")
    print("\n\n")


if os.path.isfile(DICTIONARY):
    main_menu()
    print("\n\n\n\n\nGoodbye\n\n\n\n\n\n\n\n\n")
else:
    print(f"\n\n\n\n\nERROR: DICTIONARY NOT FOUND\n{DICTIONARY}\n\n\n\n\n\n\n\n")
