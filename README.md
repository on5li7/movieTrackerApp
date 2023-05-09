# Blank template
The first thing to do is to add a `.gitignore` file

You should do this based off of the language, and you can find a list of [different gitignore files here](https://github.com/github/gitignore)

# Technical Debt Assignment
Read the [TechDebt](TechDebt.md) file. 

# General Overview
This app lets the user keep track of the shows and movies they are planning to watch or have already watched. They can rate the things they watch and leave comments. There are three lists (Unwatched, Currently Watching, and Watched) that the user can move their shows and movies around on. 

![image](Movie_Images\Menu.png "menu")

# Features Currently Implemented
There is a menu page that the user can choose a list out of three options: Watched, Plan to Watch, or Currently Watching.

When the user chooses a list they can switch to another list of their choice using the buttons on the top right. 
![image](Movie_Images\WatchedList.png "lists")

By clicking Add Movie the user can add a new show/movie and its rating, image path (to display an image) and comments.
![image](Movie_Images\AddMovie.png "add movie")

The user can switch a movie/show from Unwatched to Currently Watching or from Currently Watching to Watched. To do this, they click the green button on the top left of the movie/show. 
![image](Movie_Images\SwitchMovie.png "Switch Movie")

To view comments the user left, they click on the movie/show and an edit window pops up, showing the comment along with the title, image path, and rating. The edit feature is currently not implemented. 
![image](Movie_Images\ViewComments.png "View Comments")

# Instructions on Downloading the App
To use the app, the user runs the menu_page.py file of the project. This shows the menu, and the user can use the app however they like. 

# For More Info 

[Customer Notes](customerNotes.md)

[Traditional Report](TraditionalReport.md) 
