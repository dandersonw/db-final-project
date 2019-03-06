import os
import pytest
import sqlite3


@pytest.fixture(scope="class")
def db_class(request):
    db_path = os.path.join(os.environ['RDLIST_DB_PATH'],
                           'test.db')
    connection = sqlite3.connect(db_path)
    # this is kind of a pain, but neccessary to give us control over
    # transactions, instead of using the weird automatic transaction management
    # that the sqlite3 lib provides natively
    connection.isolation_level = None
    request.cls.db = connection
