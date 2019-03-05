ifndef RDLIST_ENV
override RDLIST_ENV = dev
endif

ifndef RDLIST_DB_PATH
override RDLIST_DB_PATH = dbs
endif

clean_db:
	rm -f $(RDLIST_DB_PATH)/$(RDLIST_ENV).db

generate_db:
	mkdir -p $(RDLIST_DB_PATH)
	sqlite3 $(RDLIST_DB_PATH)/$(RDLIST_ENV).db < scripts/create_db.sql

regenerate_db:
	make clean_db
	make generate_db

