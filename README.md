# Getting Started

You need Python and MySQL development headers on your system.

With a Python 3.7 environment, pip install the packages in `requirements.txt`.

To generate a DB config file, you can either run `make make_config`
or create a file named `db_config` of the format:

``` text
[DEFAULT]
hostname=HOSTNAME
port=PORT
username=DB_USER_NAME
pass=PASSWORD
```

`db_config` needs to be located in a folder pointed to by an environment variable `RDLIST_CONFIG_PATH`.

The first step to working on the package is to run `pip install -e .` from the root of the project directory.

To create the database run `make generate_db`.

To run the tests run `make test`.

