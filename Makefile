SRC_DIR = pilgram2

all: test clean build;

lint:
	poetry run ruff check ${SRC_DIR}

format:
	poetry run ruff --fix ${SRC_DIR}

test: lint
	poetry run pytest --cov-report=term --cov-report=xml:coverage.xml

test-benchmark:
	poetry run pytest --benchmark-only --benchmark-max-time=5 --benchmark-columns="mean,stddev,min,max"

clean:
	find . -type f -name "*.pyc" -delete
	rm -rf dist

build:
	poetry build

test-upload: clean build
	poetry publish -r testpypi

upload: clean build
	poetry publish -r pypi

.PHONY: all lint format test test-benchmark benchmark clean build test-upload upload
