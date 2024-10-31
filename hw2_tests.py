import data
import hw2
import unittest

from data import Duration
from hw2 import Point, create_rectangle, shorter_duration_than, song_shorter_than, Song, running_time, validate_route, longest_repetition

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
    def test_running_time(self):
        song1 = Song("June Hymn", "Decemberists", Duration(4, 30))
        song2 = Song("October", "Broken Bells", Duration(3, 40))
        song3 = Song("Dust in the Wind", "Kansas", Duration(3, 29))
        song4 = Song("Airplanes", "Local Natives", Duration(3, 58))

        songs = [song1, song2, song3, song4]
        playlist = [0, 2, 1, 3, 0]

        result = running_time(songs, playlist)
        self.assertEqual(result.minutes, 20)
        self.assertEqual(result.seconds, 7)

    def test_running_time_with_out_of_range_indices(self):
        song1 = Song("June Hymn", "Decemberists", Duration(4, 30))
        song2 = Song("October", "Broken Bells", Duration(3, 40))
        song3 = Song("Dust in the Wind", "Kansas", Duration(3, 29))

        songs = [song1, song2, song3]
        playlist = [0, 1, 4, 2, -1, 5]

        result = running_time(songs, playlist)
        self.assertEqual(result.minutes, 11)
        self.assertEqual(result.seconds, 39)

    # Part 5
    def test_route(self):
        city_links = [
            ['san luis obispo', 'santa margarita'],
            ['san luis obispo', 'pismo beach'],
            ['atascadero', 'santa margarita'],
            ['atascadero', 'creston']
        ]
        route = ['san luis obispo', 'santa margarita', 'atascadero']
        self.assertTrue(validate_route(city_links, route))

    def test_single_city_route(self):
        city_links = [
            ['san luis obispo', 'santa margarita'],
            ['san luis obispo', 'pismo beach'],
            ['atascadero', 'santa margarita'],
            ['atascadero', 'creston']
        ]
        route = ['san luis obispo']
        self.assertTrue(validate_route(city_links, route))

    def test_empty_route(self):
        city_links = [
            ['san luis obispo', 'santa margarita'],
            ['san luis obispo', 'pismo beach'],
            ['atascadero', 'santa margarita'],
            ['atascadero', 'creston']
        ]
        route = []
        self.assertTrue(validate_route(city_links, route))

    # Part 6
    def test_longest(self):
        lst = [1, 1, 2, 2, 1, 1, 1, 3]
        self.assertEqual(longest_repetition(lst), 4)

    def test_longest_repetition_empty(self):
        lst = []
        self.assertIsNone(longest_repetition(lst))

    def test_longest_repetition_no_repeats(self):
        lst = [1, 2, 3, 4, 5]
        self.assertEqual(longest_repetition(lst), 0)




if __name__ == '__main__':
    unittest.main()
