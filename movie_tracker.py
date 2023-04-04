from movie_functions import Movie, add_movie_to_recently_watched, print_recently_watched

# create a list to hold recently watched movies
recently_watched = []

# create a new Movie object
movie1 = Movie("The Shawshank Redemption", 9.3, "Drama")
movie2 = Movie("The Godfather", 9.2, "Crime")
movie3 = Movie("The Dark Knight", 9.0, "Action")

# add the movie to the recently watched list
recently_watched = add_movie_to_recently_watched(movie1, recently_watched)
recently_watched = add_movie_to_recently_watched(movie2, recently_watched)
recently_watched = add_movie_to_recently_watched(movie3, recently_watched)

# print the recently watched movies
print_recently_watched(recently_watched)
