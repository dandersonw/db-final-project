import os
import pytest
import sqlite3


@pytest.fixture(scope="class")
def db_class(request):
    db_path = os.path.join(os.environ['RDLIST_DB_PATH'],
                           'test.db')
    request.cls.db = sqlite3.connect(db_path)
