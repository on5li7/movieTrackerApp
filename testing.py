import unittest
from mainPane import *

class TestMovieList(unittest.TestCase):

    def test_create_movie_list(self):
        create_movie_list()
        self.assertEqual(len(movies_list), 1)
        self.assertEqual(movies_list[0].get_title(), "the last Jedi")
        self.assertEqual(movies_list[0].get_rating(), "4")
        self.assertEqual(movies_list[0].get_comment(), "I liked it")
        self.assertEqual(movies_list[0].get_image_path(), "Movie_Images/The_Last_Jedi_resized.png")

if __name__ == '__main__':
    unittest.main()
