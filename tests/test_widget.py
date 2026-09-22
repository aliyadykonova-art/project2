import pytest

from src.widget import (
    get_date,
    mask_account_card,
    mask_account_number,
    mask_card_number,
)


class TestMaskCardNumber:
    @pytest.mark.parametrize(
        "number, expected",
        [
            ("7000792289606361", "7000 79** **** 6361"),
            ("1234567890123456", "1234 56** **** 3456"),
            ("0000000000000000", "0000 00** **** 0000"),
            ("1111222233334444", "1111 22** **** 4444"),
        ],
    )
    def test_valid(self, number, expected):
        assert mask_card_number(number) == expected

    @pytest.mark.parametrize("short", ["", "1234", "123456789012345"])
    def test_short_returns_as_is(self, short):
        assert mask_card_number(short) == short

    def test_too_long_returns_as_is(self):
        assert mask_card_number("1" * 17) == "1" * 17

    def test_none_raises(self):
        with pytest.raises(TypeError):
            mask_card_number(None)

    def test_non_digits_16_chars(self):

        assert mask_card_number("abcdefghijklmnop") == "abcd ef** **** mnop"


class TestMaskAccountNumber:
    @pytest.mark.parametrize(
        "number, expected",
        [
            ("73654108430135874305", "**4305"),
            ("12345678901234567890", "**7890"),
            ("1234", "**1234"),
        ],
    )
    def test_valid_or_boundary(self, number, expected):
        assert mask_account_number(number) == expected

    @pytest.mark.parametrize("short", ["", "1", "123"])
    def test_short_returns_as_is(self, short):
        assert mask_account_number(short) == short

    def test_none_raises(self):
        with pytest.raises(TypeError):
            mask_account_number(None)


class TestMaskAccountCard:
    @pytest.mark.parametrize(
        "raw, expected",
        [
            ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
            ("Maestro 7000792289606361", "Maestro 7000 79** **** 6361"),
            ("MasterCard 1234567890123456", "MasterCard 1234 56** **** 3456"),
            ("Счет 73654108430135874305", "Счет **4305"),
            ("СЧЕТ 73654108430135874305", "СЧЕТ **4305"),
        ],
    )
    def test_cards_and_accounts(self, raw, expected):
        assert mask_account_card(raw) == expected

    def test_empty_string_raises(self):
        with pytest.raises(IndexError):
            mask_account_card("")

    def test_none_raises(self):
        with pytest.raises(AttributeError):
            mask_account_card(None)

    def test_only_name_returns_garbage(self):

        assert mask_account_card("Visa") == " Visa"

    def test_number_without_name(self):
        # ведущий пробел — тоже баг
        assert mask_account_card("7000792289606361") == " 7000 79** **** 6361"

    def test_multiword_account_name_goes_to_card_branch(self):

        result = mask_account_card("Расчетный счет 12345678901234567890")
        assert result == "Расчетный счет 12345678901234567890"


class TestGetDate:
    @pytest.mark.parametrize(
        "raw, expected",
        [
            ("2019-07-03T18:35:29.512364", "03.07.2019"),
            ("2018-06-30T02:08:58.425572", "30.06.2018"),
            ("2020-01-01T00:00:00.000000", "01.01.2020"),
            ("2023-12-31T23:59:59.999999", "31.12.2023"),
            ("2019-07-03", "03.07.2019"),
            ("2019-07-03T18:35", "03.07.2019"),
        ],
    )
    def test_valid(self, raw, expected):
        assert get_date(raw) == expected

    def test_empty_string_raises(self):
        with pytest.raises(ValueError):
            get_date("")

    def test_none_raises(self):
        with pytest.raises(AttributeError):
            get_date(None)

    def test_garbage_with_three_parts_returns_garbage(self):

        assert get_date("not-a-date") == "date.a.not"

    def test_too_many_parts_raises(self):
        with pytest.raises(ValueError):
            get_date("2019-07-03-extra")

    def test_too_few_parts_raises(self):
        with pytest.raises(ValueError):
            get_date("2019-07")