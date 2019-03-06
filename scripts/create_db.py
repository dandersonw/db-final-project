import argparse
import sqlalchemy_utils

from readinglist import db


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--overwrite',
                        action='store_true')
    args = parser.parse_args()

    create_db(overwrite=args.overwrite)


def create_db(overwrite=False):
    if sqlalchemy_utils.database_exists(db.engine.url):
        if overwrite:
            sqlalchemy_utils.drop_database(db.engine.url)
        else:
            raise Exception('Database already exists!')
    sqlalchemy_utils.create_database(db.engine.url)    
    script = ''.join(list(open('./scripts/create_db.sql')))
    db.engine.execute(script)


if __name__ == '__main__':
    main()
