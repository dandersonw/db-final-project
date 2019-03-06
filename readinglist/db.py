import configparser
import os
import sqlalchemy


config_path = os.environ.get('RDLIST_CONFIG_PATH')
env = os.environ.get('RDLIST_ENV')

if config_path is None or not os.path.exists(config_path):
    raise Exception('RDLIST_CONFIG_PATH not set!')
if env is None:
    raise Exception('RDLIST_ENV not set!')

db_config_path = os.path.join(config_path, 'db_config')
db_config = configparser.ConfigParser()
db_config.read(db_config_path)
db_config = db_config['DEFAULT']

engine = sqlalchemy.create_engine('{dialect}://{username}:{password}@{host}:{port}/{database}'
                                  .format(dialect='mysql+mysqldb',
                                          username=db_config['username'],
                                          password=db_config['pass'],
                                          host=db_config['hostname'],
                                          port=db_config['port'],
                                          database='readinglist_{}'.format(env)))
