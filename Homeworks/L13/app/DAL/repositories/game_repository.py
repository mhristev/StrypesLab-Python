from DAL.parsers.game_parser import GameParser
from DAL.repositories.base_repository import BaseRepository

class GameRepository:
    def __init__(self):
        self.base_repository = BaseRepository()

    def create_game(self, title, release_date, genre, synopsis, image_path, developer_id, platform, multiplayer_mode):
        self.base_repository.cursor.execute("INSERT INTO Media (title, release_date, genre, synopsis, image_path) VALUES (?, ?, ?, ?, ?)",
                            (title, release_date, genre, synopsis, image_path))
        media_id = self.base_repository.cursor.lastrowid

        self.base_repository.cursor.execute("INSERT INTO Game (media_id, developer_id, platform, multiplayer_mode) VALUES (?, ?, ?, ?)",
                            (media_id, developer_id, platform, multiplayer_mode))

        self.base_repository.conn.commit()
        return media_id

    def get_game_by_id(self, game_id):
        self.base_repository.cursor.execute("""
            SELECT M.id, M.title, M.release_date, M.genre, M.synopsis, M.image_path,
                   D.id AS developer_id, D.name AS developer_name, G.platform, G.multiplayer_mode
            FROM Media M
            JOIN Game G ON M.id = G.media_id
            JOIN Developer D ON G.developer_id = D.id
            WHERE M.id = ?;
        """, (game_id,))
        result = self.base_repository.cursor.fetchall()
        return GameParser.parse_game_result(result)[0]

    def update_game(self, game_id, title, release_date, genre, synopsis, image_path, developer_id, platform, multiplayer_mode):
        self.base_repository.cursor.execute("""
            UPDATE Media SET title=?, release_date=?, genre=?, synopsis=?, image_path=?
            WHERE id=?;
        """, (title, release_date, genre, synopsis, image_path, game_id))

        self.base_repository.cursor.execute("""
            UPDATE Game SET developer_id=?, platform=?, multiplayer_mode=?
            WHERE media_id=?;
        """, (developer_id, platform, multiplayer_mode, game_id))

        self.base_repository.conn.commit()

    def get_games_by_title(self, title):
        title = "%" + title.lower() + "%"
        self.base_repository.cursor.execute("""
            SELECT M.id, M.title, M.release_date, M.genre, M.synopsis, M.image_path,
                   D.id AS developer_id, D.name AS developer_name, G.platform, G.multiplayer_mode
            FROM Media M
            JOIN Game G ON M.id = G.media_id
            JOIN Developer D ON G.developer_id = D.id
            WHERE LOWER(M.title) LIKE ?;
        """, (title,))
        result = self.base_repository.cursor.fetchall()
        return GameParser.parse_game_result(result)
    
    def get_games_by_genre(self, genre):
        genre = "%" + genre.lower() + "%"
        self.base_repository.cursor.execute("""
            SELECT M.id, M.title, M.release_date, M.genre, M.synopsis, M.image_path,
                   D.id AS developer_id, D.name AS developer_name, G.platform, G.multiplayer_mode
            FROM Media M
            JOIN Game G ON M.id = G.media_id
            JOIN Developer D ON G.developer_id = D.id
            WHERE LOWER(M.genre) LIKE ?;
        """, (genre,))
        result = self.base_repository.cursor.fetchall()
        return GameParser.parse_game_result(result)
    
    
    def delete_game(self, game_id):
        self.base_repository.cursor.execute("DELETE FROM Game WHERE media_id=?", (game_id,))
        self.base_repository.cursor.execute("DELETE FROM Media WHERE id=?", (game_id,))
        self.base_repository.conn.commit()

    def get_all_games(self):
        self.base_repository.cursor.execute("""
            SELECT M.id, M.title, M.release_date, M.genre, M.synopsis, M.image_path,
                   D.id AS developer_id, D.name AS developer_name, G.platform, G.multiplayer_mode
            FROM Media M
            JOIN Game G ON M.id = G.media_id
            JOIN Developer D ON G.developer_id = D.id;
        """)
        result = self.base_repository.cursor.fetchall()
        return GameParser.parse_game_result(result)
