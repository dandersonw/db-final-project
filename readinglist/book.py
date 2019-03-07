import sqlalchemy
from sqlalchemy.sql import text

import typing

from . import author


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


def get_book_by_name(conn: sqlalchemy.engine.Connection,
                     name: str) -> typing.Optional[Book]:
    result = conn.execute(text('select * from books where title = :name'),
                          name=name)\
                 .fetchone()
    return None if result is None else Book.from_db_row(result)


def list_books(conn: sqlalchemy.engine.Connection) -> typing.List[Book]:
    rows = conn.execute('select * from books').fetchall()
    return [Book.from_db_row(row) for row in rows]


def insert_book(conn: sqlalchemy.engine.Connection,
                title: str,
                authors: typing.List[author.Author],
                status: int):  # TODO: make status an enum or something
    insertion = conn.execute(text('insert into books values (NULL, :title, :status)'),
                             title=title,
                             status=status)
    book_id = insertion.lastrowid
    for i, authorr in enumerate(authors):
        conn.execute(text('insert into book_author values (:book_id, :author_id, :index)'),
                     book_id=book_id,
                     author_id=authorr.id,
                     index=i)
    return Book(book_id, title, status)


def get_authors(conn: sqlalchemy.engine.Connection,
                book: Book) -> typing.List[author.Author]:
    rows = conn.execute(text('select authors.id, author_name '
                             'from authors inner join book_author on author_id = id '
                             'where book_id = :book_id'),
                        book_id=book.id)
    return [author.Author.from_db_row(row) for row in rows]
