import sqlalchemy

import readinglist
from readinglist import series, book, author


def test_list_readinglist(db_transaction):
    assert 1 == len(readinglist.readinglist.list_readinglists(db_transaction.connection))


def test_insert_readinglist(db_transaction):
    conn: sqlalchemy.engine.Connection = db_transaction.connection
    readinglist_name = 'Discworld'
    inserted = readinglist.readinglist.insert_readinglist(conn, readinglist_name)
    fetched = readinglist.readinglist.get_readinglist_by_name(conn, readinglist_name)
    assert inserted.id == fetched.id


def test_insert_remove_book(db_transaction):
    conn: sqlalchemy.engine.Connection = db_transaction.connection
    fantasy = readinglist.readinglist.get_readinglist_by_name(conn, 'Fantasy')
    on_list = readinglist.readinglist.get_books_on_readinglist(conn, fantasy)
    assert 4 == len(on_list)
    new_book = book.get_book_by_name(conn, '1Q84 Volume 1')
    readinglist.readinglist.add_book_to_readinglist(conn, fantasy, new_book)
    assert 5 == len(readinglist.readinglist.get_books_on_readinglist(conn, fantasy))
    readinglist.readinglist.remove_book_from_readinglist(conn, fantasy, new_book)
    assert 4 == len(readinglist.readinglist.get_books_on_readinglist(conn, fantasy))
