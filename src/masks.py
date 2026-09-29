def get_mask_card_number(card_number: str) -> str:
    """Маскирует номер карты, заменяя символы с 6 по 11 на звездочки."""
    card_number_formatted = ""

    for i in range(len(card_number)):
        if i > 0 and i % 4 == 0:
            card_number_formatted += " "

        if 5 <= i <= 11:
            card_number_formatted += "*"
        else:
            card_number_formatted += card_number[i]

    return card_number_formatted


def get_mask_account(card_number: str) -> str:
    """Маскирует номер счета, оставляя только последние 4 цифры."""
    return "**" + card_number[-4:]
