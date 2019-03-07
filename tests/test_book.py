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
    authors = book.get_authors(conn, all_books[-1])
    assert authors[0].id == authorr.id


def test_update_status(db_transaction):
    conn = db_transaction.connection
    bookk = book.get_book_by_name(conn, 'Good Omens')
    assert bookk.status == reading_status.UNSET
    book.update_book_status(conn, bookk, reading_status.WANT_TO_READ)
    bookk = book.get_book_by_name(conn, 'Good Omens')
    assert bookk.status == reading_status.WANT_TO_READ
