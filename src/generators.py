from typing import Any, Dict, Iterator, List  # Импортируем типы


def filter_by_currency(transactions: List[Dict[str, Any]], currency_code: str) -> Iterator[Dict[str, Any]]:
    """
    Фильтрует транзакции по указанной валюте
    """
    for transaction in transactions:
        transaction_currency_code = transaction.get("operationAmount", {}).get("currency", {}).get("code")
        if transaction_currency_code == currency_code:
            yield transaction


def transaction_descriptions(transactions: List[Dict[str, Any]]) -> Iterator[str]:
    """
    Генерирует описания транзакций
    """
    for transaction in transactions:
        description = transaction.get("description", "")
        yield description


def card_number_generator(start: int = 1, stop: int = 9999999999999999) -> Iterator[str]:
    """
    Генерирует номера банковских карт в формате XXXX XXXX XXXX XXXX
    """
    for number in range(start, stop + 1):
        num_str = str(number).zfill(16)
        yield f"{num_str[:4]} {num_str[4:8]} {num_str[8:12]} {num_str[12:]}"
