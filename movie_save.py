import os
def save_movie_data():
    # Create a directory named "movie_data" if it doesn't already exist
    if not os.path.exists("movie_data"):
        os.mkdir("movie_data")

# Open the file in append mode, so that new data  is added without overwriting the old data

with open("movieData.txt", "a") as file:
    # Get user input
    movie_title = input("Enter movie title: ")
    movie_rating = input("Enter movie rating (out of 5): ")
    movie_comment = input("Enter comment: ")
    movie_image_path = input("Enter movie image: ")


    # Write the user input to the file
    file.write(f"{movie_title},{movie_rating},{movie_comment},{movie_image_path}\n")

# Open the file again in read mode to display the saved data

with open("movie_data/movieData.txt", "r") as file:    # Read the lines in the file and display them
    for line in file:
        # Split the line by commas to separate the movie data
        movie_data = line.strip().split(",")
        print(f"Title: {movie_data[0]}")
        print(f"Rating: {movie_data[1]}/5")
        print(f"Comment: {movie_data[2]}")
        print(f"Image Path: {movie_data[3]}")
        print()
