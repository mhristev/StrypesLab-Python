from DAL.repositories.base_repository import BaseRepository

class DeveloperRepository:
    def __init__(self):
        self.base_repository = BaseRepository()

    def create_developer(self, name):
        self.base_repository.cursor.execute("INSERT INTO Developer (name) VALUES (?)", (name, ))
        dev_id = self.base_repository.cursor.lastrowid

        self.base_repository.conn.commit()
        return dev_id

    def get_developer_by_id(self, dev_id):
        self.base_repository.cursor.execute("SELECT * FROM Developer WHERE id=?", (dev_id))
        result = self.base_repository.cursor.fetchone()
        return result

    def get_all_developers(self):
        self.base_repository.cursor.execute("SELECT * FROM Developer")
        results = self.base_repository.cursor.fetchall()
        return results