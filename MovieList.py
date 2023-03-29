from movie import Movie

class MovieList:
    def __init__(self, notWatched, watched):
        self.notWatched = notWatched
        self.watched = watched

    def addNewMovie(self, movie):
        self.notWatched.append(movie)

    def alreadyWatched(self, movie):
        self.notWatched.remove(movie)
        self.watched.append(movie)

    def displayAll(self):
        print("watched list")
        for i in self.notWatched:
            print(i.getTitle())
        print("not watched list")
        for i in self.watched:
            print(i.getTitle())

def main():
    arr1 = []
    arr2 = []

    movie1 = Movie("Titanic", 2)
    movie2= Movie("Titanic2", 2)
    movie3 = Movie("Titanic3", 2)

    movieList1 = MovieList(arr1, arr2)

    movieList1.addNewMovie(movie1)
    movieList1.addNewMovie(movie2)
    movieList1.addNewMovie(movie3)

    # movieList1.displayAll()
    movieList1.alreadyWatched(movie1)

    movieList1.displayAll()



if __name__ == "__main__":
    main()


