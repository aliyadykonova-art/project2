from unittest.mock import Mock, patch

from src.external_api import convert_currency


def test_convert_rub():
    transaction = {
        "amount": "1000",
        "currency": "RUB",
    }

    result = convert_currency(transaction)

    assert result == 1000.0


@patch("src.external_api.requests.get")
def test_convert_usd(mock_get):
    mock_response = Mock()
    mock_response.json.return_value = {
        "rates": {
            "RUB": 80.0,
        }
    }
    mock_response.raise_for_status.return_value = None
    mock_get.return_value = mock_response

    transaction = {
        "amount": "100",
        "currency": "USD",
    }

    result = convert_currency(transaction)

    assert result == 8000.0

    mock_get.assert_called_once()


@patch("src.external_api.requests.get")
def test_convert_eur(mock_get):
    mock_response = Mock()
    mock_response.json.return_value = {
        "rates": {
            "RUB": 90.0,
        }
    }
    mock_response.raise_for_status.return_value = None
    mock_get.return_value = mock_response

    transaction = {
        "amount": "100",
        "currency": "EUR",
    }

    result = convert_currency(transaction)

    assert result == 9000.0

    mock_get.assert_called_once()
