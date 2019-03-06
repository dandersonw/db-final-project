import sqlalchemy
from sqlalchemy.sql import text

import typing


class Author():
    def __init__(self, id, name):
        self.id = id
        self.name = name

    @staticmethod
    def from_db_row(row):
        return Author(int(row[0]),
                      row[1])


def get_author_by_name(conn: sqlalchemy.engine.Connection,
                       name: str) -> typing.Optional[Author]:
    result = conn.execute(text('select * from authors where author_name = :name'),
                          name=name)\
                 .fetchone()
    return None if result is None else Author.from_db_row(result)


def list_authors(conn: sqlalchemy.engine.Connection) -> typing.List[Author]:
    rows = conn.execute('select * from authors').fetchall()
    return [Author.from_db_row(row) for row in rows]


def insert_author(conn: sqlalchemy.engine.Connection,
                  name: str):
    insertion = conn.execute(text('insert into authors values (NULL, :name)'),
                             name=name)
    author_id = insertion.lastrowid
    return Author(author_id, name)
