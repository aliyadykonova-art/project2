def get_mask_card_number(card_number: str) -> str:
    card_number_formatted = ""

    for i in range(len(card_number)):
        if i > 0 and i % 4 == 0:
            card_number_formatted += " "

        if i > 5 and i < 12:
            card_number_formatted += "*"
        else:
            card_number_formatted += card_number[i]            
    return card_number_formatted

def get_mask_account(card_number: str) -> str:
    return "**" + card_number[-4::]
