import pytest
from src.widget import mask_account_card, get_date


def test_mask_account_card(card_string: str, card_number: str) -> None:
    """Тестирование маскировки карты"""
    expected = f"Visa Platinum {card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"
    result = mask_account_card(card_string)
    assert result == expected


def test_mask_account_card_account(account_string: str, account_number: str) -> None:
    """Тестирование маскировки счета"""
    expected = f"Счет **{account_number[-4:]}"
    result = mask_account_card(account_string)
    assert result == expected


def test_mask_account_card_length() -> None:
    """Тестирование mask_account_card с некорректным номером"""
    input_str = "Visa Invalid12345"
    result = mask_account_card(input_str)
    assert result == input_str

    input_str_2 = "Счет 123456789"
    result_2 = mask_account_card(input_str_2)
    assert result_2 == input_str_2

    input_str_3 = "Mir 123456789012345678901"
    result_3 = mask_account_card(input_str_3)
    assert result_3 == input_str_3


@pytest.mark.parametrize(
    "input_str, expected",
    [
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
        ("Счет 64686473678894779589", "Счет **9589"),
        ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
        ("Счет 35383033474447895560", "Счет **5560"),
        ("Visa Classic 6831982476737658", "Visa Classic 6831 98** **** 7658"),
        ("Visa Platinum 8990922113665229", "Visa Platinum 8990 92** **** 5229"),
        ("Visa Gold 5999414228426353", "Visa Gold 5999 41** **** 6353"),
        ("Счет 73654108430135874305", "Счет **4305"),
    ],
)
def test_mask_account_card_parametrize(input_str: str, expected: str) -> None:
    """Параметризованный тест для различных карт и счетов"""
    result = mask_account_card(input_str)
    assert result == expected


def test_get_date(date: str) -> None:
    """Тестирование правильности преобразования даты"""
    result = get_date(date)
    assert result == "11.03.2024"


def test_get_date_z() -> None:
    """Тестирование даты с Z на конце"""
    result = get_date("2023-12-02T23:00:00.000000Z")
    assert result == "02.12.2023"


def test_get_date_no_z() -> None:
    """Тестирование даты с без Z на конце"""
    result = get_date("2023-12-03T03:00:00.000000")
    assert result == "03.12.2023"
