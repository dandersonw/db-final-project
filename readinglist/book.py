import sqlite3

import typing

from .author import Author


class Book():
    def __init__(self, id, title, status):
        self.id = id
        self.title = title
        self.status = status

    @staticmethod
    def from_db_row(row):
        return Book(int(row[0]),
                    row[1],
                    int(row[2]))


def list_books(cursor: sqlite3.Cursor) -> typing.List[Book]:
    rows = cursor.execute('select * from books').fetchall()
    return [Book.from_db_row(row) for row in rows]


def insert_book(cursor: sqlite3.Cursor,
                title: str,
                authors: typing.List[Author],
                status: int):  # TODO: make status an enum or something
    cursor.execute('insert into books values (NULL, ?, ?)', (title, status))
    book_id = cursor.lastrowid
    for i, authorr in enumerate(authors):
        cursor.execute('insert into book_author values (?, ?, ?)',
                       (book_id,
                        authorr.id,
                        i))
    return Book(book_id, title, status)


def get_authors(cursor: sqlite3.Cursor,
                book: Book) -> typing.List[Author]:
    rows = cursor.execute('select authors.id, author_name '
                          'from authors inner join book_author on author_id = id '
                          'where book_id = ?',
                          (book.id,))
    return [Author.from_db_row(row) for row in rows]
