# This file contains code for the class Movie, which holds 
# information about different movies.  Class Movie shows
# key details about movies to a user. 

import webbrowser

class Movie():
	"""Class Movie holds information about different movies"""
	
	def __init__(self, movie_title, movie_plot, movie_poster, movie_trailer):
		self.title = movie_title
		self.storyline = movie_plot
		self.poster_image_url = movie_poster
		self.trailer_youtube_url = movie_trailer
		
	def show_trailer(self):
		webbrowser.open(self.trailer_youtube_url)
		
	def detail_plot(self):
		print (self.storyline)
		
	
