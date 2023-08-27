import sqlite3
from DAL.parsers.movie_parser import MovieParser

class MovieRepository:
    def __init__(self, db_file='media_manager.db'):
        self.db_file = db_file
        self.conn = None
        self.cursor = None

    def connect_to_db(self):
        self.conn = sqlite3.connect(self.db_file)
        self.cursor = self.conn.cursor()

    def create_movie(self, title, release_date, genre, synopsis, image_path, director, runtime_in_minutes, production_company, language, country):
        self.connect_to_db()

        self.cursor.execute("INSERT INTO Media (title, release_date, genre, synopsis, image_path) VALUES (?, ?, ?, ?, ?)",
                            (title, release_date, genre, synopsis, image_path))
        media_id = self.cursor.lastrowid

        self.cursor.execute("INSERT INTO Movie (media_id, director, runtime_in_minutes, production_company, language, country) VALUES (?, ?, ?, ?, ?, ?)",
                            (media_id, director, runtime_in_minutes, production_company, language, country))

        self.commit_close_db()
        return media_id

    def get_movie(self, movie_id):
        self.connect_to_db()
        self.cursor.execute("SELECT * FROM Movie WHERE media_id=?", (movie_id,))
        result = self.cursor.fetchone()
        self.commit_close_db()
        return MovieParser.parse_movie_result(result)

    def update_movie(self, movie_id, title, release_date, genre, synopsis, image_path, director, runtime_in_minutes, production_company, language, country):
        self.connect_to_db()
        self.cursor.execute("UPDATE Media SET title=?, release_date=?, genre=?, synopsis=?, image_path=? WHERE id=?",
                            (title, release_date, genre, synopsis, image_path, movie_id))

        self.cursor.execute("UPDATE Movie SET director=?, runtime_in_minutes=?, production_company=?, language=?, country=? WHERE media_id=?",
                            (director, runtime_in_minutes, production_company, language, country, movie_id))
        self.commit_close_db()

    def delete_movie(self, movie_id):
        self.connect_to_db()
        self.cursor.execute("DELETE FROM Movie WHERE media_id=?", (movie_id,))
        self.cursor.execute("DELETE FROM Media WHERE id=?", (movie_id,))
        self.commit_close_db()

    def get_all_movies(self):
        self.connect_to_db()
        self.cursor.execute("SELECT * FROM Movie")
        result = self.cursor.fetchall()
        self.commit_close_db()
        return MovieParser.parse_movie_result(result)

    def commit_close_db(self):
        self.conn.commit()
        self.conn.close()