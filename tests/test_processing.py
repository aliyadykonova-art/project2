import pytest

from src.processing import filter_by_state, get_date, sort_by_date


class TestFilterByState:
    def test_default_state_executed(self, sample_transactions):
        result = filter_by_state(sample_transactions)
        assert len(result) == 2
        assert all(op["state"] == "EXECUTED" for op in result)

    @pytest.mark.parametrize(
        "state, expected_ids",
        [
            ("EXECUTED", [41428829, 939719570]),
            ("CANCELED", [594226727, 615064591]),
            ("PENDING", []),
            ("executed", []),
        ],
    )
    def test_various_states(self, sample_transactions, state, expected_ids):
        result = filter_by_state(sample_transactions, state)
        assert [op["id"] for op in result] == expected_ids

    def test_no_matching_state(self, no_matching_state):
        assert filter_by_state(no_matching_state, "EXECUTED") == []

    def test_empty_list(self, empty_transactions):
        assert filter_by_state(empty_transactions) == []

    def test_operations_without_state_key_are_ignored(self):
        ops = [
            {"id": 1, "date": "2020-01-01T00:00:00.000000"},  # нет state
            {"id": 2, "state": "EXECUTED", "date": "2021-01-01T00:00:00.000000"},
        ]
        result = filter_by_state(ops, "EXECUTED")
        assert [op["id"] for op in result] == [2]

    def test_does_not_mutate_input(self, sample_transactions):
        original = [op.copy() for op in sample_transactions]
        filter_by_state(sample_transactions, "CANCELED")
        assert sample_transactions == original

    def test_returns_new_list(self, sample_transactions):
        result = filter_by_state(sample_transactions, "EXECUTED")
        assert result is not sample_transactions

    @pytest.mark.parametrize("bad_input", [None, "not a list", 42])
    def test_invalid_input_type(self, bad_input):
        with pytest.raises(TypeError):
            filter_by_state(bad_input)


class TestGetDate:
    def test_returns_date_when_present(self):
        op = {"id": 1, "date": "2019-07-03T18:35:29.512364"}
        assert get_date(op) == "2019-07-03T18:35:29.512364"

    def test_returns_empty_string_when_missing(self):
        op = {"id": 1, "state": "EXECUTED"}
        assert get_date(op) == ""

    @pytest.mark.parametrize("bad_input", [None, "string", 42, ["date"]])
    def test_invalid_input_type(self, bad_input):
        with pytest.raises(AttributeError):
            get_date(bad_input)



class TestSortByDate:
    def test_descending_by_default(self, sample_transactions):
        result = sort_by_date(sample_transactions)
        dates = [op["date"] for op in result]
        assert dates == sorted(dates, reverse=True)

    def test_ascending_with_reverse_false(self, sample_transactions):
        result = sort_by_date(sample_transactions, reverse=False)
        dates = [op["date"] for op in result]
        assert dates == sorted(dates)

    def test_same_dates_are_stable(self, transactions_same_date):
        result = sort_by_date(transactions_same_date)
        # при одинаковых датах порядок должен сохраниться
        assert [op["id"] for op in result] == [1, 2, 3]

    def test_empty_list(self, empty_transactions):
        assert sort_by_date(empty_transactions) == []

    def test_does_not_mutate_input(self, sample_transactions):
        original = [op.copy() for op in sample_transactions]
        sort_by_date(sample_transactions)
        assert sample_transactions == original

    def test_returns_new_list(self, sample_transactions):
        result = sort_by_date(sample_transactions)
        assert result is not sample_transactions

    def test_operations_without_date_go_first_when_desc(self):
        ops = [
            {"id": 1, "date": "2020-01-01T00:00:00.000000"},
            {"id": 2},  # нет date → ""
        ]
        result = sort_by_date(ops)

        assert [op["id"] for op in result] == [2, 1]

    def test_non_iso_dates_sort_lexicographically(self):

        ops = [
            {"id": 1, "date": "31.12.2020"},
            {"id": 2, "date": "01.01.2019"},
        ]
        result = sort_by_date(ops, reverse=False)

        assert [op["id"] for op in result] == [2, 1]

    def test_non_iso_dates_can_sort_incorrectly(self):
        """Демонстрация проблемы: '9' > '1', хотя 2020-09 < 2021-01."""
        ops = [
            {"id": 1, "date": "2021-01-01T00:00:00.000000"},
            {"id": 2, "date": "2020-09-01T00:00:00.000000"},
        ]
        result = sort_by_date(ops, reverse=False)

        assert [op["id"] for op in result] == [2, 1]

    @pytest.mark.parametrize("bad_input", [None, "not a list", 42])
    def test_invalid_input_type(self, bad_input):
        with pytest.raises(TypeError):
            sort_by_date(bad_input)