SHELL := /bin/bash
PY := python

.PHONY: help install fmt lint test train run docker-build docker-run pre-commit openapi

help:
	@echo "Targets:"
	@echo "  install       - install requirements"
	@echo "  fmt           - run formatters (black, isort)"
	@echo "  lint          - run flake8"
	@echo "  test          - run pytest"
	@echo "  train         - train baseline model"
	@echo "  run           - run API locally (uvicorn --reload)"
	@echo "  docker-build  - build Docker image"
	@echo "  docker-run    - run Docker container"
	@echo "  pre-commit    - install pre-commit hooks"
	@echo "  openapi       - export OpenAPI spec to openapi.json"

install:
	pip install -r requirements.txt

fmt:
	black . && isort .

lint:
	flake8 .

test:
	pytest -q

train:
	$(PY) model/train.py

run:
	uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload

docker-build:
	docker build -t minimal-deploy-pipeline:latest -f infra/Dockerfile .

docker-run:
	docker run --rm -p 8000:8000 \
		-e MODEL_PATH=/app/model/artifacts/model.joblib \
		-e LOG_LEVEL=INFO \
		minimal-deploy-pipeline:latest

pre-commit:
	pre-commit install

openapi:
	$(PY) scripts/gen_openapi.py
