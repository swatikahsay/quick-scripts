.PHONY: test lint format clean install

install:
	pip install -e .

test:
	python -m pytest tests/ -v --tb=short

lint:
	flake8 . --max-line-length=120 --exclude=venv,.git

format:
	black . --line-length=120

clean:
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
	find . -name "*.pyc" -delete 2>/dev/null || true
	rm -rf dist/ build/ *.egg-info/
