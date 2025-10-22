from src.masks import get_mask_account, get_mask_card_number
from src.widget import mask_account_card, get_date

"""Загружает нашу библиотеку"""

if __name__ == "__main__":
    try:
        # Тесты для masks (если нужно)
        print("Тесты для masks:")
        print(get_mask_card_number("1234567890123456"))  # Вернет: 1234 56** **** 3456
        print(get_mask_account("12345678901234567890"))  # Вернет **7890

        print("\nТесты для widget:")
        # Тесты для widget
        print(mask_account_card("Visa Platinum 7000792289606361"))  # Вернет: Visa Platinum 7000 79** **** 6361
        print(mask_account_card("Счет 73654108430135874305"))      # Вернет: Счет **4305
        print(mask_account_card("Maestro 1596837868705199"))       # Вернет: Maestro 1596 83** **** 5199
        print(mask_account_card("Счет 64686473678894779589"))      # Вернет: Счет **9589

        print("\nТесты для get_date:")
        print(get_date("2024-03-11T02:26:18.671407"))             # Вернет: 11.03.2024
        print(get_date("2023-12-02T08:15:30.123456"))             # Вернет: 02.12.2023

    except ValueError as e:
        print(f"Ошибка: {e}")
