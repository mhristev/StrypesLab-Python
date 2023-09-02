from DAL.repositories.director_repository import DirectorRepository

class DirectorManager:
    def __init__(self):
        self.repository = DirectorRepository()
        
    def get_all_directors(self):
        return self.repository.get_all_directors()