import pytest

from src.generators import (card_number_generator, filter_by_currency,
                            transaction_descriptions)

STATIC_TRANSACTIONS = [
    {
        "id": 1,
        "description": "Перевод организации",
        "operation": {"currency": {"name": "Рубль", "code": "RUB"}}
    },
    {
        "id": 2,
        "description": "Покупка в магазине",
        "operation": {"currency": {"name": "Доллар", "code": "USD"}}
    },
    {
        "id": 3,
        "operation": {"currency": {"name": "Рубль", "code": "RUB"}}
    }
]

@pytest.mark.parametrize(
    "transactions, currency_code, expected_ids",
    [
        (STATIC_TRANSACTIONS, "RUB", [1, 3]),
        (STATIC_TRANSACTIONS, "USD", [2]),
        (STATIC_TRANSACTIONS, "EUR", []),
        ([], "USD", []),
        ([{"id": 4}], "RUB", [])
    ],
    ids=["find_rub", "find_usd", "no_match_eur", "empty_list", "missing_operation"]
)
def test_filter_by_currency(transactions, currency_code, expected_ids):
    """Проверяем фильтрацию по валютам для различных кейсов."""

    result_list = list(filter_by_currency(transactions, currency_code))
    actual_ids = [tx["id"] for tx in result_list]

    assert actual_ids == expected_ids


@pytest.mark.parametrize(
    "transactions, expected_descriptions",
    [
        (STATIC_TRANSACTIONS, ["Перевод организации", "Покупка в магазине", "Описание отсутствует"]),
        ([], []),
        ([{"description": None}], [None]),
        ([{"description": ""}], [""])
    ],
    ids=["normal_and_missing", "empty_input", "none_value", "empty_string"]
)
def test_transaction_descriptions(transactions, expected_descriptions):
    """Проверяем генератор описаний, включая пустые строки и отсутствующие поля."""
    assert list(transaction_descriptions(transactions)) == expected_descriptions

@pytest.mark.parametrize(
    "start, stop, expected_cards",
    [
        (1, 3, ["0000 0000 0000 0001", "0000 0000 0000 0002", "0000 0000 0000 0003"]),
        (99999, 99999, ["0000 0000 0009 9999"]),
        (9999999999999999, 9999999999999999, ["9999 9999 9999 9999"]),
        (5, 3, []),
        (-1, -1, ["-000 0000 0000 0001"])
    ],
    ids=["range_1_3", "single_value", "max_digits", "invalid_range", "negative_number"]
)
def test_card_number_generator(start, stop, expected_cards):
    """Проверяем генерацию номеров карт для всех возможных диапазонов."""
    assert list(card_number_generator(start, stop)) == expected_cards
