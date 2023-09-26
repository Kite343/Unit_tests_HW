from book_repository import BookRepository


class BookService:
    def __init__(self, book_repository: BookRepository):
        self._book_repository = book_repository

    def get_all_books(self):
        return self._book_repository.get_books()
    
    def get_book(self, id):
        return self._book_repository.get_book_by_id(id)