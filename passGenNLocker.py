# Create a pass generator that doubles as a password locker

# NOTES: dictionary = {"key": "value"}

from secrets import *
from string import *

# Dictionary for letter change and special characters
lDict = {"a": "@", "c": "C", "d": "(", "e": "3", "f": "F", "h": "H", "i": "!", "j": "?", "l": "|",
         "o": "0", "p": ")", "s": "$", "u": "U", "v": "^", "w": "W", "x": "X", "z": "Z"}
NUMBERS = digits
ALPHABET = printable
SPECIAL_CHAR = punctuation


# Iterates through user-generated word and changes value based off of letter given
def generate():

    # Define final_pass as a list for iteration
    new_pass = []

    # Collect word from user and criteria for creation of password
    word = str(input("What word would you like to use? "))
    min_length = int(input("What would you like the minimum length of the password to be? "))
    min_num = int(input("How many numbers minimum would you like? "))
    min_sc = int(input("How many special characters minimum would you like? "))
    min_caplet = int(input("How many capital letters minimum would you like? "))

    # Iterates through word one letter, number or spec char at a time
    for w in word:

        # Replaces letter if found in dictionary with its value
        new_pass.append(lDict.get(w, w))

    # Join letters to form new password
    new_pass = ''.join(new_pass)

    # Checks if new password meets user-generated requirements
    # min_num
    if not min_num - new_pass.count(NUMBERS) < 0:
        new_pass += "".join(choice(NUMBERS) for n in range(min_num - new_pass.count(NUMBERS)))

    # min_sc
    if not min_sc - new_pass.count(SPECIAL_CHAR) < 0:
        new_pass += "".join(choice(SPECIAL_CHAR) for n in range(min_sc - new_pass.count(SPECIAL_CHAR)))

    # min_caplet
    if not min_caplet - new_pass.count(ascii_uppercase) < 0:
        new_pass += "".join(choice(ascii_uppercase) for n in range(min_caplet - new_pass.count(ascii_uppercase)))

    # min_length
    if not min_length - len(new_pass) < 0:
        new_pass += "".join(choice(ALPHABET) for n in range(min_length - len(new_pass)))

    # Prints new password
    print("Here is your new strong password: " + new_pass)

    # Checks if user wants to input another password
    check = str(input("Would you like to create another password? (Y/N) "))
    check.lower()
    while check != "y" and check != "n":
        check = str(input("Please enter y or n: "))
        check.lower()
    else:
        if check == "n":
            # (WIP) Does not save password to anything yet
            exit("Saving Passwords...")
        else:
            generate()


generate()
