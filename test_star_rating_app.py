"""
Homework 3: Star Rating App Tests
=======================
Course:   CS 5001
Semester: Spring2023
Student:  Alex Perkins
Tests an application that queries the client for movie titles
and a rating for each movie.
"""
from star_rating_app import get_movie, get_rating, convert_rating


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


def test_get_movie() -> int:
    """
    tests star_rating_app.get_rating
    Returns:
        float: the number of tests **failed**
    """
    fail = 0
    fail += check(get_movie("    v"), "V")
    fail += check(get_movie("star wars  "), "Star Wars")
    fail += check(get_movie(" thor "), "Thor")
    return fail


def test_get_rating() -> int:
    """
    tests star_rating_app.get_rating
    Returns:
        float: the number of tests **failed**
    """
    fail = 0
    fail += check(get_rating(0), "1")
    fail += check(get_rating(1.5), "1")
    fail += check(get_rating(5.2), "5")
    fail += check(get_rating(3.7), "3")
    return fail


def test_convert_rating() -> int:
    """
    tests star_rating_app.convert_rating
    Returns:
        float: the number of tests **failed**
    """
    fail = 0
    fail += check(convert_rating(0), "*")
    fail += check(convert_rating(1.2), "*")
    fail += check(convert_rating(6.1), "*****")
    fail += check(convert_rating(2.6), "**")
    return fail


def run() -> None:
    fail = 0
    fail += test_get_movie()
    fail += test_get_rating()
    fail += test_convert_rating()

    print(f"Failed {fail} tests.")


if __name__ == "__run__":
    run()
