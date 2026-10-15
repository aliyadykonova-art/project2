import pytest

from src.processing import filter_by_state, sort_by_date


@pytest.fixture
def sample_operations() -> list[dict]:
    """Простые тестовые данные с понятными ID и датами"""
    return [
        {"id": 1, "state": "EXECUTED", "date": "2019-07-03"},
        {"id": 2, "state": "CANCELED", "date": "2018-09-12"},
        {"id": 3, "state": "EXECUTED", "date": "2018-06-30"},
    ]


# Тестируем фильтрацию по статусу
@pytest.mark.parametrize(
    "state_arg, expected_ids",
    [
        ("EXECUTED", [1, 3]),  # ожидаемые id для "EXECUTED"
        ("CANCELED", [2]),     # ожидаемые id для "CANCELED"
    ],
)
def test_filter_by_state(sample_operations: list[dict], state_arg: str, expected_ids: list[int]) -> None:
    result = filter_by_state(sample_operations, state_arg)

    result_ids = []
    for op in result:
        result_ids.append(op["id"])

    assert result_ids == expected_ids


@pytest.mark.parametrize(
    "reverse_arg, expected_ids",
    [
        (True, [1, 2, 3]),   # от новых к старым id
        (False, [3, 2, 1]),  # от старых к новым id
    ],
)
def test_sort_by_date(sample_operations: list[dict], reverse_arg: bool, expected_ids: list[int]) -> None:
    result = sort_by_date(sample_operations, reverse_arg)

    result_ids = []
    for op in result:
        result_ids.append(op["id"])

    assert result_ids == expected_ids
