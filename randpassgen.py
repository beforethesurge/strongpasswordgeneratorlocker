# Create a pass generator that doubles as a password locker
# NOTES: dictionary = {"key": "value"}

# Dictionary for letter change and special characters
lDict = {"a": "@", "c": "C", "d": "(", "f": "F", "h": "H", "i": "!", "j": "?", "l": "|",
         "o": "0", "p": ")", "s": "$", "u": "U", "v": "^", "w": "W", "x": "X", "z": "Z"}
scSet = ("!", "@", "#", "$", "%", "^", "&", "*", "?", ">", "<")


# Iterates through user-generated word and changes value based off of letter given
def generate():
    # Define final_pass as a set for iteration
    final_pass = []
    # Collect word from user
    word = input(str("What word would you like to use? "))
    # Iterates through word one letter at a time
    for w in word:
        # Replaces letter if found in dictionary with its value
        final_pass.append(lDict.get(w, w))
    # Join letters to form word
    final_pass = ''.join(final_pass)

    print("Here is your new strong password: " + str(final_pass))


generate()
