from typing import Any, Dict, List, Literal, Optional

def filter_by_state(operations: List[Dict[str, Any]], state: Literal['EXECUTED', 'CANCELED'] = 'EXECUTED') -> List[Dict[str, Any]]:
    """
    Фильтрует список операций по значению ключа 'state'
    """
    return [op for op in operations if op.get('state') == state]


def sort_by_date(operations: List[Dict[str, Any]], reverse: bool = True) -> List[Dict[str, Any]]:
    """
    Сортирует список операций по ключу 'date'
    """
    return sorted(operations, key=lambda x: x.get('date', ''), reverse=reverse)
