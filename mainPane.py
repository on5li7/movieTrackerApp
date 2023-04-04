'''
This displays the unwatch movie list.
'''

from graphics import *
from movie_list import MovieList
from movie import Movie

# public movie list
global movies_list
movies_list = []

def run_app():
    # create a window
    win = GraphWin("Movie List", 900, 600)

    # create a list of movies
    global movies_list

    movie_objects = []
    for i, movie in enumerate(movies_list):
        # create rectangle
        rect = Rectangle(Point(50, 30 + i*60), Point(350, 80 + i*60))
        rect.setOutline("black")
        rect.draw(win)

                # create star polygon
        rating = int(movie.get_rating())
        for j in range(rating):
            star = Polygon(
                Point(360 + j*70, 40 + i*60),
                Point(370 + j*70, 60 + i*60),
                Point(390 + j*70, 60 + i*60),
                Point(375 + j*70, 70 + i*60),
                Point(385 + j*70, 90 + i*60),
                Point(360 + j*70, 80 + i*60),
                Point(335 + j*70, 90 + i*60),
                Point(345 + j*70, 70 + i*60),
                Point(330 + j*70, 60 + i*60),
                Point(350 + j*70, 60 + i*60)
            )
            star.setFill("yellow")
            star.draw(win)


        # create text object
        text = Text(Point(200, 55 + i*60), f"{i+1}. {movie.get_title()}")
        text.setSize(16)
        text.draw(win)
        # store both objects in a list
        movie_objects.append((rect, star, text))

    # wait for user input
    win.getMouse()

    # close the window
    win.close()


def create_movie_list():
    global movies_list
    # movie_data_list = [] # getting all movie data

    with open('movieData.txt', 'r') as file:
        lines = [line.strip() for line in file.readlines()]

    for line in lines:
        data = line.split(",")
        movie = Movie(data[0], data[1])
        movies_list.append(movie)
        # movie_data_list.append(data)



def main():
    create_movie_list()
    run_app()
    



if __name__ == '__main__':
    main()