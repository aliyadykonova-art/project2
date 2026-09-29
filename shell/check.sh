#!/bin/bash
clear

echo "flake8 running..."
poetry run flake8 src tests

echo "isort running..."
poetry run isort src tests

echo "mypy running..."
poetry run mypy src tests
