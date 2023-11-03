"""
Homework 3: Test Game Helper
============================
Student:  Alex Perkins
Semester: Spring 2023
Run tests on game_helper
"""
from .game_helper import area_sq, area_rec, vol_cube, area_triangle, can_add, roll_dice, vol_pyramid

def test_area_sq():
    assert area_sq(5)
    assert area_sq(10.5)
    return

def test_area_rec():
    assert area_rec(5, 10)
    assert area_rec(0.075, 0.02)
    return

def test_vol_cube():
    assert vol_cube(10, 12, 10)
    assert vol_cube(0.2, 10, 5.3)
    return

def test_area_triangle():
    assert area_triangle(10, 10)
    assert area_triangle(4.2, 17)
    return

def test_vol_pyramid():
    assert vol_pyramid(10, 10)
    assert vol_pyramid(33, 6)
    return

def test_can_add():
    assert can_add(5, 0, 7)
    assert can_add(5, 10, 2)
    return

def test_roll_dice():
    assert roll_dice(100)
    assert roll_dice(6)
    return


### example main, use as you want. 
def main() -> None:
    print("Running all tests")
    fail_count = test_area_sq()
    fail_count += test_area_rec()
    fail_count += test_vol_cube()
    fail_count += test_area_triangle()
    fail_count += test_vol_pyramid()
    fail_count += test_can_add()
    fail_count += test_roll_dice()    


    if (fail_count > 0):
       print(f"Failed {fail_count} tests.")


if __name__ == '__main__':
    main()