# mkdir src
# mkdir tests

# init project
poetry init

# add dependencies
poetry add --group lint flake8
poetry add --group lint black
poetry add --group lint isort
poetry add --group lint mypy

# add local dependencies
poetry add pytest --group dev
poetry add pytest-cov --group dev

poetry add requests
poetry add python-dotenv

# add emoty __init__.py files for folders recognition
touch src/__init__.py
touch tests/__init__.py
