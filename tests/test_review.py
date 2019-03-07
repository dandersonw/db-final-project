import sqlalchemy
import pytest

from readinglist import book, review


def test_list_reviews(db_transaction):
    assert 2 == len(review.list_reviews(db_transaction.connection))


def test_insert_review(db_transaction):
    conn = db_transaction.connection
    bookk = book.get_book_by_name(conn, '1Q84 Volume 3')
    review.insert_review(conn,
                         bookk,
                         'The most intriguing yet',
                         4.5)
    with pytest.raises(sqlalchemy.exc.IntegrityError):
        # inserting a review for a book that already has a review
        review.insert_review(conn,
                             bookk,
                             'The most intriguing yet',
                             4.5)
    with pytest.raises(sqlalchemy.exc.OperationalError):
        bookk = book.get_book_by_name(conn, '1Q84 Volume 4')
        review.insert_review(conn,
                             bookk,
                             'Too intriguing',
                             5.1)


def test_remove_review(db_transaction):
    conn = db_transaction.connection
    bookk = book.get_book_by_name(conn, '1Q84 Volume 2')
    fetch = review.get_review_for_book(conn, bookk)
    assert fetch is not None
    review.remove_review(conn, fetch)
    assert review.get_review_for_book(conn, bookk) is None
