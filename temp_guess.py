"""
Homework 2: Where to live
===========================
Course:   CS 5001
Semester: Spring 2023
Student:  Alex Perkins
An application that provides recommendations on where to live based on temp ranges. 
"""


def main():
    """
    Asks the client for two temperatures. Based on the values, it provides cities
    that meets the conditions. 
    | City | High | Low |
    | Beijing | 33 | -8 |
    | Boston | 28 | -7 |
    | Honolulu | 32 | 13 |
    | San Francisco | 27 | 6 |
    | Vancouver BC | 24  | 2 |
    Values can be in any order.
    Examples:
        >>> main()                                       # doctest: +NORMALIZE_WHITESPACE
        Enter a temperature: 28
        Enter a second temperature: -10
        Boston
        San Francisco
        Vancouver
        >>> main()                                       # doctest: +NORMALIZE_WHITESPACE
        Enter a temperature: 0
        Enter a second temperature: 20
        Unknown
    """

    pass  # remove and put your code here

    Temp1 = float(input("Enter a temperature: "))
    Temp2 = float(input("Enter a second temperature: "))

    if Temp1 > Temp2:
        high = Temp1
        low = Temp2
    else:
        high = Temp2
        low = Temp1

    if high >= 33 and low <= -8:
        print("Beijing")

    if high >= 28 and low <= -7:
        print("Boston")

    if high >= 32 and low <= 13:
        print("Honolulu")

    if high >= 27 and low <= 6:
        print("San Francisco")

    if high >= 24 and low <= 2:
        print("Vancouver")    

    if high < 24 and low > 2:
        print("Unknown")     

    if high >= 24 and low > 13:
        print("Unknown") 


if __name__ == "__main__":
    main()
