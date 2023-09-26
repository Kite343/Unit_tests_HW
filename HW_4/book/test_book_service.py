import unittest
from unittest.mock import patch
from book_service import BookService

class TestBookService(unittest.TestCase):
    @patch('book_repository.BookRepository')
    def test_book_service(self, mock_book):
        self.book_service = BookService(mock_book)
        book_id = 7
        self.book_service.get_book(book_id)
        self.book_service.get_all_books()
        self.book_service._book_repository.get_book_by_id.assert_called_once_with(book_id)
        self.book_service._book_repository.get_books.assert_called_once_with()
    
if __name__ == '__main__':
    unittest.main(verbosity=2)