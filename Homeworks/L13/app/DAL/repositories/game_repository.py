import sqlite3
from DAL.parsers.game_parser import GameParser

class GameRepository:
    def __init__(self, db_file='media_manager.db'):
        self.db_file = db_file
        self.conn = None
        self.cursor = None

    def connect_to_db(self):
        self.conn = sqlite3.connect(self.db_file)
        self.cursor = self.conn.cursor()

    def create_game(self, title, release_date, genre, synopsis, image_path, developer, platform, multiplayer_mode):
        self.connect_to_db()

        self.cursor.execute("INSERT INTO Media (title, release_date, genre, synopsis, image_path) VALUES (?, ?, ?, ?, ?)",
                            (title, release_date, genre, synopsis, image_path))
        media_id = self.cursor.lastrowid

        self.cursor.execute("INSERT INTO Game (media_id, developer, platform, multiplayer_mode) VALUES (?, ?, ?, ?)",
                            (media_id, developer, platform, multiplayer_mode))

        self.commit_close_db()
        return media_id

    def get_game(self, game_id):
        self.connect_to_db()
        self.cursor.execute("SELECT * FROM Game WHERE media_id=?", (game_id,))
        result = self.cursor.fetchone()
        self.commit_close_db()
        return GameParser.parse_game_result(result)

    def update_game(self, game_id, title, release_date, genre, synopsis, image_path, developer, platform, multiplayer_mode):
        self.connect_to_db()
        self.cursor.execute("UPDATE Media SET title=?, release_date=?, genre=?, synopsis=?, image_path=? WHERE id=?",
                            (title, release_date, genre, synopsis, image_path, game_id))

        self.cursor.execute("UPDATE Game SET developer=?, platform=?, multiplayer_mode=? WHERE media_id=?",
                            (developer, platform, multiplayer_mode, game_id))
        self.commit_close_db()

    def delete_game(self, game_id):
        self.connect_to_db()
        self.cursor.execute("DELETE FROM Game WHERE media_id=?", (game_id,))
        self.cursor.execute("DELETE FROM Media WHERE id=?", (game_id,))
        self.commit_close_db()

    def get_all_games(self):
        self.connect_to_db()
        self.cursor.execute("SELECT * FROM Game")
        result = self.cursor.fetchall()
        self.commit_close_db()
        return GameParser.parse_game_result(result)

    def commit_close_db(self):
        self.conn.commit()
        self.conn.close()