.PHONY: run migrate test

run:
    flask run

migrate:
    flask db upgrade

test:
    pytest
