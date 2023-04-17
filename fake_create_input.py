from graphics import *
# from movie_list import MovieList
from movie import Movie
import time

def f():

    win2 = GraphWin("User Inputs", 850, 600, autoflush=False)

    # create an Entry widget for user input
    title_input_text = Text(Point(200, 70), "Enter Movie Title")
    title_input = Entry(Point(200, 100), 30)
    title_input.setFill("white")
    title_input.draw(win2)
    title_input_text.draw(win2)

    star_input_text = Text(Point(200, 170), "Enter Movie Star (1-5)")
    star_input = Entry(Point(200, 200), 30)
    star_input.setFill("white")
    star_input.draw(win2)
    star_input_text.draw(win2)

    comment_input_text = Text(Point(600, 70), "Enter Your Comments")
    comment_input = Entry(Point(600, 100), 30)
    comment_input.setFill("white")
    comment_input.draw(win2)
    comment_input_text.draw(win2)

    path_input_text = Text(Point(600, 170), "Enter Path to the Image")
    path_input = Entry(Point(600, 200), 30)
    path_input.setFill("white")
    path_input.draw(win2)
    path_input_text.draw(win2)

    # create a Text variable to save inputs
    saved_text = ''

    # create a button to save input to Text widget
    save_button = Rectangle(Point(350, 300), Point(450, 325))
    save_button_text = Text(Point(400, 310), "Save Input")
    save_button.draw(win2)
    save_button_text.draw(win2)

    # main loop to wait for user input and handle button clicks
    while True:
        click = win2.getMouse()
        
        # check if save button was clicked
        if (click.getX() >= 350 and click.getX() <= 450
            and click.getY() >= 300 and click.getY() <= 325):
            
            # save input to Text widget
            saved_text = title_input.getText() + ',' + star_input.getText() + ',' + comment_input.getText() +',' + path_input.getText()+'\n'
            print(saved_text)
            with open('movieData.txt', 'a') as file:
                file.write(saved_text)
            file.close()
            break
            # win2.close()
            # refresh_main_page()
            
            # win2.close()
        # check if window was closed
        elif click == None:
            break


    win2.close()


# f()