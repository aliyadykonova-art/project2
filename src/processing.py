import re
from typing import Any


def filter_by_state(data_list: list[dict], state: str = "EXECUTED") -> list[dict]:
    """Фильтрует список словарей по значению ключа 'state'."""
    filtered_data = []

    for item in data_list:
        if item.get("state") == state:
            filtered_data.append(item)

    return filtered_data


def sort_by_date(data_list: list[dict], descending: bool = True) -> list[dict]:
    """Сортирует список словарей по дате."""
    return sorted(data_list, key=lambda x: x["date"], reverse=descending)

def process_bank_search(data: list[dict[str, Any]], search_string: str) -> list[dict[str, Any]]:
    """Принимает список словарей с транзакциями и строку поиска,

    возвращает список словарей, у которых в описании есть данная строка (через regex).
    """
    matched_transactions = []
    pattern = re.compile(re.escape(search_string), re.IGNORECASE)

    for transaction in data:
        description = transaction.get("description", "")
        if description and pattern.search(str(description)):
            matched_transactions.append(transaction)

    return matched_transactions


def process_bank_operations(data: list[dict[str, Any]], categories: list[str]) -> dict[str, int]:
    """Принимает список словарей и список категорий,

    возвращает словарь с количеством операций для каждой категории.
    """
    category_counts = {category: 0 for category in categories}

    for transaction in data:
        description = transaction.get("description", "")
        for category in categories:
            if description and category.lower() in str(description).lower():
                category_counts[category] += 1

    return category_counts
