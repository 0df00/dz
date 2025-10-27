from src.masks import get_mask_account, get_mask_card_number
from src.widget import mask_account_card, get_date
from src.processing import filter_by_state, sort_by_date

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
        print(mask_account_card("Счет 73654108430135874305"))  # Вернет: Счет **4305
        print(mask_account_card("Maestro 1596837868705199"))  # Вернет: Maestro 1596 83** **** 5199
        print(mask_account_card("Счет 64686473678894779589"))  # Вернет: Счет **9589

        print("\nТесты для get_date:")
        print(get_date("2024-03-11T02:26:18.671407"))  # Вернет: 11.03.2024
        print(get_date("2023-12-02T08:15:30.123456"))  # Вернет: 02.12.2023

        # Тесты для processing
        print("\nТесты для processing:")
        operations = [
            {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
            {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        ]

        # Фильтрация по статусу
        executed_ops = filter_by_state(operations)
        canceled_ops = filter_by_state(operations, state="CANCELED")

        # Сортировка по дате (по убыванию)
        sorted_ops_desc = sort_by_date(operations)
        # Сортировка по дате (по возрастанию)
        sorted_ops_asc = sort_by_date(operations, reverse=False)

        print("\nПо сатусу:")
        print(executed_ops)
        print("\nПо сатусу (CANCELED):")
        print(canceled_ops)
        print("\nПо дате (по убыванию):")
        print(sorted_ops_desc)
        print("\nПо дате (по возрастанию):")
        print(sorted_ops_asc)

    except ValueError as e:
        print(f"Ошибка: {e}")
