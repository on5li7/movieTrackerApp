'''
This class is for the movieLists object
'''

from movie import Movie

class MovieList:
    def __init__(self, not_watched, watched):
        self.notWatched = not_watched
        self.watched = watched

    def add_new_Movie(self, movie):
        self.not_watched.append(movie)

    def already_watched(self, movie):
        self.not_watched.remove(movie)
        self.watched.append(movie)

    def display_all(self):
        print("watched list")
        for i in self.not_watched:
            print(i.get_title())
        print("not watched list")
        for i in self.watched:
            print(i.get_title())

def main():
    arr1 = []
    arr2 = []

    movie1 = Movie("Titanic", 2)
    movie2= Movie("Titanic2", 2)
    movie3 = Movie("Titanic3", 2)

    movieList1 = MovieList(arr1, arr2)

    movieList1.add_new_Movie(movie1)
    movieList1.add_new_Movie(movie2)
    movieList1.add_new_Movie(movie3)

    # movieList1.displayAll()
    movieList1.already_watched(movie1)

    movieList1.display_all()



if __name__ == "__main__":
    main()
