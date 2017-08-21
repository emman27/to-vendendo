help:
	@echo 'All commands:'
	@echo ''
	@echo 'coverage ................................ Measure tests coverage'
	@echo 'clean ................................ Clean unused files'
	@echo 'create-db ................................ Create database'
	@echo 'drop-db ................................ Drop database'
	@echo 'init-db .............................. Initialize the database'
	@echo 'install .............................. Install all dependencies'
	@echo 'lint ................................. Run code linter'
	@echo 'migrate ................................. Generate the migrations and upgrade the database'
	@echo 'run .................................. Run the application'
	@echo 'test ................................. Run all tests'
	@echo 'upgrade ................................. Upgrade the database'
	@echo ''

coverage:
	@@pytest --cov=tovendendo tests/ --cov-branch

clean:
	@find . -name *.pyc -delete
	@find . -name __pycache__ -delete

create-db:
	@psql -c "CREATE DATABASE tovendendo_dev;"
	@psql -c "CREATE DATABASE tovendendo_test;"

drop-db:
	@psql -c "DROP DATABASE tovendendo_dev;"
	@psql -c "DROP DATABASE tovendendo_test;"

init-db:
	@python manage.py db init

install:
	@pip install -r requirements.txt

lint:
		@flake8 .

migrate:
	@python manage.py db migrate
	@$(MAKE) upgrade

run:
	@python run.py

supermigrate:
	@$(MAKE) drop-db
	@$(MAKE) create-db
	@$(MAKE) upgrade
	@$(MAKE) migrate

test:
	@pytest tests/

upgrade:
	@python manage.py db upgrade
