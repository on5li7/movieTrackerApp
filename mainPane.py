'''
This displays the unwatch movie list.
'''

from graphics import *
from movie_list import MovieList

# create a window
win = GraphWin("Movie List", 900, 600)

# create a list of movies
movies = ["The Shawshank Redemption", "The Godfather", "The Dark Knight", "The Godfather: Part II", "12 Angry Men"]

movie_objects = []
for i, movie in enumerate(movies):
    # create rectangle
    rect = Rectangle(Point(50, 30 + i*60), Point(350, 80 + i*60))
    rect.setOutline("black")
    rect.draw(win)
    # create text object
    text = Text(Point(200, 55 + i*60), f"{i+1}. {movie}")
    text.setSize(16)
    text.draw(win)
    # store both objects in a list
    movie_objects.append((rect, text))

# wait for user input
win.getMouse()

# close the window
win.close()
