import unittest
from mainPane import *
from graphics import GraphWin
from fake_create_input import f
from graphics import *

class TestMovieList(unittest.TestCase):

    def test_create_movie_list(self):
        create_movie_list()
        self.assertEqual(len(movies_list), 1)
        self.assertEqual(movies_list[0].get_title(), "the last Jedi")
        self.assertEqual(movies_list[0].get_rating(), "4")
        self.assertEqual(movies_list[0].get_comment(), "I liked it")
        self.assertEqual(movies_list[0].get_image_path(), "Movie_Images/The_Last_Jedi_resized.png")

    def test_adding_movie_to_the_database(self):
        f()
        with open('movieData.txt', 'r') as file:
            lines = [line.strip() for line in file.readlines()]
        data = lines[len(lines)-1].split(",")
        print(data)
        self.assertEqual(data[0], "Test Title")
        self.assertEqual(data[1], "5")
        self.assertEqual(data[2], "Test comment")
        self.assertEqual(data[3], "/test/path")


if __name__ == '__main__':
    unittest.main()
