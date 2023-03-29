'''
This class is for the movie object
'''

class Movie:
    def __init__(self, title='', rating = 0):
        self.title = title
        self.rating = rating

    def get_title(self):
        return self.title

    def set_rating(self, rating):
        self.rating = rating

    def get_rating(self):
        return self.rating
    