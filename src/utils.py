import json
import logging

from pathlib import Path

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

file_handler = logging.FileHandler("logs/utils.log", mode="w", encoding="utf-8")
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


def read_json_file(file_path: str) -> list[dict]:
    """Читает JSON-файл и возвращает список транзакций."""
    try:
        with Path(file_path).open(encoding="utf-8") as file:
            data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        logger.error("Не удалось прочитать файл: %s", file_path)
        return []

    if not isinstance(data, list):
        logger.error("Файл не содержит список данных: %s", file_path)
        return []

    logger.info("Файл успешно прочитан: %s", file_path)
    return data
