from DAL.repositories.movie_repository import MovieRepository

class MovieManager:
    def __init__(self, db_path):
        self.repository = MovieRepository(db_path)

    def add_movie(self, movie):
        self.repository.insert(movie)

    def get_movie_by_id(self, movie_id):
        return self.repository.get_by_id(movie_id)

    def update_movie(self, movie_id, movie):
        self.repository.update(movie_id, [movie.title, movie.director, movie.release_date, movie.genre, movie.runtime, movie.synopsis, movie.production_company, movie.language, movie.country, movie.image, movie.trailer])

    def delete_movie(self, movie_id):
        self.repository.delete(movie_id)

    def get_all_movies(self):
        return self.repository.get_all_movies()
    
    def close(self):
        self.repository.close()
