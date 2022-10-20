# Makefile

SHELL := /bin/bash

init:
	python3 -m venv venv; \
	source ./venv/bin/activate; \
	pip install -r requirements.txt; \

run:
	source ./venv/bin/activate; \
	python manage.py run --dev

update:
	( \
       source ./venv/bin/activate; \
       pip install -r requirements.txt; \
    )
