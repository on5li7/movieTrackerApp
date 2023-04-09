class movie_functions:
    def __init__(self, title, rating, genre):
        self.title = title  # store the title of the movie
        self.rating = rating  # store the rating of the movie
        self.genre = genre  # store the genre of the movie

def add_movie_to_recently_watched(movie, recently_watched):
    recently_watched.append(movie)  # add the movie object to the recently_watched list
    return recently_watched  # return the updated list

def print_recently_watched(recently_watched):
    if len(recently_watched) == 0:
        print("You haven't watched any movies recently.")
    else:
        print("Recently watched movies:")
        for i, movie in enumerate(recently_watched):  # loop through the recently_watched list
            print(f"{i+1}. {movie.title} ({movie.rating}/10) - {movie.genre}")  # print each movie's title, rating, and genre
