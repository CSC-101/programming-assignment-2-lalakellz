import data
import hw2
import unittest

from data import Duration
from hw2 import Point, create_rectangle, shorter_duration_than, song_shorter_than, Song


# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 1
    def test_create_rectangle_standard(self):
        point1 = Point(2, 2)
        point2 = Point(10, 10)
        rectangle = create_rectangle(point1, point2)

        self.assertEqual(rectangle.top_left, Point(2, 10))
        self.assertEqual(rectangle.bottom_right, Point(10, 2))

    def test_create_rectangle_swapped(self):
        point1 = Point(10, 10)
        point2 = Point(2, 2)
        rectangle = create_rectangle(point1, point2)

        self.assertEqual(rectangle.top_left, Point(2, 10))
        self.assertEqual(rectangle.bottom_right, Point(10, 2))

    # Part 2
    def test_dur(self):
        dur1 = Duration (4, 30)
        dur2 = Duration(5, 0)
        self.assertTrue(shorter_duration_than(dur1, dur2))

    def test_shorter_duration_than_false(self):
        duration1 = Duration(6, 0)
        duration2 = Duration(5, 59)
        self.assertFalse(shorter_duration_than(duration1, duration2))

    # Part 3
    def test_song(self):
        song1 = Song("Song A", "Artist A", Duration(3, 30))
        song2 = Song("Song B", "Artist B", Duration(4, 15))
        song3 = Song("Song C", "Artist C", Duration(5, 0))
        max_duration = Duration(4, 0)

        result = song_shorter_than([song1, song2, song3], max_duration)
        self.assertEqual(result, [song1])

    def test_song_2(self):
        song1 = Song("Song D", "Artist D", Duration(2, 45))
        song2 = Song("Song E", "Artist E", Duration(3, 30))
        song3 = Song("Song F", "Artist F", Duration(4, 5))
        max_duration = Duration(4, 10)

        result = song_shorter_than([song1, song2, song3], max_duration)
        self.assertEqual(result, [song1, song2, song3])

    # Part 4


    # Part 5


    # Part 6





if __name__ == '__main__':
    unittest.main()
