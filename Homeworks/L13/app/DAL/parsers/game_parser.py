from BL.models.developer import Developer
from BL.models.game import Game

class GameParser:
    @staticmethod
    def parse_game_result(results):
        games = []

        for result in results:
            media_id, title, release_date, genre, synopsis, image_path, \
            dev_id, developer_name, platform, multiplayer_mode = result
            
            game = Game(
                id=media_id,
                title=title, 
                developer=Developer(dev_id, developer_name),
                release_date=release_date,
                genre=genre,
                platform=platform,
                multiplayer_mode=bool(multiplayer_mode),
                synopsis=synopsis,
                image_path=image_path
            )
            games.append(game)

        return games