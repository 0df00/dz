from typing import Any, Dict, List

import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


def test_filter_by_currency_usd(transactions: List[Dict[str, Any]]) -> None:
    """Тестирование фильтрации по валюте USD"""
    usd_gen = filter_by_currency(transactions, "USD")
    result = list(usd_gen)  # Преобразуем генератор в список для проверки
    expected_ids = {939719570, 142264268, 895315941}
    assert len(result) == 3
    assert {t["id"] for t in result} == expected_ids


def test_filter_by_currency_rub(transactions: List[Dict[str, Any]]) -> None:
    """Тестирование фильтрации по валюте RUB"""
    rub_gen = filter_by_currency(transactions, "RUB")
    result = list(rub_gen)
    expected_ids = {873106923, 594226727}
    assert len(result) == 2
    assert {t["id"] for t in result} == expected_ids


def test_filter_by_currency_empty(transactions: List[Dict[str, Any]]) -> None:
    """Тестирование фильтрации по валюте которой нет"""
    empty_gen = filter_by_currency(transactions, "EUR")
    result = list(empty_gen)
    assert result == []


def test_filter_by_currency_err_data() -> None:
    """Тестирование с некорректными данными"""
    invalid_transactions = [
        {"id": 1, "operationAmount": {}},  # Нет currency
        {"id": 2, "operationAmount": {"currency": {}}},  # Нет code
        {"id": 3, "operationAmount": {"currency": {"code": "USD"}}},  # Корректно
    ]
    usd_gen = filter_by_currency(invalid_transactions, "USD")
    result = list(usd_gen)
    expected_ids = {3}
    assert {t["id"] for t in result} == expected_ids


@pytest.mark.parametrize(
    "desc_index, expected_desc",
    [
        (0, "Перевод организации"),
        (1, "Перевод со счета на счет"),
        (3, "Перевод с карты на карту"),
        (4, "Перевод организации"),
    ],
)
def test_transaction_descriptions(transactions: List[Dict[str, Any]], desc_index: int, expected_desc: str) -> None:
    """Параметризованный тест для описаний транзакций"""
    desc_gen = transaction_descriptions(transactions)
    descriptions_list = list(desc_gen)
    assert descriptions_list[desc_index] == expected_desc


def test_transaction_descriptions_empty() -> None:
    """Тестирование с пустым списком транзакций"""
    empty_gen = transaction_descriptions([])
    result = list(empty_gen)
    assert result == []


def test_transaction_descriptions_no() -> None:
    """Тестирование транзакции без описания"""
    transactions_with_missing_desc: List[Dict[str, Any]] = [
        {"id": 1},
        {"id": 2, "description": "Описание 2"},
    ]
    desc_gen = transaction_descriptions(transactions_with_missing_desc)
    result = list(desc_gen)
    assert result == ["", "Описание 2"]


@pytest.mark.parametrize(
    "start, stop, expected_numbers",
    [
        (1, 3, ["0000 0000 0000 0001", "0000 0000 0000 0002", "0000 0000 0000 0003"]),
        (9999, 10001, ["0000 0000 0000 9999", "0000 0000 0001 0000", "0000 0000 0001 0001"]),
        (
            1000000000000000,
            1000000000000002,
            ["1000 0000 0000 0000", "1000 0000 0000 0001", "1000 0000 0000 0002"],
        ),  # Проверка больших чисел
    ],
)
def test_card_number_generator_parametrized(start: int, stop: int, expected_numbers: List[str]) -> None:
    """Параметризованный тест для генератора номеров карт"""
    gen = card_number_generator(start, stop)
    result = list(gen)
    assert result == expected_numbers


def test_card_number_generator_single() -> None:
    """Тестирование генератора с диапазоном из одного числа"""
    gen = card_number_generator(5, 5)
    result = list(gen)
    assert result == ["0000 0000 0000 0005"]


def test_card_number_generator_empty() -> None:
    """Тестирование генератора с некорректным диапазоном (start > stop)"""
    gen = card_number_generator(5, 4)
    result = list(gen)
    assert result == []
