import sqlalchemy
from sqlalchemy.sql import text

import typing

from . import book


class Review():
    def __init__(self, book_id, review_text, rating):
        self.book_id = book_id
        self.review_text = review_text
        self.rating = rating

    @staticmethod
    def from_db_row(row):
        return Review(int(row[0]),
                      row[1],
                      float(row[2]))


def list_reviews(conn: sqlalchemy.engine.Connection) -> typing.List[Review]:
    rows = conn.execute('select * from reviews').fetchall()
    return [Review.from_db_row(row) for row in rows]


def insert_review(conn: sqlalchemy.engine.Connection,
                  bookk: book.Book,
                  review_text: str,
                  rating: float):  # TODO: make status an enum or something
    conn.execute(text('insert into reviews values (:book_id, :review_text, :rating)'),
                 book_id=bookk.id,
                 review_text=review_text,
                 rating=rating)
    return Review(bookk.id, review_text, rating)


def get_review_for_book(conn: sqlalchemy.engine.Connection,
                        bookk: book.Book) -> typing.Optional[Review]:
    result = conn.execute(text('select book_id, review_text from '
                               'books join reviews on book_id = id '
                               'where book_id = :book_id'),
                          book_id=bookk.id).fetchone()
    return None if result is None else Review.from_db_row(result)
