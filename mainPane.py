from graphics import *

win = GraphWin("My Graphics Window", 900, 900)
win.setBackground("white")

# Draw a rectangle
rect = Rectangle(Point(100, 100), Point(200, 200))
rect.setFill("red")
rect.draw(win)

# Draw a circle
circle = Circle(Point(300, 300), 50)
circle.setFill("blue")
circle.draw(win)

# Wait for the user to click the window
win.getMouse()

# Close the window
win.close()