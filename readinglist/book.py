import sqlalchemy
from sqlalchemy.sql import text

import typing

from . import author, reading_status, review, series


class Book():
    def __init__(self, id, title, status):
        self.id = id
        self.title = title
        self.status = status

    @staticmethod
    def from_db_row(row):
        return Book(int(row[0]),
                    row[1],
                    reading_status.Status.from_id(int(row[2])))

    def attach_joined_attributes(self, conn: sqlalchemy.engine.Connection):
        self.authors = get_authors_for_book(conn, self)
        self.review = review.get_review_for_book(conn, self)
        self.series = get_series(conn, self)


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
                status: reading_status.Status):
    insertion = conn.execute(text('insert into books values (NULL, :title, :status)'),
                             title=title,
                             status=status.id)
    book_id = insertion.lastrowid
    for i, authorr in enumerate(authors):
        conn.execute(text('insert into book_author values (:book_id, :author_id, :index)'),
                     book_id=book_id,
                     author_id=authorr.id,
                     index=i)
    return Book(book_id, title, status)


def delete_book(conn,
                bookk):
    conn.execute(text('delete from books where id = :book_id'),
                 book_id=bookk.id)


def get_authors_for_book(conn: sqlalchemy.engine.Connection,
                         bookk: Book) -> typing.List[author.Author]:
    rows = conn.execute(text('select authors.id, author_name '
                             'from authors inner join book_author on author_id = id '
                             'where book_id = :book_id'),
                        book_id=bookk.id)
    return [author.Author.from_db_row(row) for row in rows]


def get_series(conn: sqlalchemy.engine.Connection,
               bookk: Book) -> typing.List[series.Series]:
    result = conn.execute(text('select series.id, series_name '
                               'from series inner join book_series on book_id = id '
                               'where book_id = :book_id'),
                          book_id=bookk.id).fetchone()
    return None if result is None else series.Series.from_db_row(result)


def get_books_by_reading_status(conn: sqlalchemy.engine.Connection,
                                status: reading_status.Status) -> typing.List[Book]:
    rows = conn.execute(text('select * from books '
                             'where status = :status'),
                        status=status.id)
    return [Book.from_db_row(row) for row in rows]


def set_book_status(conn: sqlalchemy.engine.Connection,
                    bookk: Book,
                    new_status: reading_status.Status):
    conn.execute(text('update books set status = :status_id where id = :book_id'),
                 book_id=bookk.id,
                 status_id=new_status.id)
