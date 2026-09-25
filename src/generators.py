from collections.abc import Generator, Iterator
from typing import Any


def filter_by_currency(
    transactions: list[dict[str, Any]],
    currency: str,
) -> Iterator[dict[str, Any]]:
    """
    Фильтрует транзакции по коду валюты.

    Принимает список словарей (транзакции) и код валюты.
    Возвращает итератор с транзакциями, у которых код валюты
    совпадает с переданным.
    """
    return (
        transaction
        for transaction in transactions
        if transaction.get("operation", {})
        .get("currency", {})
        .get("code") == currency
    )


def transaction_descriptions(
    transactions: list[dict[str, Any]],
) -> Generator[str, None, None]:
    """
    Генератор описаний транзакций.

    Generator[yieldReturnType, SendDataType, ReturnDataType].

    Принимает список словарей (транзакции) и поочерёдно возвращает
    описание каждой транзакции. Если описание отсутствует,
    возвращается строка "Описание отсутствует".
    """
    for transaction in transactions:
        yield transaction.get("description", "Описание отсутствует")


def card_number_generator(start: int, stop: int) -> Iterator[str]:
    """
    Генератор номеров карт в формате 'XXXX XXXX XXXX XXXX'.

    Принимает начало и конец диапазона номеров карт (включительно)
    и возвращает итератор со строками — номерами карт.
    """
    for card_number in range(start, stop + 1):
        card_str = f"{card_number:016d}"
        yield " ".join(
            card_str[i:i + 4] for i in range(0, 16, 4)
        )
