from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(input_str: str) -> str:
    """
    Маскирует номер карты или счета в строке
    """
    parts = input_str.split()
    number = parts[-1]

    if len(number) == 20:
        masked_number = get_mask_account(number)
        parts[-1] = masked_number
    elif len(number) == 16:
        masked_number = get_mask_card_number(number)
        parts[-1] = masked_number
    else:
        return input_str

    return " ".join(parts)


def get_date(date_string: str) -> str:
    """
    Преобразует строку даты '2024-03-11T02:26:18.671407' в 'ДД.ММ.ГГГГ'
    """
    from datetime import datetime
    date_obj = datetime.fromisoformat(
        date_string.replace('Z', '+00:00')
    ) if date_string.endswith('Z') else datetime.fromisoformat(date_string)
    return date_obj.strftime("%d.%m.%Y")
