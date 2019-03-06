import unittest
import pytest

from readinglist import book


@pytest.mark.usefixtures("db_class")
class MyTest(unittest.TestCase):
    def test_list_books(self):
        assert 5 == len(book.list_books(self.db))

    def test_insert_book(self):
        title = 'Equal Rites'
        book.insert_book(self.db, title, 1)
        all_books = book.list_books(self.db)
        assert 6 == len(all_books)
        assert all_books[-1].title == title
        self.db.rollback()
