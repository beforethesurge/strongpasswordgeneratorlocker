# Create a pass generator that doubles as a password locker
# NOTES: dictionary = {"key": "value"}

# Dictionary for letter change and special characters
lDict = {"a": "@", "c": "C", "d": "(", "f": "F", "h": "H", "i": "!", "j": "?", "l": "|",
         "o": "0", "p": ")", "s": "$", "u": "U", "v": "^", "w": "W", "x": "X", "z": "Z"}
# (WIP) Constant that will be an input for user later
MIN_LENGTH = 8
MIN_NUM = 2
MIN_SC = 1
MIN_CAPLET = 1


# Iterates through user-generated word and changes value based off of letter given
def generate():
    # Define final_pass as a list for iteration
    final_pass = []
    # Collect word from user
    word = input(str("What word would you like to use? "))
    # Iterates through word one letter at a time
    for w in word:
        # Replaces letter if found in dictionary with its value
        final_pass.append(lDict.get(w, w))
    # Join letters to form new password
    final_pass = ''.join(final_pass)
    # Prints new password
    print("Here is your new strong password: " + str(final_pass))
    # Checks if user wants to input another password
    check = str(input("Would you like to create another password? (Y/N) "))
    check.lower()
    while check != "y" and check != "n":
        check = str(input("Please enter y or n: "))
        check.lower()
    else:
        if check == "n":
            # (WIP) Does not save password to anything yet
            exit("Saving Passwords!")
        else:
            generate()


generate()
