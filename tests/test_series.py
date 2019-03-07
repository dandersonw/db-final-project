import sqlalchemy

from readinglist import series, book, author, reading_status


def test_list_series(db_transaction):
    assert 2 == len(series.list_series(db_transaction.connection))


def test_insert_series(db_transaction):
    conn: sqlalchemy.engine.Connection = db_transaction.connection
    authorr = author.get_author_by_name(conn, 'Terry Pratchett')
    series_name = 'Discworld'
    book_titles = ['The Color of Magic', 'Lights Fantastic']
    books = [book.insert_book(conn, title, [authorr], reading_status.UNSET)
             for title in book_titles]
    inserted = series.insert_series(conn, series_name, [authorr], books)
    fetched = series.get_series_by_name(conn, series_name)
    assert inserted.id == fetched.id
