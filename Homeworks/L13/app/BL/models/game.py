from .media import Media
    
class Game(Media):
    def __init__(self, id, title, genre, release_date, developer, platform, synopsis, multiplayer_mode, price, image):
        super().__init__(id, title, release_date, genre, synopsis, image)
        self.developer = developer
        self.platform = platform
        self.multiplayer_mode = multiplayer_mode