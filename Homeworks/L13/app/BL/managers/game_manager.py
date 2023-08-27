from DAL.repositories.game_repository import GameRepository

class GameManager:
    def __init__(self, db_path):
        self.repository = GameRepository(db_path)

    def add_game(self, game):
        self.repository.insert(game)

    def get_game_by_id(self, game_id):
        return self.repository.get_by_id(game_id)

    def update_game(self, game):
        self.repository.update(game.id, [game.title, game.genre, game.release_date, game.developer, game.platform, game.synopsis, game.multiplayer_mode, game.price, game.image])

    def delete_game(self, game_id):
        self.repository.delete(game_id)
    
    def get_all_games(self):
        return self.repository.get_all_games()

    def close(self):
        self.repository.close()
