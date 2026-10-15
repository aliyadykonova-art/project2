import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize(
    "card_data_arg, expected",
    [
        ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
        ("Maestro 1596234125697412", "Maestro 1596 23** **** 7412"),
        ("Счет 73654108430135874305", "Счет **4305"),
    ],
)
def test_mask_account_card(card_data_arg: str, expected: str) -> None:
    result = mask_account_card(card_data_arg)

    assert result == expected


@pytest.mark.parametrize(
    "date_arg, expected",
    [
        ("2024-03-11T02:26:18.671407", "11.03.2024"),
        ("2019-07-03T18:35:29.512364", "03.07.2019"),
    ],
)
def test_get_date(date_arg: str, expected: str) -> None:
    result = get_date(date_arg)

    assert result == expected
