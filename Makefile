.PHONY: test
test:
	poetry run pytest

.PHONY: lint
lint:
	black src/ tests/
	isort --profile black src/ tests/