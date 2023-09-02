from BL.models.author import Author
from BL.models.book import Book

class BookParser:
    @staticmethod
    def parse_book_result(results):
        if results is None:
            return None
        books = []

        for result in results:
            media_id, title, release_date, genre, synopsis, image_path, author_id, author_name, page_count, language = result
        
            book = Book(
                id=media_id,
                title=title,
                author=Author(author_id, author_name),
                release_date=release_date,
                genre=genre,
                page_count=page_count,
                synopsis=synopsis,
                language=language,
                image_path=image_path
            )
            books.append(book)
        return books
        
        
        