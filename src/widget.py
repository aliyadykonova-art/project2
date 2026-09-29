from . import masks  # относительный import для файлов в одной папке


def mask_account_card(card_data: str) -> str:
    card_number = card_data.split(" ")[-1] # take only the card number
    card_type = card_data.rstrip(card_number)

    if card_type.startswith("Счет"):
        return card_type + masks.get_mask_account(card_number)
    else:
        return card_type + masks.get_mask_card_number(card_number)

def get_date(date: str) -> str:
    date_parts = date.split("-")

    day = date_parts[2][0:2]
    month = date_parts[1]
    year = date_parts[0]

    return f"{day}.{month}.{year}"
