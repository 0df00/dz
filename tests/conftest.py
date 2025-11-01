import pytest
from typing import List, Dict, Any


@pytest.fixture
def card_number() -> str:
    """Фикстура для валидного номера карты"""
    return "1234567890123456"


@pytest.fixture
def card_string() -> str:
    """Фикстура для карты"""
    return "Visa Platinum 1234567890123456"


@pytest.fixture
def account_number() -> str:
    """Фикстура для валидного номера счета"""
    return "12345678901234567890"


@pytest.fixture
def account_string() -> str:
    """Фикстура для счета"""
    return "Счет 12345678901234567890"


@pytest.fixture
def date() -> str:
    """Фикстура для даты"""
    return "2024-03-11T02:26:18.671407"


@pytest.fixture
def operations() -> List[Dict[str, Any]]:
    """Фикстура для списка операций"""
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 789012345, "state": "TEST_VALUE", "date": "2020-01-01T00:00:00.000000"},
    ]
