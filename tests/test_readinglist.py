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
