import data
from data import Point, Rectangle, Duration


# Write your functions for each part in the space below.

# Part 1
# Create a Rectangle object from two Point objects by determining
# the top left/ bottom right corners based on x and y values
# input: two Point objects
# output: a Rectangle object
def create_rectangle(point1: Point, point2: Point) -> Rectangle:
    #determine top left/ bottom right Point object
    top_left_x = min(point1.x, point2.x)
    bottom_right_x = max(point1.x, point2.x)
    top_left_y = max(point1.y, point2.y)
    bottom_right_y = min(point1.y, point2.y)

    #top left/ bottom right Point objects
    top_left = Point(top_left_x, top_left_y)
    bottom_right = Point(bottom_right_x, bottom_right_y)

    return Rectangle(top_left, bottom_right)

# Part 2
# Define a function to check if one duration is shorter than another.
# input: two Duration objects
# output: bool showing if first Duration is shorter than the second
def shorter_duration_than(dur1: Duration, dur2: Duration) -> bool:
    # Convert both durations to total seconds for comparison
    seconds1 = dur1.minutes * 60 + dur2.seconds
    seconds2 = dur2.minutes * 60 + dur2.seconds

    # Return True if dur1 is shorter than dur2, otherwise False
    return seconds1 < seconds2

# Part 3


# Part 4


# Part 5


# Part 6
