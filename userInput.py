from graphics import *

win = GraphWin("Save Inputs", 400, 300)

# create an Entry widget for user input
title_input = Entry(Point(200, 100), 30)
title_input.draw(win)

# create a Text widget to display saved inputs
saved_text = Text(Point(200, 200), "")
saved_text.draw(win)

# create a button to save input to Text widget
save_button = Rectangle(Point(150, 150), Point(250, 175))
save_button_text = Text(Point(200, 162.5), "Save Input")
save_button.draw(win)
save_button_text.draw(win)

# main loop to wait for user input and handle button clicks
while True:
    click = win.getMouse()
    
    # check if save button was clicked
    if (click.getX() >= 150 and click.getX() <= 250
        and click.getY() >= 150 and click.getY() <= 175):
        
        # save input to Text widget
        saved_text.setText(title_input.getText())
    
    # check if window was closed
    elif click == None:
        break

win.close()
