from .media import Media

class Book(Media):
    def __init__(self, id, title, author, release_date, genre, page_count, synopsis, language, image_path):
        super().__init__(id, title, release_date, genre, synopsis, image_path)
        self.author = author
        self.page_count = page_count
        self.language = language    