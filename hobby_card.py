"""
Homework 1: Hobby Card
===========================
Course:   CS 5001
Semester: Spring 2023
Student:  Alex Perkins
                             
A simple assignment to practice string concatenation.  
"""
# The block above is a docstring (short for document string).
# It starts at the triple double quote,
# and ends at the triple double quote
# Make sure you update it by modifying semester and your name
# Follow the instructions found at https://github.com/CS5001-khoury/HW1-Welcome


def hobby_card():
    """Builds a string that represents your hobby card."""
    card = '+------------------------------+\n'
    card += '|         A Hobby Card         |\n' 
    card += '| Alex Perkins                 |\n' 
    card += '|                              |\n' 
    card += '|    Exploring, Music, Food    |\n' 
    card += '|                              |\n' 
    card += '+------------------------------+\n' 


    return card # don't change



def main():
    print(hobby_card())



# This block of "magic" informs the python interpreter to start executing code in the main() function
# when the file is loaded.
if __name__ == "__main__":
    main()