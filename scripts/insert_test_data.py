from readinglist import db

script = ''.join(list(open('./scripts/insert_test_data.sql')))
db.engine.execute(script)
