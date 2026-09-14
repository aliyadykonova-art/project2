def get_mask_card_number(card_number: str) -> str:
    result = ""
    #Функция маскировки номера карты
    for i in range(len(card_number)):
        if i > 0 and i % 4 == 0:
            result += " "
           #Считает числа до 4 и ставит пробел
        if i > 5 and i < 12:
            result += "*"
            #читает числа от 5 до 12 и скрывает их
        else:
            result += card_number[i]

    return result

def get_mask_account(card_number: str) -> str:
            #читывает последние 4 числа и перед ним ставит звездочки
    return "**" + card_number[-4::]