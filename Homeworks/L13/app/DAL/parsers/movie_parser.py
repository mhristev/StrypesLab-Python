from BL.models.movie import Movie

class MovieParser:
    @staticmethod
    def parse_movie_result(result):
        if result is None:
            return None

        media_id, title, release_date, genre, synopsis, image_path, director, runtime_in_minutes, production_company, language, country = result
        
        return Movie(
            media_id,
            title,
            director,
            release_date,
            genre,
            runtime_in_minutes,
            synopsis,
            production_company,
            language,
            country,
            image_path
        )