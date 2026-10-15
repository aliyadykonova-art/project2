from unittest.mock import MagicMock, patch

from src.external_api import convert_to_rub


def test_convert_rub() -> None:
    """Тест возврата суммы без запроса к API, если валюта RUB."""
    transaction = {"operationAmount": {"amount": "100.0", "currency": {"code": "RUB"}}}
    assert convert_to_rub(transaction) == 100.0


@patch("os.getenv", return_value="fake_api_key")
@patch("requests.get")
def test_convert_usd_success(mock_get: MagicMock, mock_getenv: MagicMock) -> None:
    """Тест успешной конвертации USD в RUB с помощью маков."""
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {"result": 7500.0}

    transaction = {"operationAmount": {"amount": "100.0", "currency": {"code": "USD"}}}
    assert convert_to_rub(transaction) == 7500.0


def test_convert_invalid_transaction() -> None:
    """Тест обработки некорректных данных транзакции."""
    assert convert_to_rub({}) == 0.0
