from .media import Media
from .director import Director

class Movie(Media):
    def __init__(self, id=0, title="", director=Director(0, ""), release_date="", genre="", runtime_in_minutes=0, synopsis="", language="", country="", image_path=""):
        super().__init__(id, title, release_date, genre, synopsis, image_path)
        self.director = director
        self.runtime_in_minutes = runtime_in_minutes
        self.language = language
        self.country = country