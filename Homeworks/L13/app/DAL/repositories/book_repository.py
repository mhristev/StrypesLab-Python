import sqlite3
from DAL.parsers.book_parser import BookParser

class BookRepository:
    def __init__(self, db_file='media_manager.db'):
        self.db_file = db_file
        self.conn = None
        self.cursor = None

    def connect_to_db(self):
        self.conn = sqlite3.connect(self.db_file)
        self.cursor = self.conn.cursor()
        
    def create_book(self, title, release_date, genre, synopsis, image_path, author, page_count, language):
        self.connect_to_db()

        self.cursor.execute("INSERT INTO Media (title, release_date, genre, synopsis, image_path) VALUES (?, ?, ?, ?, ?)",
                            (title, release_date, genre, synopsis, image_path))
        media_id = self.cursor.lastrowid

        self.cursor.execute("INSERT INTO Book (media_id, author, page_count, language) VALUES (?, ?, ?, ?)",
                            (media_id, author, page_count, language))
        
        self.commit_close_db()
        return media_id

    def get_book(self, book_id):
        self.connect_to_db()
        self.cursor.execute("SELECT * FROM Book WHERE media_id=?", (book_id,))
        result = self.cursor.fetchone()
        self.commit_close_db()
        return BookParser.parse_book_result(result)

    def update_book(self, book_id, title, release_date, genre, synopsis, image_path, author, page_count, language):
        self.connect_to_db()
        self.cursor.execute("UPDATE Media SET title=?, release_date=?, genre=?, synopsis=?, image_path=? WHERE id=?",
                            (title, release_date, genre, synopsis, image_path, book_id))

        self.cursor.execute("UPDATE Book SET author=?, page_count=?, language=? WHERE media_id=?",
                            (author, page_count, language, book_id))
        self.commit_close_db()

    def delete_book(self, book_id):
        self.connect_to_db()
        self.cursor.execute("DELETE FROM Book WHERE media_id=?", (book_id,))
        self.cursor.execute("DELETE FROM Media WHERE id=?", (book_id,))
        self.commit_close_db()
        
    def get_all_books(self):
        self.connect_to_db()
        self.cursor.execute("SELECT * FROM Book")
        result = self.cursor.fetchall()
        self.commit_close_db()
        return BookParser.parse_book_result(result)
        

    def commit_close_db(self):
        self.conn.commit()
        self.conn.close()