import cv2 
from graphics import *
from PIL import Image

enter_movie_pic = input("Enter an image name (full pathname required): ")
enter_movie_name = input("Enter movie name: ")

img = Image.open(enter_movie_pic)
new_path_name = "Movie_Images/" + enter_movie_name + ".png"
new_img = img.save(new_path_name)

image = cv2.imread(new_path_name, cv2.IMREAD_UNCHANGED)
print('original dimensions: ', image.shape)

WIDTH = 150
HEIGHT = 200
DIM = (WIDTH, HEIGHT)

final_resize = cv2.resize(image, DIM, interpolation=cv2.INTER_AREA)
print('changed dimensions: ',final_resize.shape)

cv2.imshow("resized image", final_resize)
cv2.imwrite("Movie_Images/" + enter_movie_name + "_resized.png", final_resize)

cv2.waitKey(0)
cv2.destroyAllWindows()

#img = cv2.imread(enter_movie_pic)

#cv2.imshow("Movie Poster", img)

#cv2.waitKey(0)

#cv2.destroyAllWindows()

#cv2.imwrite("Movie_Images/" + enter_movie_name + ".jpg", img)