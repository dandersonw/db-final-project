from readinglist import author


def test_list_authors(db_transaction):
    assert 4 == len(author.list_authors(db_transaction.connection))


def test_insert_author(db_transaction):
    conn = db_transaction.connection
    name = 'Brandon Sanderson'
    inserted = author.insert_author(conn, name)
    got = author.get_author_by_name(conn, name)
    assert got.id == inserted.id


def test_get_author_by_name(db_transaction):
    conn = db_transaction.connection
    assert author.get_author_by_name(conn, 'Cincinnatus') is None
    assert 1 == author.get_author_by_name(conn, 'Haruki Murakami').id
