import pytest

from src.masks import get_mask_account, get_mask_card_number


def test_get_mask_card_number(card_number: str) -> None:
    """Тестирование правильности маскирования валидного номера карты"""
    result = get_mask_card_number(card_number)
    assert result == "1234 56** **** 3456"


def test_get_mask_card_number2() -> None:
    """Тестирование с коротким номером карты"""
    with pytest.raises(ValueError):
        get_mask_card_number("123456789012345")  # 15 цифр


def test_get_mask_card_number3() -> None:
    """Тестирование с длинным номером карты"""
    with pytest.raises(ValueError):
        get_mask_card_number("12345678901234567")  # 17 цифр


def test_get_mask_card_number4() -> None:
    """Тестирование с нечисловым номером карты"""
    with pytest.raises(ValueError):
        get_mask_card_number("123456789012345a")


def test_get_mask_account(account_number: str) -> None:
    """Тестирование правильности маскирования валидного номера счета"""
    result = get_mask_account(account_number)
    assert result == "**7890"


def test_get_mask_account1() -> None:
    """Тестирование с коротким номером"""
    with pytest.raises(ValueError):
        get_mask_account("123")


def test_get_mask_account2() -> None:
    """Тестирование с нечисловым номером счета"""
    with pytest.raises(ValueError):
        get_mask_account("1234567890123456789a")
