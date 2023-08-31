from DAL.repositories.movie_repository import MovieRepository
from DAL.repositories.director_repository import DirectorRepository
class MovieManager:
    def __init__(self):
        self.repository = MovieRepository()
        self.director_repository = DirectorRepository()

    def create_movie(self, movie):
        director_id = 0
        if movie.director.id == None:
            director_id = self.director_repository.create_director(movie.director.name)
        else:
            director_id = movie.director.id
        return self.repository.insert_movie(movie.title, movie.release_date, movie.genre, movie.synopsis, movie.image_path, director_id, movie.runtime_in_minutes, movie.language, movie.country)

    def get_movies_by_title(self, title):
        return self.repository.get_movies_by_title(title)
    
    def get_movies_by_genre(self, genre):
        return self.repository.get_movies_by_genre(genre)
    
    def get_movie_by_id(self, movie_id):
        return self.repository.get_movie_by_id(movie_id)

    def update_movie(self, movie):
        director_id = 0
        if movie.director.id == None:
            director_id = self.director_repository.create_director(movie.director.name)
        else:
            director_id = movie.director.id
        
        self.repository.update_movie(movie.id, movie.title, movie.release_date, movie.genre, movie.synopsis, movie.image_path, director_id, movie.runtime_in_minutes, movie.language, movie.country)

    def delete_movie(self, movie_id):
        self.repository.delete_movie(movie_id)

    def get_all_movies(self):
        return self.repository.get_all_movies()
    
    def close(self):
        self.repository.close()
