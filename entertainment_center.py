import media, fresh_tomatoes

# List that holds the names of movies that will be shown on the webpage
movieTitles = ["Mr. and Mrs. Smith", "Titanic", "Edward Scissorhands", "The Dark Knight", "Maze Runner", "Billy Elliot"]

# Creates a list of Movie objects using the provided titles.  Using this method, movie title can be added/removed
# from the moviesTitle list without having to change any other code
moviesList = [media.Movie(movieTitles[i]) for i in range(0,len(movieTitles))]

# Passes the moviesList list to the fresh_tomatoes.py which populates the page with information
fresh_tomatoes.open_movies_page(moviesList)