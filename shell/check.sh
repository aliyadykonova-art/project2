#!/bin/bash
clear

echo "flake8 running..."
poetry run flake8 .

echo "isort running..."
poetry run isort .

echo "mypy running..."
poetry run mypy .