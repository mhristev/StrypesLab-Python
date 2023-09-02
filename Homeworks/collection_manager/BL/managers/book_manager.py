from DAL.repositories.author_repository import AuthorRepository
from DAL.repositories.book_repository import BookRepository

class BookManager:
    def __init__(self):
        self.repository = BookRepository()
        self.author_repository = AuthorRepository()

    def create_book(self, book):
        author_id = 0
        if book.author.id == None:
            author_id = self.author_repository.create_author(book.author.name)
        else:
            author_id = book.author.id
        return self.repository.create_book(title=book.title, release_date=book.release_date, genre=book.genre, \
            synopsis=book.synopsis, image_path=book.image_path, author_id=author_id, page_count=book.page_count, language=book.language
            )

    def get_books_by_title(self, title):
        return self.repository.get_books_by_title(title)
    
    def get_books_by_genre(self, genre):
        return self.repository.get_books_by_genre(genre)
    
    def get_book_by_id(self, book_id):
        return self.repository.get_book_by_id(book_id)

    def update_book(self, book):
        author_id = 0
        if book.author.id == None:
            author_id = self.author_repository.create_author(book.author.name)
        else:
            author_id = book.author.id
        self.repository.update_book(book.id, book.title, book.release_date, book.genre, book.synopsis, book.image_path, author_id, book.page_count, book.language)
        

    def delete_book(self, book_id):
        self.repository.delete(book_id)
    
    def get_all_books(self):
        return self.repository.get_all_books()
    
    def close(self):
        self.repository.close()