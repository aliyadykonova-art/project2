import pytest

from src.generators import (card_number_generator, filter_by_currency,
                            transaction_descriptions)


@pytest.fixture
def sample_transactions():
    return [
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
            # Здесь специально нет описания для проверки значения по умолчанию
            "operation": {"currency": {"name": "Рубль", "code": "RUB"}}
        }
    ]


def test_filter_by_currency_rub(sample_transactions):
    """Проверяем фильтрацию по RUB (должно быть 2 транзакции)."""

    result_iterator = filter_by_currency(sample_transactions, "RUB")
    result_list = list(result_iterator)

    assert len(result_list) == 2
    assert result_list[0]["id"] == 1
    assert result_list[1]["id"] == 3


def test_filter_by_currency_empty():
    """Проверяем работу с пустым списком."""

    result = list(filter_by_currency([], "USD"))
    assert result == []


def test_filter_by_currency_no_match(sample_transactions):
    """Проверяем, если искомой валюты нет в списке."""

    result = list(filter_by_currency(sample_transactions, "EUR"))
    assert result == []


def test_transaction_descriptions(sample_transactions):
    """Проверяем корректное извлечение описаний и обработку дефолтного значения."""

    descriptions_gen = transaction_descriptions(sample_transactions)
    result_list = list(descriptions_gen)

    assert result_list == ["Перевод организации", "Покупка в магазине", "Описание отсутствует"]


def test_transaction_descriptions_empty():
    """Проверяем работу генератора описаний на пустом списке."""

    assert list(transaction_descriptions([])) == []


def test_card_number_generator_format():
    """Проверяем формат номеров карт и дополнение нулями."""

    card_gen = card_number_generator(1, 3)
    result_list = list(card_gen)

    assert result_list == [
        "0000 0000 0000 0001",
        "0000 0000 0000 0002",
        "0000 0000 0000 0003"
    ]


def test_card_number_generator_single_value():
    """Проверяем генератор, когда start и stop совпадают."""

    card_gen = card_number_generator(99999, 99999)
    result_list = list(card_gen)

    assert result_list == ["0000 0000 0009 9999"]
