import cv2 
from graphics import *

enter_movie_pic = input("Enter an image name (full pathname required): ")
enter_movie_name = input("Enter movie name: ")

img = cv2.imread(enter_movie_pic)

cv2.imshow("Movie Poster", img)

cv2.waitKey(0)

cv2.destroyAllWindows()

cv2.imwrite("Movie_Images/" + enter_movie_name + ".jpg", img)