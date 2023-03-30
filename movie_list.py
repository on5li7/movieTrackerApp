"""
This module defines a MovieList class that represents a list of watched and unwatched movies.
"""

from movie import Movie

class MovieList:
    """
    Represents a list of watched and unwatched movies.

    Attributes:
        not_watched (list): A list of movies that have not been watched.
        watched (list): A list of movies that have been watched.
    """

    def __init__(self, not_watched, watched):
        """
        Initializes a new instance of the MovieList class.

        Args:
            not_watched (list): A list of movies that have not been watched.
            watched (list): A list of movies that have been watched.
        """
        self.not_watched = not_watched
        self.watched = watched

    def add_new_movie(self, movie):
        """
        Adds a new movie to the list of unwatched movies.

        Args:
            movie (Movie): The movie to add to the list.
        """
        self.not_watched.append(movie)

    def already_watched(self, movie):
        """
        Moves a movie from the list of unwatched movies to the list of watched movies.

        Args:
            movie (Movie): The movie to move to the list of watched movies.
        """
        self.not_watched.remove(movie)
        self.watched.append(movie)

    def display_all(self):
        """
        Displays all movies in the lists of watched and unwatched movies.
        """
        print("watched list")
        for i in self.watched:
            print(i.get_title())
        print("not watched list")
        for i in self.not_watched:
            print(i.get_title())

def main():
    """
    The main function of the program.
    """
    arr1 = []
    arr2 = []

    movie = input("Enter a movie you watched: ")
    rating = input("Enter a rating for the movie: ")

    not_watched_movie = input("Enter a movie you have not watched but want to: ")
    not_watched_rating = 0

    movie1 = Movie(movie, rating)
    movie2 = Movie(not_watched_movie, not_watched_rating)

    movie_list = MovieList(arr1, arr2)

    movie_list.add_new_movie(movie1)
    movie_list.add_new_movie(movie2)
    movie_list.already_watched(movie1)
    movie_list.display_all()

    #movie1 = Movie("Titanic", 2)
    #movie2= Movie("Titanic2", 2)
    #movie3 = Movie("Titanic3", 2)

    #movie_list1 = MovieList(arr1, arr2)

    #movie_list1.add_new_movie(movie1)
    #movie_list1.add_new_movie(movie2)
    #movie_list1.add_new_movie(movie3)

    # movie_list1.displayAll()
    #movie_list1.already_watched(movie1)

    #movie_list1.display_all()

if __name__ == "__main__":
    main()
