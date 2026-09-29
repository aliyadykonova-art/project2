from typing import Any


def filter_by_state(operations: list[dict[str, Any]], state: str = "EXECUTED") -> list[dict[str, Any]]:
    """
    Фильтрует операции по статусу, создавая новый список вручную.
    Параметр operations представляет собой список банковских операций.
    """
    filtered_list = []

    for op in operations:
        if op.get("state") == state:
            filtered_list.append(op)

    return filtered_list

def get_date(op: dict[str, Any]) -> str:
    """Функция-помощник, которая получает дату операции из входного списка."""
    return op.get("date", "")

def sort_by_date(operations: list[dict[str, Any]], reverse: bool = True) -> list[dict[str, Any]]:
    """
    Сортирует операции по дате и возвращает новый список.
    Параметр operations представляет собой список банковских операций.
    """
    # Создаем новый отсортированный список, не изменяя оригинал
    sorted_list = sorted(operations, key=get_date, reverse=reverse)

    return sorted_list
