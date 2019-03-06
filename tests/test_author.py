import unittest
import pytest

from readinglist import book, author


@pytest.mark.usefixtures("db_class")
class MyTest(unittest.TestCase):
    def test_list_authors(self):
        assert 3 == len(author.list_authors(self.db.cursor()))

    def test_insert_book(self):
        cursor = self.db.cursor()
        cursor.execute('begin')
        name = 'Brandon Sanderson'
        inserted = author.insert_author(cursor, name)
        got = author.get_author_by_name(cursor, name)
        assert got.id == inserted.id
        cursor.execute('rollback')

    def test_get_author_by_name(self):
        cursor = self.db.cursor()
        assert None == author.get_author_by_name(cursor, 'Cincinnatus')
        assert 1 == author.get_author_by_name(cursor, 'Haruki Murakami').id
