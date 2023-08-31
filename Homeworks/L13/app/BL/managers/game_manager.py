from DAL.repositories.developer_repository import DeveloperRepository
from DAL.repositories.game_repository import GameRepository

class GameManager:
    def __init__(self):
        self.repository = GameRepository()
        self.developer_repository = DeveloperRepository()

    def create_game(self, game):
        creator_id = 0
        if game.developer.id == None:
            creator_id = self.developer_repository.create_developer(game.developer.name)
        else:
            creator_id = game.developer.id
        
        return self.repository.create_game(title=game.title, release_date=game.release_date, genre=game.genre, \
            synopsis=game.synopsis, image_path=game.image_path, developer_id=creator_id, platform=game.platform, multiplayer_mode=game.multiplayer_mode
            )
    
    def get_games_by_title(self, title):
        return self.repository.get_games_by_title(title)
    
    def get_games_by_genre(self, genre):
        return self.repository.get_games_by_genre(genre)
    
    def get_game_by_id(self, game_id):
        return self.repository.get_game_by_id(game_id)

    def update_game(self, game):
        creator_id = 0
        if game.developer.id == None:
            creator_id = self.developer_repository.create_developer(game.developer.name)
        else:
            creator_id = game.developer.id
        
        self.repository.update_game(game.id, game.title, game.release_date, game.genre, game.synopsis, game.image_path, creator_id, game.platform, int(game.multiplayer_mode))
        

    def delete_game(self, game_id):
        self.repository.delete(game_id)
    
    def get_all_games(self):
        return self.repository.get_all_games()

    def close(self):
        self.repository.close()
