"""
Homework 1: MY ASCII ART
===========================
Course:   CS 5001
Semester: Spring 2023
Student:  Alex Perkins
                             
A simple assignment to have fun printing artwork.  
"""
# The block above is a docstring (short for document string).
# It starts at the triple double quote,
# and ends at the triple double quote
# Make sure you update it by modifying semester and your name
# Follow the instructions found at https://github.com/CS5001-khoury/HW1-Welcome

def myart():

    art = ' \-------\                       \**/\n'
    art += '  ||  \-----\                     ||                    \n'
    art += '  ||       \-----\                ||                           |\\    |             |   ||                            |   \n'
    art += '  ||           \-----\            ||                           |  \\  | //\\ ||**; ==|== ||/*\  /’[]’\  /’[]’\  /2’\ ==|== /’[]’\ ||**; |/*\	\n'
    art += '  ||               \-----\        ||                           |    \\| \\// ||      |   ||  |   \'’_’]  \___^_\‘\V‘/   |    \'’_’] ||    |  |\n'
    art += '  ||                   \-----\    ||                           ||    ||      *                         *   |\n'
    art += '  ||                       \-----\||                           ||    |||/*\ | \  / /’[]’\ ||**; /.2’\  | ==|== \\  //\n'
    art += ' /__\                          \___|                            \\___// |  | |  \/   \'’_’] ||    ‘\V‘/  |   |    \\//\n'
    art += '                                                                                                              \_//\n'

    return art

def main():
    print(myart())


# This block of "magic" informs the python interpreter to start executing code in the main() function
# when the file is loaded.
if __name__ == "__main__":
    main()