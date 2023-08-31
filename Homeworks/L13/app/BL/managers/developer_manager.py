from DAL.repositories.developer_repository import DeveloperRepository

class DeveloperManager:
    def __init__(self):
        self.repository = DeveloperRepository()
    
    def get_all_developers(self):
        return self.repository.get_all_developers()