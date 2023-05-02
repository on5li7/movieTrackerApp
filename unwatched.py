from graphics import *
# from movie_list import MovieList
from movie import Movie
import time
import menu_page
import watched
import currently_watching

# public movie list
global movies_list
movies_list = []
global movie_coords
movie_coords = []
global button_coords
button_coords = []

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
    win.setBackground("#c6e2e9")

    win_label = Text(Point(150,10), "Planning to Watch")
    win_label.setFace("courier")
    win_label.setStyle("bold")
    win_label.setSize(18)
    win_label.draw(win)

     #create add movie button
    add_movie_button = Rectangle(Point(900, 10), Point(1000, 35))
    add_movie_button.setFill("light gray")
    add_movie_button_text = Text(Point(950, 22), "Add Movie")
    add_movie_button.draw(win)
    add_movie_button_text.draw(win)

    #create a back to menu button
    #back_to_menu_button = Rectangle(Point(750, 10), Point(850, 35))
    #back_to_menu_button.setFill("light gray")
    #back_to_menu_button_text = Text(Point(800, 22), "Menu")
    #back_to_menu_button.draw(win)
    #back_to_menu_button_text.draw(win)

    #create watched button
    watched_button = Rectangle(Point(750, 10), Point(850, 35))
    watched_button.setFill("light gray")
    watched_button_text = Text(Point(800, 22), "Watched")
    watched_button.draw(win)
    watched_button_text.draw(win)

    #create current button
    current_button = Rectangle(Point(600, 10), Point(700, 35))
    current_button.setFill("light gray")
    current_button_text = Text(Point(650, 22), "Current")
    current_button.draw(win)
    current_button_text.draw(win)

    #create edit movie button
    edit_button = Rectangle(Point(450, 10), Point(550, 35))
    edit_button.setFill("light gray")
    edit_button_text = Text(Point(500, 22), "Edit")
    edit_button.draw(win)
    edit_button_text.draw(win)

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
        title.setTextColor("black")
        title.draw(win)

        watched_button = Rectangle(Point(x+25, y-15),  Point(x, y))
        button_coords.append([x, x+25, y, y-15])
        watched_button.setFill('green')
        watched_button.draw(win)
       
        # create star polygon
        #rating = int(movie.get_rating())
        #for j in range(rating):
            #star = Polygon(
                #Point(x + 25 + j*25, y + 170), #top 40
                #Point(x + 28 + j*25, y + 177),
                #Point(x + 35 + j*25, y + 177), #right
                #Point(x + 30 + j*25, y + 182),
                #Point(x + 31 + j*25, y + 190), #bot right
                #Point(x + 25 + j*25, y + 185),
                #Point(x + 19 + j*25, y + 190), #bot left
                #Point(x + 20 + j*25, y + 182),
                #Point(x + 15 + j*25, y + 177), #left
                #Point(x + 22 + j*25, y + 177)
            #)
            #star.setFill("yellow")
            #star.draw(win)

        # store both objects in a list
        #movie_objects.append((rect, star, Text))
        movie_objects.append((rect,Text))

    print("Coordinates of the movie rectangles", movie_coords)
    # wait for user input
    win.getMouse()

    while True:
        click = win.getMouse()
        if (click.getX() >= 900 and click.getX() <= 1000 and click.getY() >= 10 and click.getY() <= 35):
            win.delete("all")
            win.close()
            create_input_page()
        for i in range(len(movie_coords)):
            if click.getX() >= movie_coords[i][0] and click.getX() <= movie_coords[i][1] and click.getY() >= movie_coords[i][2] and click.getY() <= movie_coords[i][3]:
                show_comments(i)  # Close the window
        for i in range(len(button_coords)):
            if click.getX() >= button_coords[i][0] and click.getX() <= button_coords[i][1] and click.getY() <= button_coords[i][2] and click.getY() >= button_coords[i][3]:
                line_to_delete = i
                with open('notWatchedMovieData.txt', 'r') as file:
                    lines = file.readlines()
                file.close()
                with open('notWatchedMovieData.txt', "w") as f:
                    for i, line in enumerate(lines):
                        if i != line_to_delete:
                            f.write(line)
                        else:
                            with open('watchedMovieData.txt', "a") as watched_f:
                                watched_f.write(line)
                win.close()
                refresh_main_page()
                f.close()
                watched_f.close()


        if (click.getX() >= 450 and click.getX() <= 550 and click.getY() >= 10 and click.getY() <= 35):
            win.delete("all")
            win.close()
            edit_movie_page()


        if (click.getX() >= 750 and click.getX() <= 850 and click.getY() >= 10 and click.getY() <= 35):
            win.close()
            movie_coords.clear()
            movies_list.clear()
            watched.main()
        if (click.getX() >= 600 and click.getX() <= 700 and click.getY() >= 10 and click.getY() <= 35):
            win.close()
            movie_coords.clear()
            movies_list.clear()
            currently_watching.main()

            

        # elif click == None:
        #     break

        
    # close the window
    win.close()
    # root1.destroy()


def create_movie_list():
    global movies_list
    # movie_data_list = [] # getting all movie data

    with open('notWatchedMovieData.txt', 'r+') as file:
        lines = [line.strip() for line in file.readlines()]

    for line in lines:
        data = line.split(",")
        print(data)
        movie = Movie(data[0], data[1], data[2],  data[3])
        movies_list.append(movie)
        # movie_data_list.append(data)
    file.close()

