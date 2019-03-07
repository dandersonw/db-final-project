import sqlalchemy
from sqlalchemy.sql import text

import typing

from . import author, book


class Readinglist():
    def __init__(self, id, readinglist_name):
        self.id = id
        self.readinglist_name = readinglist_name

    @staticmethod
    def from_db_row(row):
        return Readinglist(int(row[0]),
                           row[1])


def get_readinglist_by_name(conn: sqlalchemy.engine.Connection,
                            name: str) -> typing.Optional[Readinglist]:
    result = conn.execute(text('select * from readinglists where readinglist_name = :name'),
                          name=name)\
                 .fetchone()
    return None if result is None else Readinglist.from_db_row(result)


def list_readinglists(conn: sqlalchemy.engine.Connection) -> typing.List[Readinglist]:
    rows = conn.execute('select * from readinglists').fetchall()
    return [Readinglist.from_db_row(row) for row in rows]


def insert_readinglist(conn: sqlalchemy.engine.Connection,
                       readinglist_name: str):
    insertion = conn.execute(text('insert into readinglists values (NULL, :readinglist_name)'),
                             readinglist_name=readinglist_name)
    readinglist_id = insertion.lastrowid
    return Readinglist(readinglist_id, readinglist_name)
