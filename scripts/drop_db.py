import sqlalchemy_utils
from readinglist import db


sqlalchemy_utils.drop_database(db.engine.url)
