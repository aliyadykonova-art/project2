import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

file_handler = logging.FileHandler("logs/masks.log", mode="w", encoding="utf-8")
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


def get_mask_card_number(card_number: str) -> str:
    card_number_formatted = ""

    for i in range(len(card_number)):
        if i > 0 and i % 4 == 0:
            card_number_formatted += " "

        if i > 5 and i < 12:
            card_number_formatted += "*"
        else:
            card_number_formatted += card_number[i]

    logger.info("Номер карты успешно замаскирован")
    return card_number_formatted


def get_mask_account(card_number: str) -> str:
    result = "**" + card_number[-4:]
    logger.info("Номер счета успешно замаскирован")
    return result
