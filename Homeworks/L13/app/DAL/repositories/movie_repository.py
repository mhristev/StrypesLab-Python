from DAL.parsers.movie_parser import MovieParser
from DAL.repositories.base_repository import BaseRepository

class MovieRepository:
    def __init__(self):
        self.base_repository = BaseRepository()
    
    def insert_movie(self, title, release_date, genre, synopsis, image_path, director_id, runtime_in_minutes, language, country):
        
        self.base_repository.cursor.execute("INSERT INTO Media (title, release_date, genre, synopsis, image_path) VALUES (?, ?, ?, ?, ?)",
                            (title, release_date, genre, synopsis, image_path))
        media_id = self.cursor.lastrowid

        self.base_repository.cursor.execute("INSERT INTO Movie (media_id, director_id, runtime_in_minutes, language, country) VALUES (?, ?, ?, ?, ?)",
                            (media_id, director_id, runtime_in_minutes, language, country))

        self.base_repository.conn.commit()
        return media_id

    def get_movie_by_id(self, movie_id):
        self.base_repository.cursor.execute("""
            SELECT M.id, M.title, M.release_date, M.genre, M.synopsis, M.image_path, D.id as director_id,
                   D.name AS director_name, B.runtime_in_minutes, B.language, B.country
            FROM Media M
            JOIN Movie B ON M.id = B.media_id
            JOIN Director D ON B.director_id = D.id
            WHERE M.id = ?;
        """, (movie_id,))
        result = self.base_repository.cursor.fetchall()
        return MovieParser.parse_movie_result(result)[0]

    def update_movie(self, movie_id, title, release_date, genre, synopsis, image_path, director_id, runtime_in_minutes,language, country):
        self.base_repository.cursor.execute("""
            UPDATE Media SET title=?, release_date=?, genre=?, synopsis=?, image_path=?
            WHERE id=?;
        """, (title, release_date, genre, synopsis, image_path, movie_id))

        self.base_repository.cursor.execute("""
            UPDATE Movie SET director_id=?, runtime_in_minutes=?, language=?, country=?
            WHERE media_id=?;
        """, (director_id, runtime_in_minutes, language, country, movie_id))

        self.base_repository.conn.commit()

    def delete_movie(self, movie_id):
        self.base_repository.cursor.execute("DELETE FROM Movie WHERE media_id=?", (movie_id,))
        self.base_repository.cursor.execute("DELETE FROM Media WHERE id=?", (movie_id,))
        self.base_repository.conn.commit()

    def get_movies_by_title(self, title):
        title = "%" + title.lower() + "%"
        self.base_repository.cursor.execute("""
            SELECT M.id, M.title, M.release_date, M.genre, M.synopsis, M.image_path, D.id as director_id,
                   D.name AS director_name, B.runtime_in_minutes, B.language, B.country
            FROM Media M
            JOIN Movie B ON M.id = B.media_id
            JOIN Director D ON B.director_id = D.id
            WHERE LOWER(M.title) LIKE ?
        """, (title,))
        result = self.base_repository.cursor.fetchall()
        return MovieParser.parse_movie_result(result)
    
    def get_movies_by_genre(self, genre):
        genre = "%" + genre.lower() + "%"
        self.base_repository.cursor.execute("""
            SELECT M.id, M.title, M.release_date, M.genre, M.synopsis, M.image_path, D.id as director_id,
                   D.name AS director_name, B.runtime_in_minutes, B.language, B.country
            FROM Media M
            JOIN Movie B ON M.id = B.media_id
            JOIN Director D ON B.director_id = D.id
            WHERE LOWER(M.genre) LIKE ?
        """, (genre,))
        result = self.base_repository.cursor.fetchall()
        return MovieParser.parse_movie_result(result)
    
    def get_all_movies(self):
        self.base_repository.cursor.execute("""
            SELECT M.id, M.title, M.release_date, M.genre, M.synopsis, M.image_path, D.id as director_id,
                   D.name AS director_name, B.runtime_in_minutes, B.language, B.country
            FROM Media M
            JOIN Movie B ON M.id = B.media_id
            JOIN Director D ON B.director_id = D.id;
        """)
        result = self.base_repository.cursor.fetchall()
        return MovieParser.parse_movie_result(result)