test:
	poetry run pytest . -vv -x

style:
	poetry run ruff format
	poetry run ruff check --fix --show-fixes
