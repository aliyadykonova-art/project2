import json
from pathlib import Path


def read_json_file(file_path: str) -> list[dict]:
    """Читает JSON-файл и возвращает список транзакций."""
    try:
        with Path(file_path).open(encoding="utf-8") as file:
            data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

    if not isinstance(data, list):
        return []

    return data
