ifndef RDLIST_ENV
	override RDLIST_ENV = dev
endif

ifndef RDLIST_CONFIG_PATH
	override RDLIST_CONFIG_PATH = ./.config
endif

.EXPORT_ALL_VARIABLES:

run_ui:
	python ReadingUI.py

make_config:
	bash ./scripts/make_db_config.sh

drop_db:
	python scripts/drop_db.py

create_db:
	python scripts/create_db.py

insert_seed_data:
	python scripts/insert_test_data.py

regenerate_db:
	python scripts/create_db.py --overwrite

generate_test_db:
	RDLIST_ENV=test make regenerate_db
	RDLIST_ENV=test python scripts/insert_test_data.py

test: generate_test_db
	RDLIST_ENV=test	python -m pytest
