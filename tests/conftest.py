import pytest




@pytest.fixture
def sample_transactions() -> list[dict]:
    """
    Базовый набор транзакций с разными статусами и датами.
    Используется в тестах filter_by_state и sort_by_date.
    """
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


@pytest.fixture
def transactions_same_date() -> list[dict]:
    """
    Транзакции с одинаковыми датами.
    Нужны для проверки стабильности сортировки (stable sort)
    порядок элементов с одинаковой датой не должен меняться.
    """
    return [
        {"id": 1, "state": "EXECUTED", "date": "2020-01-01T00:00:00.000000"},
        {"id": 2, "state": "CANCELED", "date": "2020-01-01T00:00:00.000000"},
        {"id": 3, "state": "EXECUTED", "date": "2020-01-01T00:00:00.000000"},
    ]


@pytest.fixture
def empty_transactions() -> list[dict]:
    """Пустой список транзакций — граничный случай."""
    return []


@pytest.fixture
def no_matching_state() -> list[dict]:
    """
    Список транзакций, среди которых нет ни одной
    с ожидаемым статусом (например, EXECUTED).
    """
    return [
        {"id": 1, "state": "PENDING", "date": "2020-01-01T00:00:00.000000"},
        {"id": 2, "state": "FAILED", "date": "2021-01-01T00:00:00.000000"},
    ]




@pytest.fixture
def valid_card_number() -> str:
    """Корректный 16-значный номер карты."""
    return "7000792289606361"


@pytest.fixture
def valid_account_number() -> str:
    """Корректный 20-значный номер счёта."""
    return "73654108430135874305"


@pytest.fixture
def valid_card_string() -> str:
    """Строка с типом карты и её номером."""
    return "Visa Platinum 7000792289606361"


@pytest.fixture
def valid_account_string() -> str:
    """Строка с типом счёта и его номером."""
    return "Счет 73654108430135874305"


@pytest.fixture
def valid_iso_date() -> str:
    """Корректная дата в формате ISO-8601."""
    return "2019-07-03T18:35:29.512364"



@pytest.fixture(params=["EXECUTED", "CANCELED", "PENDING", "FAILED"])
def any_state(request) -> str:
    """
    Перебирает различные возможные значения статуса.

    Использование в тесте:
        def test_something(any_state):
            ...
    """
    return request.param


@pytest.fixture(params=[
    "7000792289606361",
    "1234567890123456",
    "0000000000000000",
    "1111222233334444",
])
def any_valid_card(request) -> str:
    """Перебирает несколько корректных 16-значных номеров карт."""
    return request.param


@pytest.fixture(params=[
    "73654108430135874305",
    "12345678901234567890",
    "00000000000000000001",
    "11112222333344445555",
])
def any_valid_account(request) -> str:
    """Перебирает несколько корректных 20-значных номеров счетов."""
    return request.param