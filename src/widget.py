def mask_card_number(number: str) -> str:
    """Маскирует номер карты в формат"""
    if len(number) != 16:
        return number
    return f"{number[:4]} {number[4:6]}** **** {number[12:]}"


def mask_account_number(number: str) -> str:
    """Маскирует номер счета в формат"""
    if len(number) < 4:
        return number
    return f"**{number[-4:]}"
 

def mask_account_card(info: str) -> str:
    """Принимает строку с типом и номером карты/счета и маскирует номер."""
    # Разбиваем строку на отдельные элементы
    parts = info.split()

    # Последний элемент — это всегда номер, остальное — название
    number = parts[-1]
    name = " ".join(parts[:-1])

    # Проверяем тип и маскируем
    if name.lower() == "счет":
        masked_number = mask_account_number(number)
    else:
        masked_number = mask_card_number(number)

    return f"{name} {masked_number}"


def get_date(date_str: str) -> str:
    """Преобразует строку ISO даты 'YYYY-MM-DDTHH:MM:SS...' в 'ДД.ММ.ГГГГ'"""
    # Выделяем только часть с датой (до символа 'T')
    date_part = date_str.split("T")[0]
    # Разделяем год, месяц и день
    year, month, day = date_part.split("-")

    return f"{day}.{month}.{year}"
