from DAL.parsers.book_parser import BookParser
from DAL.repositories.base_repository import BaseRepository

class BookRepository:
    def __init__(self):
        self.base_repository = BaseRepository()

    def create_book(self, title, release_date, genre, synopsis, image_path, author_id, page_count, language):
        self.base_repository.cursor.execute("INSERT INTO Media (title, release_date, genre, synopsis, image_path) VALUES (?, ?, ?, ?, ?)",
                            (title, release_date, genre, synopsis, image_path))
        media_id = self.base_repository.cursor.lastrowid

        self.base_repository.cursor.execute("INSERT INTO Book (media_id, author_id, page_count, language) VALUES (?, ?, ?, ?)",
                            (media_id, author_id, page_count, language))

        self.base_repository.conn.commit()
        return media_id

    def get_book_by_id(self, book_id):
        self.base_repository.cursor.execute("""
            SELECT M.id, M.title, M.release_date, M.genre, M.synopsis, M.image_path,
                   A.id as author_id, A.name AS author_name, B.page_count, B.language
            FROM Media M
            JOIN Book B ON M.id = B.media_id
            JOIN Author A ON B.author_id = A.id
            WHERE M.id = ?;
        """, (book_id,))
        result = self.base_repository.cursor.fetchall()
        return BookParser.parse_book_result(result)[0]

    def update_book(self, book_id, title, release_date, genre, synopsis, image_path, author_id, page_count, language):
        self.base_repository.cursor.execute("""
            UPDATE Media SET title=?, release_date=?, genre=?, synopsis=?, image_path=?
            WHERE id=?;
        """, (title, release_date, genre, synopsis, image_path, book_id))

        self.base_repository.cursor.execute("""
            UPDATE Book SET author_id=?, page_count=?, language=?
            WHERE media_id=?;
        """, (author_id, page_count, language, book_id))

        self.base_repository.conn.commit()

    def get_books_by_title(self, title):
        title = "%" + title.lower() + "%"
        self.base_repository.cursor.execute("""
            SELECT M.id, M.title, M.release_date, M.genre, M.synopsis, M.image_path,
                   A.id as author_id, A.name AS author_name, B.page_count, B.language
            FROM Media M
            JOIN Book B ON M.id = B.media_id
            JOIN Author A ON B.author_id = A.id
            WHERE LOWER(M.title) LIKE ?
        """, (title,))
        result = self.base_repository.cursor.fetchall()
        return BookParser.parse_book_result(result)
    
    def get_books_by_genre(self, genre):
        genre = "%" + genre.lower() + "%"
        self.base_repository.cursor.execute("""
            SELECT M.id, M.title, M.release_date, M.genre, M.synopsis, M.image_path,
                   A.id as author_id, A.name AS author_name, B.page_count, B.language
            FROM Media M
            JOIN Book B ON M.id = B.media_id
            JOIN Author A ON B.author_id = A.id
            WHERE LOWER(M.genre) LIKE ?
        """, (genre, ))
        result = self.base_repository.cursor.fetchall()
        return BookParser.parse_book_result(result)
    
    def delete_book(self, book_id):
        self.base_repository.cursor.execute("DELETE FROM Book WHERE media_id=?", (book_id,))
        self.base_repository.cursor.execute("DELETE FROM Media WHERE id=?", (book_id,))
        self.base_repository.conn.commit()

    def get_all_books(self):
        self.base_repository.cursor.execute("""
            SELECT M.id, M.title, M.release_date, M.genre, M.synopsis, M.image_path,
                   A.id as author_id, A.name AS author_name, B.page_count, B.language
            FROM Media M
            JOIN Book B ON M.id = B.media_id
            JOIN Author A ON B.author_id = A.id;
        """)
        result = self.base_repository.cursor.fetchall()
        return BookParser.parse_book_result(result)
