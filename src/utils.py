import json
import logging
from pathlib import Path

import pandas as pd

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


def read_transactions_from_csv(file_path: str) -> list[dict]:
    """Читает CSV-файл и возвращает список транзакций."""
    try:
        df = pd.read_csv(file_path)
        transactions = df.to_dict(orient="records")
    except (FileNotFoundError, pd.errors.ParserError, UnicodeDecodeError) as error:
        logger.error("Не удалось прочитать CSV-файл %s: %s", file_path, error)
        return []

    logger.info("CSV-файл успешно прочитан: %s", file_path)
    return transactions


def read_transactions_from_excel(file_path: str) -> list[dict]:
    """Читает Excel-файл и возвращает список транзакций."""
    try:
        df = pd.read_excel(file_path)
        transactions = df.to_dict(orient="records")
    except (FileNotFoundError, ValueError, OSError) as error:
        logger.error("Не удалось прочитать Excel-файл %s: %s", file_path, error)
        return []

    logger.info("Excel-файл успешно прочитан: %s", file_path)
    return transactions
