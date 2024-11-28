import unittest
from library_manager.book_manager import BookManager

class TestBookManager(unittest.TestCase):
    def setUp(self):
        self.book_manager = BookManager('test_books.json')

    def tearDown(self):
        import os
        if os.path.exists('test_books.json'):
            os.remove('test_books.json')

    def test_add_book(self):
        self.book_manager.add_book("Test Title", "Test Author", 2023)
        books = self.book_manager.load_books()
        self.assertEqual(len(books), 1)
        self.assertEqual(books[0]['title'], "Test Title")

    def test_delete_book(self):
        self.book_manager.add_book("Test Title", "Test Author", 2023)
        self.book_manager.delete_book(1)
        books = self.book_manager.load_books()
        self.assertEqual(len(books), 0)

    def test_search_books(self):
        self.book_manager.add_book("Test Title", "Test Author", 2023)
        results = self.book_manager.search_books(title="Test Title")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]['title'], "Test Title")

    def test_change_book_status(self):
        self.book_manager.add_book("Test Title", "Test Author", 2023)
        self.book_manager.change_book_status(1, "выдана")
        books = self.book_manager.load_books()
        self.assertEqual(books[0]['status'], "выдана")

if __name__ == '__main__':
    unittest.main()
