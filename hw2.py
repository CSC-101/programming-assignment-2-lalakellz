import data
from typing import List, Optional
from data import Point, Rectangle, Duration, Song

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
# Function to filter songs shorter than a given duration
# input: list of Song objects, a Duration object as the upper bound
# output: list of Song objects with durations shorter than the specified upper bound
def song_shorter_than(songs: List[Song], dur: Duration ) -> List[Song]:
    result = []
    max_sec = dur.tot_secs()
    # go through each song and check if its duration is shorter than dur
    for song in songs:
        if song.duration.tot_secs() < max_sec:
            result.append(song)

    return result

# Part 4
# Function to calculate the total running time for a playlist.
# input: list of Song objects, list of integers indicating the song order in the playlist
# output: a Duration object with the total playlist running time
def running_time(songs: List[Song], playlist: List[int]) -> Duration:
    total_secs = 0
    # go through each song number in the playlist.
    for song_index in playlist:
        # Only consider song_index if it's within the range of the songs list.
        if 0 <= song_index < len(songs):
            total_secs += songs[song_index].duration.tot_secs()

    # Calculate total minutes and seconds for the final Duration.
    mins = total_secs // 60
    seconds = total_secs % 60
    return Duration(mins, seconds)

# Part 5
# Function to validate a travel route between cities
# input: list of city links
# input: route list
# output: bool to show if the route is valid
def validate_route(city_links: list[list[str]], route: list[str]) -> bool:
    #an
    if len(route) <= 1:
        return True

    for i in range(len(route) -1):
        city1, city2 = route[i], route[i + 1]

        if [city1, city2] not in city_links and [city2, city1] not in city_links:
            return False

    return True

# Part 6
# Function to find the starting index of the longest contiguous repetition
# input: list of integers
# output: index of the longest contiguous repetition
def longest_repetition(lst: List[int]) -> Optional[int]:
    if not lst:
        return None
    max_idx = 0
    max_len = 1
    start = 0 # Start index of the current repetition
    length = 1 # Length of the current repetition

    for i in range(1, len(lst)):
        if lst[i] == lst[i - 1]:
            # Continue the repetition
            length += 1
        else:
            # End of the current repetition, compare and reset
            if length > max_len:
                max_len = length
                max_idx = start
            # Reset current repetition
            start = i
            length = 1
    # Final check after loop in case longest repetition is at the end
    if length > max_len:
        max_idx = start

    return max_idx

