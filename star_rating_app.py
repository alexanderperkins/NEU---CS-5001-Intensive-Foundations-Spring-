"""
Homework 3: Star Rating App
===========================
Course:   CS 5001
Semester: Spring 2023
Student:  Alex Perkins
An application that queries the client for movie titles
and a rating for each movie.
"""

# update
_MIN_STARS = 1
_MAX_STARS = 5


def add_movie():
    title = get_movie()
    val = get_rating()
    star = convert_rating(val)
    movie_list = star + "  " + title + "\n"
    return movie_list


def get_movie() -> str:
    title = input("Enter a movie: ")
    return title.title().strip()


def get_rating():
    try:
        val = float(input("Rate between 1 and 5: "))
    except ValueError:
        val = float(input("Input is not a number. Enter a rating 1 to 5: "))
    if val > _MAX_STARS:
        val = _MAX_STARS  # maximum star rating
    elif val < _MIN_STARS:
        val = _MIN_STARS  # minimum star rating
    else:
        val = int(val)  # rounded down star rating
    return val


def convert_rating(val):
    star = val * '*'
    star = str("{:<5}".format(star))
    return star


def list_movies(movies):
    print(movies)
    return


def menu():
    print("add -- Enter a movie and rating\n"
          "list -- List movies and ratings\n"
          "exit -- Exit\n")
    command = input("Command: ")
    command = command.lower().strip()
    return command


def run(movies: str = '') -> None:
    """
    Runs the star rating application.
    
    Args:
       The movie string, keeping track
       of all movies added between menu calls.
    """
    command = menu()
    if command == "add":
        movies += add_movie()
    if command == "list":
        list_movies(movies)
    if command == "exit":
        exit()
    if command != "exit":
        run(movies)
    else:
        menu()


if __name__ == "__main__":
    run()
