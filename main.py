from src.masks import get_mask_account, get_mask_card_number

"""Загружает нашу библиотеку"""

if __name__ == "__main__":
    try:
        print(get_mask_card_number("1234567890123456"))  # Вернет: 1234 56** **** 3456
        print(get_mask_account("1234567890123456"))  # Вернет **3456
    except ValueError as e:
        print(f"Ошибка: {e}")
