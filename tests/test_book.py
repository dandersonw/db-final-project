import unittest
import pytest

from readinglist import book, author


@pytest.mark.usefixtures("db_class")
class MyTest(unittest.TestCase):
    def test_list_books(self):
        assert 5 == len(book.list_books(self.db.cursor()))

    def test_insert_book(self):
        cursor = self.db.cursor()
        cursor.execute('begin')
        authorr = author.get_author_by_name(cursor, 'Terry Pratchett')
        title = 'Equal Rites'
        book.insert_book(cursor, title, [authorr], 1)
        all_books = book.list_books(cursor)
        assert 6 == len(all_books)
        assert all_books[-1].title == title
        authors = book.get_authors(cursor, all_books[-1])
        assert authors[0].id == authorr.id
        cursor.execute('rollback')
