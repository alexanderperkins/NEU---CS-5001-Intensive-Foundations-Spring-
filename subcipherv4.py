"""
--------------------------
Midterm Substitution Cipher
--------------------------
STUDENT: Alex Perkins
SEMESTER: Spring 2023
"""
import sys
from string import digits, ascii_letters, punctuation
from random import sample

# use this for your original alphabet string. Excludes punctuation
ALL_LETTERS_DIGITS = digits + ascii_letters
# use this random key if none is provided, try printing it out to see what it is
RANDOM_KEY = "".join(sample(list(ALL_LETTERS_DIGITS), len(ALL_LETTERS_DIGITS)))


# add your functions here. Includes function for encrypting msg without punctuation
def encrypt(m, c1, k, c2):
    for letter in m:
        index = c1.index(letter)
        c2 += k[index]
    return c2


# Decrypts encrypted msg to revert to original msg and check it matches
def decrypt(c1, c2, k):
    m = ""
    for letter in c1:
        index = k.index(letter)
        m += c2[index]
    return m


# Do not modify the arguments for main, we will call it directly
def main(action: str, msg: str, key: str):
    """ Starting point of your program. You must start here."""
    chars = " " + ALL_LETTERS_DIGITS
    chars = list(chars)
    key = " " + RANDOM_KEY
    key = list(key)
    cipher = ''
    msg = input("\nWrite your msg: \n")
    print("\nThe encrypted msg is :")
    cipher = encrypt(msg, chars, key, cipher)
    print(cipher)

    print("\nHere's the cipher for reference:")
    print(chars)
    print(key)

    print("\nTo check backwards from encrypted msg:")
    print(cipher)
    print("\nHere's the decrypted msg:")
    check = decrypt(cipher, chars, key)
    print(check)


# The following allows us to run various features from the command line
# do not modify.
# If you wish to run the program from the command line
# You could do the following
# python subcipher.py "Aloha, World"
# that will encrypt this is my msg and return both msg and key
# you can decrypt by adding -d or --decrypt as the first argument, and then a key after the msg
# python subcipher.py -d "9HUqv, VUEHQ" "0XkDwIrGzYv17QfNiqgbZHJ5UhKEljCTRnxA9uaySWopM6emc2dP4sL83BVtFO"
if __name__ == "__main__":
    # check to see if there are command line arguments
    _action = 'encrypt'
    _msg = ''
    _key = ''
    if len(sys.argv) > 1:
        if sys.argv[1] == '-d' or sys.argv[1] == '--decrypt':
            _action = 'decrypt'
            remainder = sys.argv[2:]
        else:
            remainder = sys.argv[1:]
        if len(remainder) > 0:
            _msg = remainder[0]
            if len(remainder) > 1:
                _key = remainder[1]
    main(_action, _msg, _key)
