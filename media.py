import webbrowser as wb


class Video():
	def __init__(self, title, duration):
		self.title = title
		self.duration = duration

class Movie(Video):
	valid_ratings = ["G", "PG", "PG-13", "R"]
	def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube, duration):
		Video.__init__(self, movie_title, duration)
		self.storyline = movie_storyline
		self.poster_image_url = poster_image
		self.trailer_youtube_url = trailer_youtube

	def show_trailer(self):
		wb.open(self.trailer_youtube_url)

class TvShow(Video):
	def __init__(self, title, season, episode, tv_station, duration):
		Video.__init__(self, title, duration)
		self.season = season
		self.episodes = episode
		self.tv_station = tv_station

	def get_local_listing(self):