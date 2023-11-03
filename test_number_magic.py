"""
Homework 4: Number Magic Tests    
=======================
Course:   CS 5001
Semester: Spring2023
Student:  Alex Perkins
Tests A series of functions that deal with number manipulation and string concatenation 
"""
from number_magic import number_string, evens, odds



def check(actual: str, expected: str) -> int:
    """checks for error, returns 1 if error exists, 0 if it doesn't
    Args:
        actual (str): actual value
        expected (str): expected value
    """
    if actual != expected:
        print(f"Actual: {actual} does not equal Expected: {expected}")
        return 1
    return 0


def test_number_string() -> int:
    """
    tests number_magic.number_string
    Returns:
        int: the number of tests **failed**
    """
    fail = 0
    fail += check(number_string(), "0,2,4,6,8,10")
    fail += check(number_string(2, 9), "0,2,4,6,8")
    fail += check(number_string(3, 9), "0,3,6,9")
    fail += check(number_string(4, 16), "0,4,8,12,16")
    fail += check(number_string(2, 10, True), "1,3,5,7,9")
    fail += check(number_string(2, 15, True), "1,3,5,7,9,11,13,15")
    fail += check(number_string(2, 15, True, ' '), "1 3 5 7 9 11 13 15")
    return fail


def test_evens() -> int:
    """checks number_magic.evens
    Returns:
        int: the total number of errors
    """
    fail = 0
    fail += check(evens(), "0,2,4,6,8,10")
    fail += check(evens(max=17), "0,2,4,6,8,10,12,14,16")

    return fail


def test_odds() -> int:
    fail = 0
    fail += check(odds(), "1,3,5,7,9")
    fail += check(odds(max=17), "1,3,5,7,9,11,13,15")

    return fail


def main() -> None:
    fail = 0
    fail += test_number_string()
    fail += test_evens()
    fail += test_odds()

    print(f"Failed {fail} tests.")


if __name__ == "__main__":
    main()