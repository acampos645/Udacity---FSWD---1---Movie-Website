# Imports the Python requests library which can be used to make get requests
# from databases
import requests

# API key for 'The Movie Database'
api = "c573688971f5f68e0bad00d000fac7ae"

# Each movie title that is listed in entertainment_center.py will be used to create
# a new object of the Movie class
class Movie():

	# When each object is created, the __init__ function will take in the title
	# and use the information to request data from themoviedb.org
	def __init__(self, title):
		self.title = title

		# Uses the provided movie title to search for the movie ID in the TheMovieDB
		self.movieID = findID(self.title)

		# The resulting ID is used to find a URL for the movie's poster/trailer
		self.moviePoster, self.movieTrailer = findPosterTrailer(self.movieID)

# Global method that searches for a movie's ID using TheMovieDB.org's api
def findID(title):

	# A JSON object is requested using themoviedb's api.  The api key is passed in as a paramtery and the 
	# Movie object's title is used as the query
	movieResponse = requests.get("http://api.themoviedb.org/3/search/movie", {'api_key':api, 'query':title})

	# The json() method from the requests library is used to decode the response as JSON.  The movie
	# idea is extracted from this and returned as a string
	return str(movieResponse.json()['results'][0]['id'])

# Global method that searches for a movie's trailer and poster using the ID from findID
def findPosterTrailer(movieID):

	# The movieID is used to contruct a new request URL.  Just as before, the response is decoded
	# using the request library json() method
	requestURL = "http://api.themoviedb.org/3/movie/" + movieID
	movieResponse = requests.get(requestURL, {'api_key':api, 'append_to_response':'videos'})
	movieResponse = movieResponse.json()

	# The moviePoster URL is constructed by extracting the 'poster_path' data
	moviePoster = "http://image.tmdb.org/t/p/w342/" + movieResponse['poster_path']

	# The trailer URL is constructed by extracting the YouTube key from the returned 'video' data
	trailerURL = "http://www.youtube.com/watch?v=" + movieResponse['videos']['results'][0]['key']

	# Returns strings representing the URL of the movie poster and trailer URLs
	return moviePoster, trailerURL