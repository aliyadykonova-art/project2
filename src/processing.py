import re

from collections import Counter
from typing import Any

def filter_by_state(
    operations: list[dict[str, Any]], state: str = "EXECUTED"
) -> list[dict[str, Any]]:
    """Возвращает операции с указанным статусом без учёта регистра."""
    expected_state = state.upper()
    return [
        operation
        for operation in operations
        if str(operation.get("state", "")).upper() == expected_state
    ]


def get_date(operation: dict[str, Any]) -> str:
    """Возвращает дату операции."""
    return str(operation.get("date", operation.get("Дата", "")))


def sort_by_date(
    operations: list[dict[str, Any]], reverse: bool = True
) -> list[dict[str, Any]]:
    """Сортирует операции по дате, не изменяя исходный список."""
    return sorted(operations, key=get_date, reverse=reverse)


def process_bank_search(
    operations: list[dict[str, Any]], search: str
) -> list[dict[str, Any]]:
    """Находит операции, описание которых соответствует регулярному выражению."""
    try:
        pattern = re.compile(search, re.IGNORECASE)
    except re.error:
        return []

    return [
        operation
        for operation in operations
        if pattern.search(
            str(operation.get("description", operation.get("Описание", "")))
        )
    ]


def process_bank_operations(
    operations: list[dict[str, Any]], categories: list[str]
) -> dict[str, int]:
    """Подсчитывает операции, в описании которых встречается каждая категория."""
    descriptions = [
        str(operation.get("description", operation.get("Описание", ""))).lower()
        for operation in operations
    ]

    return {
        category: sum(
            1 for description in descriptions
            if category.lower() in description
        )
        for category in categories
    }
