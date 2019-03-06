import sqlite3

import typing


class Book():
    def __init__(self, id, title, status):
        self.id = id
        self.title = title
        self.status = status

    @staticmethod
    def from_db_row(row):
        return Book(int(row[0]),
                    row[1],
                    int(row[2]))


def list_books(conn: sqlite3.Connection) -> typing.List[Book]:
    rows = conn.execute('select * from books').fetchall()
    return [Book.from_db_row(row) for row in rows]


def insert_book(conn: sqlite3.Connection,
                title: str,
                status: int):  # TODO: make status an enum or something
    cursor = conn.cursor()
    cursor.execute('insert into books values (NULL, ?, ?)', (title, status))
    book_id = cursor.lastrowid
    return Book(book_id, title, status)
