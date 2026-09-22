import pytest
from src.masks import get_mask_account, get_mask_card_number


class TestGetMaskCardNumber:
    @pytest.mark.parametrize(
        "card_number, expected",
        [
            ("7000792289606361", "7000 79** **** 6361"),
            ("1234567890123456", "1234 56** **** 3456"),
            ("0000000000000000", "0000 00** **** 0000"),
            ("1111222233334444", "1111 22** **** 4444"),
        ],
    )
    def test_valid_card_numbers(self, card_number, expected):
        assert get_mask_card_number(card_number) == expected

    @pytest.mark.parametrize(
        "invalid_input",
        [
            "",                       # пустая строка
            "1234",                   # слишком короткий
            "123456789012345",        # 15 цифр
            "12345678901234567",      # 17 цифр
            "abcd efgh ijkl mnop",    # не цифры
            "7000 7922 8960 6361",    # с пробелами (если не поддерживаем)
        ],
    )
    def test_invalid_card_numbers(self, invalid_input):
        with pytest.raises(ValueError):
            get_mask_card_number(invalid_input)

    @pytest.mark.parametrize("bad_type", [None, 1234567890123456, []])
    def test_non_string_input(self, bad_type):
        with pytest.raises(TypeError):
            get_mask_card_number(bad_type)


class TestGetMaskAccount:
    @pytest.mark.parametrize(
        "account_number, expected",
        [
            ("73654108430135874305", "**4305"),
            ("12345678901234567890", "**7890"),
            ("00000000000000000001", "**0001"),
            ("11112222333344445555", "**5555"),
        ],
    )
    def test_valid_account_numbers(self, account_number, expected):
        assert get_mask_account(account_number) == expected

    @pytest.mark.parametrize(
        "invalid_input",
        [
            "",                # пустая строка
            "123",             # короче 4
            "abcd",            # не цифры
            "1234abcd5678",    # смешанное
        ],
    )
    def test_invalid_account_numbers(self, invalid_input):
        with pytest.raises(ValueError):
            get_mask_account(invalid_input)

    @pytest.mark.parametrize("bad_type", [None, 12345678901234567890, []])
    def test_non_string_input(self, bad_type):
        with pytest.raises(TypeError):
            get_mask_account(bad_type)