import unittest
from mainPane import *
from graphics import GraphWin
from fake_create_input import f


class TestMovieList(unittest.TestCase):

    # def test_create_movie_list(self):
    #     create_movie_list()
    #     self.assertEqual(len(movies_list), 1)
    #     self.assertEqual(movies_list[0].get_title(), "the last Jedi")
    #     self.assertEqual(movies_list[0].get_rating(), "4")
    #     self.assertEqual(movies_list[0].get_comment(), "I liked it")
    #     self.assertEqual(movies_list[0].get_image_path(), "Movie_Images/The_Last_Jedi_resized.png")


     def test_create_input_page(self):
        win = f()
        # call the function

        # test that the input fields were created and are empty
        title_input = win.checkMouse()
        self.assertEqual(title_input.getText(), "")
        star_input = win.checkMouse()
        self.assertEqual(star_input.getText(), "")
        comment_input = win.checkMouse()
        self.assertEqual(comment_input.getText(), "")
        path_input = win.checkMouse()
        self.assertEqual(path_input.getText(), "")

        # simulate clicking the save button and check that input was saved
        # save_button = win.checkMouse()
        # saved_text = "Test Title,3,This is a test comment,/test/image/path"
        # title_input.setText("Test Title")
        # star_input.setText("3")
        # comment_input.setText("This is a test comment")
        # path_input.setText("/test/image/path")
        # save_button = win.checkMouse()
        # with open('movieData.txt') as file:
        #     file_content = file.read()
        # self.assertIn(saved_text, file_content)

        # close the window
        win.close()

if __name__ == '__main__':
    unittest.main()
