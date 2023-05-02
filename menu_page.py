from graphics import *
import watched
import unwatched
import currently_watching

def main():
    # Create a graphics window
    win = GraphWin("Menu Page", 400, 450)

    
    # Set a background color
    win.setBackground("#c6e2e9")

    menu_label = Text(Point(200, 25), "My Movies and Shows")
    menu_label.setStyle("bold")
    menu_label.setFace("courier")
    menu_label.setSize(18)
    menu_label.draw(win)

    # Create buttons
    button1 = Rectangle(Point(100, 100), Point(300, 150))
    button1.setFill("lightgray")
    button1.draw(win)
    button1_label = Text(Point(200, 125), "Watched")
    button1_label.draw(win)

    button2 = Rectangle(Point(100, 200), Point(300, 250))
    button2.setFill("lightgray")
    button2.draw(win)
    button2_label = Text(Point(200, 225), "Plan to Watch")
    button2_label.draw(win)

    button3 = Rectangle(Point(100, 300), Point(300, 350))
    button3.setFill("lightgray")
    button3.draw(win)
    button3_label = Text(Point(200, 325), "Currently Watching")
    button3_label.draw(win)

    # Wait for a button to be clicked
    while True:
        click_point = win.getMouse()

        if button1.getP1().getX() <= click_point.getX() <= button1.getP2().getX() and \
                button1.getP1().getY() <= click_point.getY() <= button1.getP2().getY():
            # Button 1 is clicked
            win.close()
            watched.main()
            

        elif button2.getP1().getX() <= click_point.getX() <= button2.getP2().getX() and \
                button2.getP1().getY() <= click_point.getY() <= button2.getP2().getY():
            # Button 2 is clicked
            win.close()
            unwatched.main()
        
        elif button3.getP1().getX() <= click_point.getX() <= button3.getP2().getX() and \
                button3.getP1().getY() <= click_point.getY() <= button3.getP2().getY():
            # Button 2 is clicked
            win.close()
            currently_watching.main()
        

        else:
            # No button is clicked
            continue

if __name__ == "__main__":
    main()
