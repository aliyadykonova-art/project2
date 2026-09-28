def get_mask_card_number(card_number: str) -> str:
    """Функция маскировки номера карты.

    Преобразует строку из 16 цифр в формат: XXXX XX** **** XXXX
    """
    # Убираем пробелы, если они были во входной строке
    card_number = card_number.replace(" ", "")

    # Вырезаем нужные части карты по индексам
    first_chunk = card_number[:4]
    second_chunk = card_number[4:6] + "**"
    third_chunk = "****"
    fourth_chunk = card_number[12:]

    # Собираем всё вместе через пробел
    return f"{first_chunk} {second_chunk} {third_chunk} {fourth_chunk}"


def get_mask_account(account_number: str) -> str:
    """Функция маскировки номера счета.

    Оставляет только последние 4 цифры счета и добавляет перед ними **.
    """
    return "**" + account_number[-4:]
