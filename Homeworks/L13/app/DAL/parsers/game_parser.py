from BL.models.game import Game

class GameParser:
    @staticmethod
    def parse_game_result(result):
        if result is None:
            return None

        media_id, title, release_date, genre, synopsis, image_path, developer, platform, multiplayer_mode = result
        
        return Game(
            media_id,
            title,
            genre,
            release_date,
            developer,
            platform,
            synopsis,
            bool(multiplayer_mode),
            image_path
        )