import os

import requests
from dotenv import load_dotenv

load_dotenv()


def convert_to_rub(transaction: dict) -> float:
    """Конвертирует сумму транзакции в рубли через API."""
    try:
        amount = float(transaction["operationAmount"]["amount"])
        code = transaction["operationAmount"]["currency"]["code"]
    except (KeyError, ValueError, TypeError):
        return 0.0

    if code == "RUB":
        return amount

    if code in ["USD", "EUR"]:
        api_key = os.getenv("API_KEY")
        if not api_key:
            return 0.0

        url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={code}&amount={amount}"
        headers = {"apikey": api_key}
        try:
            response = requests.get(url, headers=headers)
            if response.status_code == 200:
                data = response.json()
                return float(data.get("result", 0.0))
        except requests.RequestException:
            return 0.0

    return amount
