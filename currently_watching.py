from graphics import *
# from movie_list import MovieList
from movie import Movie
import time
import menu_page

# public movie list
global movies_list
movies_list = []
global movie_coords
movie_coords = []

RECTANGLE_WIDTH = 150
RECTANGLE_HEIGHT = 200
MARGIN_X = 50
MARGIN_Y = 50
SPACING_X = 50
SPACING_Y = 70

def run_app():
    # create a window
    # root1 = tk.Tk()
    win = GraphWin("NOT WATCHED Movie List", 1050, 600, autoflush=False)
    win.setBackground("dark grey")

     #create add movie button
    add_movie_button = Rectangle(Point(900, 10), Point(1000, 35))
    add_movie_button_text = Text(Point(950, 22), "Add Movie")
    add_movie_button.draw(win)
    add_movie_button_text.draw(win)

    #create a back to menu button
    back_to_menu_button = Rectangle(Point(750, 10), Point(850, 35))
    back_to_menu_button_text = Text(Point(800, 22), "Menu")
    back_to_menu_button.draw(win)
    back_to_menu_button_text.draw(win)

    # create a list of movies
    global movies_list
    global movie_coords

    movie_objects = []
    rectangles = []
    for i, movie in enumerate(movies_list):
        x = MARGIN_X + (i % 5) * (RECTANGLE_WIDTH + SPACING_X)
        y = MARGIN_Y + (i // 5) * (RECTANGLE_HEIGHT + SPACING_Y)

        img = Image(Point(x + RECTANGLE_WIDTH/2, y + RECTANGLE_HEIGHT/2), movie.get_image_path())
        img.draw(win)

        rect = Rectangle(Point(x, y), Point(x + RECTANGLE_WIDTH, y + RECTANGLE_HEIGHT))
        movie_coords.append([x, x + RECTANGLE_WIDTH, y, y + RECTANGLE_HEIGHT])
        #rect.setFill(color_rgb(200, 200, 200))
        rect.draw(win)
        rectangles.append(rect)
        # create movie title
        title = Text(Point(x + RECTANGLE_WIDTH / 2, y + RECTANGLE_HEIGHT + 15), f"{i+1}. {movie.get_title()}")
        title.setSize(12)
        title.setTextColor("white")
        title.draw(win)
       