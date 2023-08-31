from DAL.repositories.base_repository import BaseRepository

class DirectorRepository:
    def __init__(self):
        self.base_repository = BaseRepository()

    def create_director(self, name):
        self.base_repository.cursor.execute("INSERT INTO Director (name) VALUES (?)", (name, ))
        director_id = self.base_repository.cursor.lastrowid
        
        self.base_repository.conn.commit()
        return director_id

    def get_all_directors(self):
        self.base_repository.cursor.execute("SELECT * FROM Director")
        results = self.base_repository.cursor.fetchall()
        return results