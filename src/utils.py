import json
import logging
import os

import pandas as pd

# Автоматически создаем папку logs, если ее еще нет
os.makedirs("logs", exist_ok=True)

logger = logging.getLogger("utils")
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler("logs/utils.log", mode="w", encoding="utf-8")
file_handler.setLevel(logging.DEBUG)

formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)

if not logger.handlers:
    logger.addHandler(file_handler)


def get_financial_data(path: str) -> list[dict]:
    """Читает финансовые данные из JSON файла."""
    logger.info(f"Попытка чтения данных из файла: {path}")

    if not os.path.exists(path):
        logger.error(f"Файл не найден по пути: {path}")
        return []

    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
            if isinstance(data, list):
                logger.info(f"Данные успешно загружены из файла {path}. Найдено записей: {len(data)}")
                return data
            else:
                logger.warning(f"Файл {path} содержит не список, а {type(data).__name__}")
                return []
    except json.JSONDecodeError as e:
        logger.error(f"Ошибка декодирования JSON в файле {path}: {e}")
        return []
    except Exception as e:
        logger.error(f"Непредвиденная ошибка при чтении файла {path}: {e}")
        return []


def read_transactions_from_csv(file_path: str) -> list[dict]:
    """Считывает финансовые транзакции из CSV-файла с помощью pandas."""
    logger.info(f"Попытка чтения CSV-файла: {file_path}")
    if not os.path.exists(file_path):
        logger.error(f"CSV-файл не найден по пути: {file_path}")
        return []
    try:
        df = pd.read_csv(file_path)
        transactions = df.to_dict(orient="records")
        logger.info(f"CSV-файл успешно прочитан. Найдено записей: {len(transactions)}")
        return transactions
    except Exception as e:
        logger.error(f"Ошибка при чтении CSV-файла {file_path}: {e}")
        return []


def read_transactions_from_excel(file_path: str) -> list[dict]:
    """Считывает финансовые транзакции из XLSX-файла с помощью pandas."""
    logger.info(f"Попытка чтения Excel-файла: {file_path}")
    if not os.path.exists(file_path):
        logger.error(f"Excel-файл не найден по пути: {file_path}")
        return []
    try:
        df = pd.read_excel(file_path)
        transactions = df.to_dict(orient="records")
        logger.info(f"Excel-файл успешно прочитан. Найдено записей: {len(transactions)}")
        return transactions
    except Exception as e:
        logger.error(f"Ошибка при чтении Excel-файла {file_path}: {e}")
        return []
