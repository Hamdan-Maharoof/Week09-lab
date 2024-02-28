import unittest
from book_manager import Book, BookManager

class TestBookManager(unittest.TestCase):
    def setUp(self):
        self.book1 = Book("1234567890", "Book1", "Author1")
        self.book2 = Book("2345678901", "Book2", "Author2")
        self.book3 = Book("3456789012", "Book3", "Author3")
        self.book_manager = BookManager()

    def test_add_book(self):
        self.book_manager.add_book(self.book1)
        self.assertEqual(len(self.book_manager.books), 1)
        self.book_manager.add_book(self.book2)
        self.assertEqual(len(self.book_manager.books), 2)
        self.book_manager.add_book(self.book1)  # Adding the same book again
        self.assertEqual(len(self.book_manager.books), 2)

    def test_remove_book(self):
        self.book_manager.add_book(self.book1)
        self.book_manager.add_book(self.book2)
        self.book_manager.remove_book("1234567890")
        self.assertEqual(len(self.book_manager.books), 1)
        self.assertEqual(self.book_manager.books[0].isbn, "2345678901")
        self.book_manager.remove_book("1234567890")  # Trying to remove a non-existent book
        self.assertEqual(len(self.book_manager.books), 1)

    def test_list_books(self):
        self.book_manager.add_book(self.book1)
        self.book_manager.add_book(self.book2)
        self.book_manager.add_book(self.book3)
        books = self.book_manager.list_books()
        self.assertEqual(len(books), 3)
        self.assertIn(self.book1, books)
        self.assertIn(self.book2, books)
        self.assertIn(self.book3, books)

if __name__ == '__main__':
    unittest.main()
