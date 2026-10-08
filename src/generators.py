from collections.abc import Generator, Iterator
from typing import Any


def filter_by_currency(transactions: list[dict[str, Any]], currency: str) -> Iterator[dict[str, Any]]:
    """
    Функция принимает на вход список словарей (транзакции), и валюту по которой надо отфильтровать
    все транзакции клиента, вовзвращая в ответ итератор list[dict[str, Any].
    """
    # tx.get("значение", значение если элемента нет)
    return (transaction
            for transaction in transactions
            if transaction.get("operation", {}).get("currency", {}).get("code") == currency
            )

def transaction_descriptions(transactions: list[dict[str, Any]]) -> Generator[str, None, None]:
    """
    Generator[yieldReturnType, SendDataType, ReturnDataType]

    Функция принимает на вход список словарей (транзакции), и возвращает
    генератор, ибо эта функция является генератором
    """

    for transaction in transactions:
        # при каждой новой итерации возвращает следующее значение из списка.
        yield transaction.get("description", "Описание отсутствует")

def card_number_generator(start: int, stop: int) -> Iterator[str]:
    """
    Функция принимает на вход начало и конец номера карты, которая нужна для генерации,
    возвращает итератор, который содержит в себе номер карты как строку.
    """

    # цикл по всему диапазону номеров (включая stop)
    for card_number in range(start, stop + 1):
        card_str = f"{card_number:016d}"

        # перебираем строку с шагом 4 и склеиваем куски через пробел
        yield " ".join(card_str[i: i + 4] for i in range(0, 16, 4))
