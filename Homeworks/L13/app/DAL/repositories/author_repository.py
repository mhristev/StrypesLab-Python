from DAL.repositories.base_repository import BaseRepository

class AuthorRepository:
    def __init__(self):
        self.base_repository = BaseRepository()

    def create_author(self, name):
        self.base_repository.cursor.execute("INSERT INTO Author (name) VALUES (?)", (name,))
        author_id = self.cursor.lastrowid

        self.base_repository.conn.commit()
        return author_id

    def get_author(self, author_id):
        self.base_repository.cursor.execute("SELECT * FROM Author WHERE id=?", (author_id))
        result = self.base_repository.cursor.fetchone()
        return result

    def get_all_authors(self):
        self.base_repository.cursor.execute("SELECT * FROM Author")
        results = self.base_repository.cursor.fetchall()
        return results