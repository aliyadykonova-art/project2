import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize(
    "card_number, expected",
    [
        ("9923923271549754", "9923 92** **** 9754"),
        ("1234567812345678", "1234 56** **** 5678"),
    ],
)
def test_get_mask_card_number(card_number: str, expected: str) -> None:
    result = get_mask_card_number(card_number)

    assert result == expected


@pytest.mark.parametrize(
    "account_number, expected",
    [
        ("73654108430135874305", "**4305"),
        ("98765432109876543210", "**3210"),
    ],
)
def test_get_mask_account(account_number: str, expected: str) -> None:
    result = get_mask_account(account_number)

    assert result == expected
