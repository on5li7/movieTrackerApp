"""
This module defines the Movie class, which represents a movie object.
"""


class Movie:
    """
    This class represents a movie object.

    Attributes:
        title (str): The title of the movie.
        rating (int): The rating of the movie.
    """

    def __init__(self, title='', rating=0, comment ='', image_path=''):
        """
        Initializes a new instance of the Movie class.

        Args:
            title (str): The title of the movie.
            rating (int): The rating of the movie.
        """
        self.title = title
        self.rating = rating
        self.comment = comment
        self.image_path = image_path

    def get_title(self):
        """
        Gets the title of the movie.

        Returns:
            str: The title of the movie.
        """
        return self.title

    def set_rating(self, rating):
        """
        Sets the rating of the movie.

        Args:
            rating (int): The rating of the movie.
        """
        self.rating = rating

    def get_rating(self):
        """
        Gets the rating of the movie.

        Returns:
            int: The rating of the movie.
        """
        return self.rating
    def set_comment(self, comment):
        """
        Sets the comment of the movie.

        Args:
            comment (str): The comment of the movie.
        """
        self.comment = comment 
    def get_comment(self):
        """
        Gets the comment of the movie.

        Returns:
            str: The comment of the movie.
        """
        return self.comment
    def set_image_path(self, image_path):
        """
        Sets the image path of the movie

        Args: 
            image path(img): The image path of the movie.
        """
        self.image_path = image_path
    def get_image_path(self):
        """"
        Gets the image path of the movie.

        Returns:
            img: The image path of the movie.
        """
        return self.image_path