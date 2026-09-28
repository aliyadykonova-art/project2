from collections.abc import Generator
from typing import Any


def filter_by_currency(
    transactions: list[dict[str, Any]],
    currency: str,
) -> Generator[dict[str, Any], None, None]:
    """Фильтрует транзакции по коду валюты.

    Принимает список словарей (транзакции) и код валюты.
    Возвращает генератор с транзакциями, у которых код валюты
    совпадает с переданным.
    """
    for transaction in transactions:
        # Проверяем оба часто встречающихся ключа: operation и operationAmount
        op_data = transaction.get("operation") or transaction.get("operationAmount") or {}
        currency_code = op_data.get("currency", {}).get("code")
        
        if currency_code == currency:
            yield transaction


def transaction_descriptions(
    transactions: list[dict[str, Any]],
) -> Generator[str, None, None]:
    """Генератор описаний транзакций.

    Принимает список словарей (транзакции) и поочерёдно возвращает
    описание каждой транзакции. Если описание отсутствует,
    возвращается строка "Описание отсутствует".
    """
    for transaction in transactions:
        yield transaction.get("description", "Описание отсутствует")


def card_number_generator(start: int, stop: int) -> Generator[str, None, None]:
    """Генератор номеров карт в формате 'XXXX XXXX XXXX XXXX'.

    Принимает начало и конец диапазона номеров карт (включительно)
    и возвращает генератор со строками — номерами карт.
    """
    for card_number in range(start, stop + 1):
        card_str = f"{card_number:016d}"
        # Форматируем строку по 4 цифры через пробел
        yield " ".join(card_str[i:i + 4] for i in range(0, 16, 4))
