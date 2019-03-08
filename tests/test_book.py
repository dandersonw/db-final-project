from readinglist import book, author, reading_status


def test_list_books(db_transaction):
    assert 8 == len(book.list_books(db_transaction.connection))


def test_insert_book(db_transaction):
    conn = db_transaction.connection
    authorr = author.get_author_by_name(conn, 'Terry Pratchett')
    title = 'Equal Rites'
    book.insert_book(conn, title, [authorr], reading_status.UNSET)
    all_books = book.list_books(conn)
    assert 9 == len(all_books)
    assert all_books[-1].title == title
    authors = book.get_authors_for_book(conn, all_books[-1])
    assert authors[0].id == authorr.id


def test_update_status(db_transaction):
    conn = db_transaction.connection
    bookk = book.get_book_by_name(conn, 'Good Omens')
    assert bookk.status == reading_status.UNSET
    book.set_book_status(conn, bookk, reading_status.WANT_TO_READ)
    bookk = book.get_book_by_name(conn, 'Good Omens')
    assert bookk.status == reading_status.WANT_TO_READ

    want_to_read = book.get_books_by_reading_status(conn, reading_status.WANT_TO_READ)
    assert 1 == len(want_to_read)
    assert 'Good Omens' == want_to_read[0].title


def test_attach_joined_attributes(db_transaction):
    conn = db_transaction.connection
    bookk = book.get_book_by_name(conn, 'Good Omens')
    bookk.attach_joined_attributes(conn)
    assert bookk.series is None
    assert bookk.review is None
    assert 'Terry Pratchett' == bookk.authors[0].name \
        and 'Neil Gaiman' == bookk.authors[1].name
