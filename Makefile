help:
	python -m bloknot.runner --help

install:
	python -m pip install --upgrade pip
	python -m pip install --upgrade poetry
	poetry install

lock:
	poetry lock --no-update

update:
	poetry update

format:
	poetry run ruff format bloknot
	poetry run ruff check  bloknot --fix

lint:
	poetry run ruff format bloknot --check
	poetry run ruff check bloknot
	poetry run mypy bloknot

amend:
	git commit --amend --no-edit -a

run:
	python -m bloknot.runner --host localhost --port 8000

up:
	poetry export --without-hashes --format=requirements.txt > requirements.txt
	docker compose up --build --detach
	rm requirements.txt

down:
	docker compose down

build:
	poetry export --without-hashes --format=requirements.txt > requirements.txt
	docker build -t bloknot:latest .
	rm requirements.txt

