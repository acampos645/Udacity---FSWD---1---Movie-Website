import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
						" A story of his boys and his toys that come to life",
						"https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
						"https://www.youtube.com/watch?v=vwyZH85NQC4")

avatar = media.Movie("Avatar",
					 "A marine on an alien planet",
					 "http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg",
					 "https://www.youtube.com/watch?v=5PSNL1qE6VY")

school_of_rock = media.Movie("Shool of Rock",
							 "Storyline",
							 "http://static.rogerebert.com/uploads/movie/movie_poster/school-of-rock-2003/large_cREN222Yw78zvSQ9bg17Y9QZS0c.jpg",
							 "https://www.youtube.com/watch?v=XCwy6lW5Ixc")

movies = [toy_story, avatar, school_of_rock]
fresh_tomatoes.open_movies_page(movies)