# Getting Started

You need Python and MySQL development headers on your system
in order to install the mysqlclient DB connector used by this project.
For more details on the headers,
see the [connector's README](https://github.com/PyMySQL/mysqlclient-python).

It is advisable to create a new Python environment for this application.
My tool of choice for managing such environments is
[Anaconda](https://www.anaconda.com/distribution/).
With a Python 3.7 environment,
pip install the packages in `requirements.txt`
with `pip install -r requirements.txt`.

To generate a DB config file, you can either run `make make_config`
or create a file named `db_config` of the format:

``` text
[DEFAULT]
hostname=HOSTNAME
port=PORT
username=DB_USER_NAME
pass=PASSWORD
```

You must set an environment variable `RDLIST_CONFIG_PATH`
which points to the directory containing the `db_config` file.
The credentials `db_config` provides should be to
a user with the ability to create databases.

The first step to working on the package is to run `pip install -e .`
from the root of the project directory.

To create the database run `make create_db`.
To insert some seed data run `make insert_seed_data`.
To run the tests run `make test`.
To run the GUI run `make run_ui`.

