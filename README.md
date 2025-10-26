# Мой Проект

## Использование
### Маскировка данных
Используйте функции из `src.masks` или `src.widget`:

```python
from src.masks import get_mask_card_number, get_mask_account
from src.widget import mask_account_card
print(mask_account_card("Visa Platinum 7000792289606361"))
print(mask_account_card("Счет 73654108430135874305"))
print(mask_account_card("Maestro 1596837868705199"))
print(mask_account_card("Счет 64686473678894779589"))
```
### Результат:
```
Visa Platinum 7000 79** **** 6361
Счет **4305
Maestro 1596 83** **** 5199
Счет **9589
```

### Фильтрация данных

```python
from src.processing import filter_by_state, sort_by_date

operations = [
    {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
    {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
    {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
]

# Фильтрация по статусу
executed_ops = filter_by_state(operations)
canceled_ops = filter_by_state(operations, state='CANCELED')

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
```
### Результат:
```
По сатусу:
[{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]

По сатусу (CANCELED):
[{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]

По дате (по убыванию):
[{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}, {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]

По дате (по возрастанию):
[{'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}, {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}, {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}]
```