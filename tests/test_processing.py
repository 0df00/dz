import pytest
from src.processing import filter_by_state, sort_by_date
from typing import List, Dict, Any


def test_filter_by_state_default(operations: List[Dict[str, Any]]) -> None:
    """Тестирование фильтрации по статусу по умолчанию (EXECUTED)"""
    result = filter_by_state(operations)
    executed_items = [op for op in operations if op["state"] == "EXECUTED"]
    assert result == executed_items


def test_filter_by_state_canceled(operations: List[Dict[str, Any]]) -> None:
    """Тестирование фильтрации по статусу CANCELED"""
    result = filter_by_state(operations, state="CANCELED")
    canceled_items = [op for op in operations if op["state"] == "CANCELED"]
    assert result == canceled_items


def test_filter_by_state_empty_result(operations: List[Dict[str, Any]]) -> None:
    """Тестирование фильтрации когда нет совпадений"""
    result = filter_by_state(operations, state="FAILED")
    assert result == []


@pytest.mark.parametrize(
    "state, expected_count",
    [
        ("EXECUTED", 2),
        ("CANCELED", 2),
        ("TEST_VALUE", 1),
        ("FAILED", 0),
    ],
)
def test_filter_by_state_parametrized(operations: List[Dict[str, Any]], state: str, expected_count: int) -> None:
    """Параметризованный тест для различных статусов"""
    result = filter_by_state(operations, state=state)
    assert len(result) == expected_count
    for item in result:
        assert item["state"] == state


def test_sort_by_date_desc(operations: List[Dict[str, Any]]) -> None:
    """Тестирование сортировки по убыванию (по умолчанию)"""
    result = sort_by_date(operations)
    correct_order_ids = [789012345, 41428829, 615064591, 594226727, 939719570]
    assert [op["id"] for op in result] == correct_order_ids


def test_sort_by_date_asc(operations: List[Dict[str, Any]]) -> None:
    """Тестирование сортировки по возрастанию"""
    result = sort_by_date(operations, reverse=False)
    correct_order_ids = [939719570, 594226727, 615064591, 41428829, 789012345]
    assert [op["id"] for op in result] == correct_order_ids


def test_sort_by_date_duble() -> None:
    """Тестирование сортировки, когда есть одинаковые даты"""
    ops_with_same_date = [
        {"id": 1, "state": "EXECUTED", "date": "2020-01-01T00:00:00.000000"},
        {"id": 2, "state": "CANCELED", "date": "2020-01-01T00:00:00.000000"},
        {"id": 3, "state": "TEST_VALUE", "date": "2019-12-31T23:59:59.999999"},
    ]
    result_desc = sort_by_date(ops_with_same_date)
    assert result_desc[2]["id"] == 3
    assert set(op["id"] for op in result_desc[:2]) == {1, 2}

    result_asc = sort_by_date(ops_with_same_date, reverse=False)
    assert result_asc[0]["id"] == 3
    assert set(op["id"] for op in result_asc[1:3]) == {1, 2}
