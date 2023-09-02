from DAL.repositories.author_repository import AuthorRepository

class AuthorManager:
    def __init__(self):
        self.repository = AuthorRepository()
    
    def get_all_authors(self):
        return self.repository.get_all_authors()