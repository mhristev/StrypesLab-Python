from .media import Media

class Movie(Media):
    def __init__(self, id, title, director, release_date, genre, runtime_in_minutes, synopsis, production_company, language, country, image, trailer):
        super().__init__(id, title, release_date, genre, synopsis, image)
        self.director = director
        self.runtime_in_minutes = runtime_in_minutes
        self.production_company = production_company
        self.language = language
        self.country = country