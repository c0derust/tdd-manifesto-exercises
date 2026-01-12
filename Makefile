PHONY: linter test

linter:
	uvx ruff format
	uvx ruff check

test:
	uv run pytest