def create_input_page():

    win2 = GraphWin("User Inputs", 850, 600, autoflush=False)

    win2.setBackground("#c6e9d9")

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
    save_button.setFill("light gray")
    save_button_text.draw(win2)

    #create a back button 
    back_button = Rectangle(Point(350, 400), Point(450, 425))
    back_button_text = Text(Point(400, 410), "Back")
    back_button.draw(win2)
    back_button.setFill("light gray")
    back_button_text.draw(win2)

    # main loop to wait for user input and handle button clicks
    while True:
        click = win2.getMouse()
        
        # check if save button was clicked
        if (click.getX() >= 350 and click.getX() <= 450
            and click.getY() >= 300 and click.getY() <= 325):
            
            # save input to Text widget
            saved_text = title_input.getText() + ',' + star_input.getText() + ',' + comment_input.getText() +',' + path_input.getText()+'\n'
            print(saved_text)
            with open('notWatchedMovieData.txt', 'a') as file:
                file.write(saved_text)
            file.close()
            win2.close()
            refresh_main_page()
        
        if (click.getX() >= 350 and click.getX() <= 450 
            and click.getY() >= 400 and click.getY() <= 425):
            win2.close()
            refresh_main_page()
            
            # win2.close()
        # check if window was closed
        elif click == None:
            break


    win2.close()

#rerun the main page and update global variables
def refresh_main_page():
    global movies_list
    movies_list.clear()
    movie_coords.clear()
    button_coords.clear()
    create_movie_list()
    run_app()

# def show_comments(i):
#     win_comment = GraphWin("Comment Window", 1000, 200)
#     comment = Text(Point(700, 50), movies_list[i].get_comment())
#     comment.draw(win_comment)
#     time.sleep(2)

#     win_comment.close()

def show_comments(i):
    win_comment = GraphWin("Comment Window", 500, 200)

    win_comment.setBackground("#d8c6e9")

    comment = Text(Point(250, 100), movies_list[i].get_comment())
    comment.setSize(18)
    comment.setStyle("bold")
    comment.draw(win_comment)

    # Add a close button to the comment window
    close_button = Rectangle(Point(480, 10), Point(500, 30))
    close_button.setFill("red")
    close_button.draw(win_comment)
    close_label = Text(Point(490, 20), "X")
    close_label.setStyle("bold")
    close_label.draw(win_comment)

    while True:
        click = win_comment.getMouse()
        if click.getX() >= 480 and click.getX() <= 500 and click.getY() >= 10 and click.getY() <= 30:
            # Clicked the close button, so close the comment window and return to main window
            win_comment.close()
            return

def edit_movie_page():

    win2 = GraphWin("Edit Movie", 850, 600, autoflush=False)

    # create an Entry widget for user input
    title_input_text = Text(Point(200, 70), "Edit Movie Title")
    title_input = Entry(Point(200, 100), 30)
    title_input.setFill("white")
    title_input.draw(win2)
    title_input_text.draw(win2)

    star_input_text = Text(Point(200, 170), "Edit Movie Star (1-5)")
    star_input = Entry(Point(200, 200), 30)
    star_input.setFill("white")
    star_input.draw(win2)
    star_input_text.draw(win2)

    comment_input_text = Text(Point(600, 70), "Edit Your Comments")
    comment_input = Entry(Point(600, 100), 30)
    comment_input.setFill("white")
    comment_input.draw(win2)
    comment_input_text.draw(win2)

    path_input_text = Text(Point(600, 170), "Edit Path to the Image")
    path_input = Entry(Point(600, 200), 30)
    path_input.setFill("white")
    path_input.draw(win2)
    path_input_text.draw(win2)

    # create a Text variable to save inputs
    saved_text = ''

    # create a button to save input to Text widget
    save_button = Rectangle(Point(325, 300), Point(475, 325))
    save_button_text = Text(Point(400, 310), "Save Changes")
    save_button.draw(win2)
    save_button_text.draw(win2)

    #create a back button 
    back_button = Rectangle(Point(350, 400), Point(450, 425))
    back_button_text = Text(Point(400, 410), "Back")
    back_button.draw(win2)
    back_button_text.draw(win2)

    # main loop to wait for user input and handle button clicks
    while True:
        click = win2.getMouse()
        
        # check if save button was clicked
        if (click.getX() >= 350 and click.getX() <= 450
            and click.getY() >= 300 and click.getY() <= 325):
            
            # save input to Text widget
            saved_text = title_input.getText() + ',' + star_input.getText() + ',' + comment_input.getText() +',' + path_input.getText()+'\n'
            print(saved_text)
            with open('watchedMovieData.txt', 'a') as file:
                file.write(saved_text)
            file.close()
            win2.close()
            # refresh_main_page()

        if (click.getX() >= 350 and click.getX() <= 450 
            and click.getY() >= 400 and click.getY() <= 425):
            win2.close()
            refresh_main_page()
            
            # win2.close()
        # check if window was closed
        elif click == None:
            break

    win2.close()


def main():
    create_movie_list()
    run_app()
    
    



if __name__ == '__main__':
    main()


# spiderman,4,liked,Movie_Images/The_Last_Jedi_resized.png
# spider man,3,asdasdasda,Movie_Images/Spider Man_resized.png