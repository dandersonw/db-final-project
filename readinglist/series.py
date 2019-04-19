import sqlalchemy
from sqlalchemy.sql import text

import typing


class Series():
    def __init__(self, id, series_name):
        self.id = id
        self.series_name = series_name

    @staticmethod
    def from_db_row(row):
        return Series(int(row[0]),
                      row[1])


def get_series_by_name(conn: sqlalchemy.engine.Connection,
                       name: str) -> typing.Optional[Series]:
    result = conn.execute(text('select * from series where series_name = :name'),
                          name=name)\
                 .fetchone()
    return None if result is None else Series.from_db_row(result)


def list_series(conn: sqlalchemy.engine.Connection) -> typing.List[Series]:
    rows = conn.execute('select * from series').fetchall()
    return [Series.from_db_row(row) for row in rows]


def insert_series(conn: sqlalchemy.engine.Connection,
                  series_name: str,
                  authors,
                  books):
    insertion = conn.execute(text('insert into series values (NULL, :series_name)'),
                             series_name=series_name)
    series_id = insertion.lastrowid
    for authorr in authors:
        conn.execute(text('insert into series_author values (:series_id, :author_id)'),
                     series_id=series_id,
                     author_id=authorr.id)
    for i, bookk in enumerate(books):
        conn.execute(text('insert into book_series values (:book_id, :series_id, :position)'),
                     book_id=bookk.id,
                     series_id=series_id,
                     position=i)
    return Series(series_id, series_name)


def series_len(conn,
               series: Series):
    result = conn.execute(text('select series_len(:series_id)'),
                          series_id=series.id)
    return result.fetchone()[0]
