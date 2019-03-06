import sqlalchemy
import pytest

from readinglist import db


@pytest.fixture(scope="session")
def db_connection(request):
    conn: sqlalchemy.engine.Connection = db.engine.connect()
    yield conn
    conn.close()


@pytest.fixture(scope="function")
def db_transaction(db_connection):
    trans: sqlalchemy.engine.Transaction = db_connection.begin()
    yield trans
    trans.rollback()
