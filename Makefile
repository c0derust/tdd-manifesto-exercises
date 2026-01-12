PHONY: linter test

lint:
	uvx ruff format
	uvx ruff check

test:
	uv run pytest
