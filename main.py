from src.generators import filter_by_currency  # Импортируем новые функции
from src.generators import card_number_generator, transaction_descriptions
from src.masks import get_mask_account, get_mask_card_number
from src.processing import filter_by_state, sort_by_date
from src.widget import get_date, mask_account_card

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

        print("\nПо статусу (EXECUTED):")
        print(executed_ops)
        print("\nПо статусу (CANCELED):")
        print(canceled_ops)
        print("\nПо дате (по убыванию):")
        print(sorted_ops_desc)
        print("\nПо дате (по возрастанию):")
        print(sorted_ops_asc)

    except ValueError as e:
        print(f"Ошибка: {e}")

    # --- Тесты для generators ---
    print("\n--- generators ---")

    transactions = [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160",
        },
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229",
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657",
        },
    ]

    print("\n1. filter_by_currency (USD):")
    try:
        usd_transactions = filter_by_currency(transactions, "USD")
        for _ in range(2):  # Выведем 2 транзакции в USD
            print(next(usd_transactions))
    except StopIteration:
        print("Больше нет транзакций в USD")

    print("\n2. transaction_descriptions (первые 5):")
    try:
        descriptions = transaction_descriptions(transactions)
        for _ in range(5):
            print(next(descriptions))
    except StopIteration:
        print("Больше нет описаний")

    print("\n3. card_number_generator (1-5):")
    for card_number in card_number_generator(1, 5):
        print(card_number)

    print("\n--- Конец generators ---")
