'''
This class is for the movie object
'''

class Movie:
    def __init__(self, title='', rating = 0):
        self.title = title
        self.rating = rating

    def getTitle(self):
        return self.title

    def setRating(self, rating):
        self.rating = rating

    def getRating(self):
        return self.rating
    