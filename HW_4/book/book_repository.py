# from abc import ABC, abstractmethod

# class BookRepository(ABC):
#     @abstractmethod
#     def get_book_by_id(self, book_id):
#         pass

#     @abstractmethod
#     def get_books(self, book_id):
#         pass

from book import Book

class BookRepository:
    def __init__(self, books: dict[int: Book]):
        self.books = books

    def get_book_by_id(self, book_id):
        return self.books.get(book_id)

    def get_books(self):
        return self.books.values()
    
# if __name__ == '__main__':
#     a = BookRepository({1: Book(2,'tyuu', 'hyyf'),
#                          2: Book(2,'tyuu', 'hyyf')})
#     print(*a.get_books())
