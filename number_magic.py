"""
Homework 4: Number Magic
=======================
Course:   CS 5001
Semester: Spring 2023
Student:  Alex Perkins
A series of functions that deal with number manipulation and string
concatenation
"""


def evens(max: int = 10) -> str:
    """Returns an even number only string separated by commas
    Examples:
        >>> evens()
        '0,2,4,6,8,10'
        >>> evens(max=17)
        '0,2,4,6,8,10,12,14,16'
    Args:
        max (int, optional): the max number in the sequence. Defaults to 10.
    Returns:
        str: returns even numbers up to max separated by commas
    """
    i = 1
    even = [0]
    while i <= max:
        if i % 2 == 0:
            even += [i]
        i += 1
    even = ','.join(str(i) for i in even)
    return even


def odds(max: int = 10) -> str:
    """Returns an odd number only string separated by commas
    Examples:
        >>> odds()
        '1,3,5,7,9'
        >>> odds(15)
        '1,3,5,7,9,11,13,15'
    Args:
        max (int, optional): the max number in the sequence. Defaults to 10.
    Returns:
        str: returns even numbers up to max separated by commas
    """
    i = 2
    odd = [1]
    while i < max:
        if i % 2 == 1:
            odd += [i]
        i += 1
    odd = ','.join(str(i) for i in odd)
    return odd


def number_string(number: int = 2, max: int = 10, 
                  invert: bool = False, delim: str = ",") -> str:
    """
    generate a number string with commas between each number
    only showing the numbers divisible by a set number. Adding invert = True
    prints out the inverted set of numbers.
    Examples:
        >>> number_string()
        '0,2,4,6,8,10'
        >>> number_string(3, 9)
        '0,3,6,9'
        >>> number_string(invert=True)
        '1,3,5,7,9'
        >>> number_string(2, 15, True)
        '1,3,5,7,9,11,13,15'
        >>> number_string(2, 15, True, ' ')
        '1 3 5 7 9 11 13 15'
    Args:
        number (int, optional): the divisor. Defaults to 2.
        max (int, optional): the max number in the sequence. Defaults to 10.
        invert (bool, optional): whether to print out the
            divisor set or inverted set. Defaults to False
        delim (str, optional): deliminator to put between numbers.
            Defaults to ','
    Returns:
        str: a comma separated value string of numbers
    """
    i = 0
    list = []
    list2 = []
    while i <= max:
        if i % number == 0:
            list += [i]
        else:
            list2 += [i]
        i += 1
    list = delim.join(str(i) for i in list)
    list2 = delim.join(str(i) for i in list2)
    if bool(invert) is False:
        answer = list
    if bool(invert) is True:
        answer = list2
    return answer
