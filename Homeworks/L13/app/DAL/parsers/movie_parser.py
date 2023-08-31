from BL.models.movie import Movie
from BL.models.director import Director

class MovieParser:
    @staticmethod
    def parse_movie_result(results):
        movies = []
        for result in results:
            media_id, title, release_date, genre, synopsis, image_path, director_id, director_name, \
            runtime_in_minutes, language, country = result
            
            movie = Movie(
                media_id,
                title,
                Director(director_id, director_name),
                release_date,
                genre,
                runtime_in_minutes,
                synopsis,
                language,
                country,
                image_path
            )
            movies.append(movie)

        return movies