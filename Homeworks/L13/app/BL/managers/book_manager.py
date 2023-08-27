import sys
import os
parent_dir = sys.path.append(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(parent_dir)

from DAL.repositories.book_repository import BookRepository

class BookManager:
    def __init__(self, db_path):
        self.repository = BookRepository(db_path)

    def add_book(self, book):
        self.repository.insert(book)

    def get_book_by_id(self, book_id):
        return self.repository.get_by_id(book_id)

    def update_book(self, book):
        self.repository.update(book.id, [book.title, book.author, book.release_date, book.genre, book.page_count, book.synopsis, book.language, book.image])

    def delete_book(self, book_id):
        self.repository.delete(book_id)
    
    def get_all_books(self):
        return self.repository.get_all_books()
    
    def close(self):
        self.repository.close()