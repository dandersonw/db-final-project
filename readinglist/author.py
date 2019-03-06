import sqlite3

import typing


class Author():
    def __init__(self, id, name):
        self.id = id
        self.name = name

    @staticmethod
    def from_db_row(row):
        return Author(int(row[0]),
                      row[1])


def get_author_by_name(cursor: sqlite3.Cursor,
                       name: str) -> typing.Optional[Author]:
    q_template = 'select * from authors where author_name = ?'
    result = cursor.execute(q_template, (name,)).fetchone()
    return None if result is None else Author.from_db_row(result)


def list_authors(conn: sqlite3.Connection) -> typing.List[Author]:
    rows = conn.execute('select * from authors').fetchall()
    return [Author.from_db_row(row) for row in rows]


def insert_author(cursor: sqlite3.Cursor,
                  name: str):
    cursor.execute('insert into authors values (NULL, ?)', (name,))
    author_id = cursor.lastrowid
    return Author(author_id, name)
