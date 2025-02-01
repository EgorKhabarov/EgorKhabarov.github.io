Библиотека `operator` в Python предоставляет функции, которые соответствуют основным операциям,
таким как арифметические, логические, сравнения и работа с атрибутами, элементами и срезами.
Эти функции полезны для повышения читабельности и производительности кода, особенно
при использовании в функциях высшего порядка, таких как `map()`, `filter()` и `reduce()`.

# Арифметические операции

| Функция                   | Описание            | Пример                            |
|---------------------------|---------------------|-----------------------------------|
| `operator.add(a, b)`      | Возвращает `a + b`  | `operator.add(2, 3)` => `5`       |
| `operator.sub(a, b)`      | Возвращает `a - b`  | `operator.sub(5, 3)` => `2`       |
| `operator.mul(a, b)`      | Возвращает `a * b`  | `operator.mul(2, 3)` => `6`       |
| `operator.truediv(a, b)`  | Возвращает `a / b`  | `operator.truediv(7, 2)` => `3.5` |
| `operator.floordiv(a, b)` | Возвращает `a // b` | `operator.floordiv(7, 2)` => `3`  |
| `operator.mod(a, b)`      | Возвращает `a % b`  | `operator.mod(7, 2)` => `1`       |
| `operator.pow(a, b)`      | Возвращает `a ** b` | `operator.pow(2, 3)` => `8`       |
| `operator.neg(a)`         | Возвращает `-a`     | `operator.neg(5)` => `-5`         |
| `operator.pos(a)`         | Возвращает `+a`     | `operator.pos(-5)` => `-5`        |
| `operator.abs(a)`         | Возвращает `abs(a)` | `operator.abs(-5)` => `5`         |

# Логические операции

| Функция               | Описание                                | Пример                                  |
|-----------------------|-----------------------------------------|-----------------------------------------|
| `operator.and_(a, b)` | Логическое **И**: `a & b`               | `operator.and_(True, False)` => `False` |
| `operator.or_(a, b)`  | Логическое **ИЛИ**: <code>a \| b</code> | `operator.or_(True, False)` => `True`   |
| `operator.xor(a, b)`  | Логическое **XOR**: `a ^ b`             | `operator.xor(True, False)` => `True`   |
| `operator.not_(a)`    | Логическое **НЕ**: `not a`              | `operator.not_(True)` => `False`        |

# Сравнения

| Функция                 | Описание                | Пример                                  |
|-------------------------|-------------------------|-----------------------------------------|
| `operator.eq(a, b)`     | Возвращает `a == b`     | `operator.eq(2, 2)` => `True`           |
| `operator.ne(a, b)`     | Возвращает `a != b`     | `operator.ne(2, 3)` => `True`           |
| `operator.lt(a, b)`     | Возвращает `a < b`      | `operator.lt(2, 3)` => `True`           |
| `operator.le(a, b)`     | Возвращает `a <= b`     | `operator.le(2, 2)` => `True`           |
| `operator.gt(a, b)`     | Возвращает `a > b`      | `operator.gt(3, 2)` => `True`           |
| `operator.ge(a, b)`     | Возвращает `a >= b`     | `operator.ge(3, 2)` => `True`           |
| `operator.is_(a, b)`    | Возвращает `a is b`     | `operator.is_(a, b)` => `True/False`    |
| `operator.is_not(a, b)` | Возвращает `a is not b` | `operator.is_not(a, b)` => `True/False` |

# Операции с последовательностями

| Функция                       | Описание                                                   | Пример                                                    |
|-------------------------------|------------------------------------------------------------|-----------------------------------------------------------|
| `operator.concat(a, b)`       | Соединяет две последовательности                           | `operator.concat([1, 2], [3, 4])` => `[1, 2, 3, 4]`       |
| `operator.contains(a, b)`     | Проверяет, содержится ли `b` в `a`                         | `operator.contains([1, 2, 3], 2)` => `True`               |
| `operator.countOf(a, b)`      | Возвращает количество вхождений `b` в `a`                  | `operator.countOf([1, 2, 2, 3], 2)` => `2`                |
| `operator.indexOf(a, b)`      | Возвращает индекс первого вхождения `b` в `a`              | `operator.indexOf([1, 2, 3], 2)` => `1`                   |
| `operator.itemgetter(*items)` | Возвращает функцию, которая извлекает элементы по индексам | `f = operator.itemgetter(1, 2); f([1, 2, 3])` => `(2, 3)` |

# Операции с атрибутами и элементами

| Функция                       | Описание                                                   | Пример                                                    |
|-------------------------------|------------------------------------------------------------|-----------------------------------------------------------|
| `operator.attrgetter(attr)`   | Возвращает функцию, которая извлекает атрибут `attr`       | `f = operator.attrgetter("name"); f(obj)` => `"name"`     |
| `operator.itemgetter(*items)` | Возвращает функцию, которая извлекает элементы по индексам | `f = operator.itemgetter(1, 2); f([1, 2, 3])` => `(2, 3)` |
| `operator.setitem(a, b, c)`   | Устанавливает значение `c` элементу `b` в `a`              | `operator.setitem(my_dict, "key", "value")`               |
| `operator.delitem(a, b)`      | Удаляет элемент `b` из `a`                                 | `operator.delitem(my_dict, "key")`                        |
| `operator.getitem(a, b)`      | Извлекает элемент `b` из `a`                               | `operator.getitem(my_list, 0)` => `1`                     |

# Работа с срезами

| Функция                               | Описание                                        | Пример                                              |
|---------------------------------------|-------------------------------------------------|-----------------------------------------------------|
| `operator.index(a)`                   | Возвращает индекс `a`                           | `operator.index([1, 2, 3], 2)` => `1`               |
| `operator.getslice(a, start, end)`    | Возвращает срез списка от `start` до `end`      | `operator.getslice([1, 2, 3, 4], 1, 3)` => `[2, 3]` |
| `operator.setslice(a, start, end, b)` | Заменяет срез списка от `start` до `end` на `b` | `operator.setslice(my_list, 1, 3, [7, 8])`          |
| `operator.delslice(a, start, end)`    | Удаляет срез списка от `start` до `end`         | `operator.delslice(my_list, 1, 3)`                  |

# Примеры использования

### Применение функций `operator` в `map()`
```python
import operator

numbers = [1, 2, 3, 4, 5]
squared = list(map(operator.pow, numbers, [2] * len(numbers)))
print(squared)  # [1, 4, 9, 16, 25]
```

### Использование `itemgetter` для сортировки списка словарей
```python
import operator

students = [
  {"name": "Alice", "age": 25},
  {"name": "Bob", "age": 20},
  {"name": "Charlie", "age": 23},
]
sorted_students = sorted(students, key=operator.itemgetter("age"))
print(sorted_students)
# [{"name": "Bob", "age": 20}, {"name": "Charlie", "age": 23}, {"name": "Alice", "age": 25}]
```
