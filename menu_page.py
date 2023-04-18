from graphics import *
import watched
import unwatched

def main():
    # Create a graphics window
    win = GraphWin("Menu Page", 400, 400)

    # Set a background color
    win.setBackground("white")

    # Create buttons
    button1 = Rectangle(Point(100, 100), Point(300, 150))
    button1.setFill("lightgray")
    button1.draw(win)
    button1_label = Text(Point(200, 125), "Watched List")
    button1_label.draw(win)

    button2 = Rectangle(Point(100, 200), Point(300, 250))
    button2.setFill("lightgray")
    button2.draw(win)
    button2_label = Text(Point(200, 225), "Unwatched List")
    button2_label.draw(win)

    # Wait for a button to be clicked
    while True:
        click_point = win.getMouse()

        if button1.getP1().getX() <= click_point.getX() <= button1.getP2().getX() and \
                button1.getP1().getY() <= click_point.getY() <= button1.getP2().getY():
            # Button 1 is clicked
            watched.main()
            

        elif button2.getP1().getX() <= click_point.getX() <= button2.getP2().getX() and \
                button2.getP1().getY() <= click_point.getY() <= button2.getP2().getY():
            # Button 2 is clicked
            unwatched.main()

        else:
            # No button is clicked
            continue

if __name__ == "__main__":
    main()
