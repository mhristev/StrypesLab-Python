from BL.models.book import Book

class BookParser:
    @staticmethod
    def parse_book_result(result):
        if result is None:
            return None

        media_id, title, release_date, genre, synopsis, image_path, author, page_count, language = result
        
        return Book(
            media_id,
            title,
            author,
            release_date,
            genre,
            page_count,
            synopsis,
            language,
            image_path
        )