# mkdir src
# mkdir tests

poetry init

poetry add --group lint flake8
poetry add --group lint black
poetry add --group lint isort
poetry add --group lint mypy

# mkdir src/masks