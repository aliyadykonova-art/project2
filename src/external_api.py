import os

import requests
from dotenv import load_dotenv

load_dotenv()


def convert_currency(transaction: dict) -> float:
    """Convert transaction amount from USD or EUR to RUB."""
    amount = float(transaction["amount"])
    currency = transaction["currency"]

    if currency == "RUB":
        return amount

    if currency not in ("USD", "EUR"):
        return amount

    api_key = os.getenv("API_KEY")

    if api_key is None:
        raise ValueError("API_KEY is not set")

    response = requests.get(
        "https://api.apilayer.com/exchangerates_data/latest",
        params={
            "base": currency,
            "symbols": "RUB",
        },
        headers={"apikey": api_key},
        timeout=10,
    )

    response.raise_for_status()

    data = response.json()
    rate = data["rates"]["RUB"]

    return float(amount * rate)
