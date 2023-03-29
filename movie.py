class Movie:
    """
    This class represents a movie object.

    Attributes:
        title (str): The title of the movie.
        rating (int): The rating of the movie.
    """

    def __init__(self, title='', rating=0):
        """
        Initializes a new instance of the Movie class.

        Args:
            title (str): The title of the movie.
            rating (int): The rating of the movie.
        """
        self.title = title
        self.rating = rating

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
