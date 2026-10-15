import json
import logging
from unittest.mock import mock_open, patch

import pandas as pd

from src.utils import get_financial_data, read_transactions_from_csv, read_transactions_from_excel


def test_get_financial_data_valid() -> None:
    """Тест успешного чтения корректного JSON файла."""
    data = [{"id": 1, "amount": 100}]
    with patch("builtins.open", mock_open(read_data=json.dumps(data))):
        with patch("os.path.exists", return_value=True):
            assert get_financial_data("dummy_path.json") == data


def test_get_financial_data_file_not_found() -> None:
    """Тест возврата пустого списка, если JSON-файл не существует."""
    with patch("os.path.exists", return_value=False):
        assert get_financial_data("invalid_path.json") == []


def test_get_financial_data_invalid_json() -> None:
    """Тест обработчика ошибок при поврежденном JSON."""
    with patch("builtins.open", mock_open(read_data="invalid json")):
        with patch("os.path.exists", return_value=True):
            assert get_financial_data("dummy_path.json") == []


def test_get_financial_data_logging(caplog) -> None:
    """Тест проверяет, что при отсутствии JSON-файла записывается ERROR в лог."""
    with caplog.at_level(logging.ERROR):
        get_financial_data("non_existent_file.json")
        assert "Файл не найден по пути: non_existent_file.json" in caplog.text


def test_read_transactions_from_csv(tmp_path) -> None:
    """Тест успешного чтения транзакций из CSV-файла."""
    file_path = tmp_path / "test_transactions.csv"
    df = pd.DataFrame([{"id": 1, "amount": 150}, {"id": 2, "amount": 200}])
    df.to_csv(file_path, index=False)

    result = read_transactions_from_csv(str(file_path))
    assert len(result) == 2
    assert result[0]["amount"] == 150


def test_read_transactions_from_csv_not_found() -> None:
    """Тест обработки несуществующего CSV-файла."""
    assert read_transactions_from_csv("non_existent.csv") == []


def test_read_transactions_from_excel(tmp_path) -> None:
    """Тест успешного чтения транзакций из Excel-файла."""
    file_path = tmp_path / "test_transactions.xlsx"
    df = pd.DataFrame([{"id": 10, "amount": 500}])
    df.to_excel(file_path, index=False)

    result = read_transactions_from_excel(str(file_path))
    assert len(result) == 1
    assert result[0]["amount"] == 500


def test_read_transactions_from_excel_not_found() -> None:
    """Тест обработки несуществующего Excel-файла."""
    assert read_transactions_from_excel("non_existent.xlsx") == []
