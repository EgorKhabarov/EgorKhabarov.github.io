ExceptionGroup в Python появился в версии 3.11
Позволяет объединять несколько исключений в одно


### Пример 1: Создание ExceptionGroup

```python
>>> try:
...     raise ExceptionGroup("Ошибка выполнения операций", [
...         ValueError("Некорректное значение"),
...         TypeError("Неверный тип данных"),
...         KeyError("Ключ не найден")
...     ])
... except ExceptionGroup as eg:
...     print(f"Произошло {len(eg.exceptions)} исключений:")
...     for exc in eg.exceptions:
...         print(f"- {exc.__class__.__name__}: {exc}")
Произошло 3 исключений:
- ValueError: Некорректное значение
- TypeError: Неверный тип данных
- KeyError: 'Ключ не найден'
```

### Пример 2: Обработка отдельных исключений внутри группы

```python
>>> try:
...     raise ExceptionGroup("Ошибка выполнения операций", [
...         ValueError("Некорректное значение"),
...         TypeError("Неверный тип данных"),
...         KeyError("Ключ не найден")
...     ])
... except* ValueError as v_errors:
...     for error in v_errors.exceptions:  # Итерируемся по списку исключений внутри группы
...         print(f"Обработан ValueError: {error}")
... except* TypeError as t_errors:
...     for error in t_errors.exceptions:
...         print(f"Обработан TypeError: {error}")
...
Обработан ValueError: Некорректное значение
Обработан TypeError: Неверный тип данных
  + Exception Group Traceback (most recent call last):
  |   File "<stdin>", line 2, in <module>
  | ExceptionGroup: Ошибка выполнения операций (1 sub-exception)
  +-+---------------- 1 ----------------
    | KeyError: 'Ключ не найден'
    +------------------------------------
```

### Пример 3: Вложенные ExceptionGroup

```python
try:
    raise ExceptionGroup("Основная группа", [
        ExceptionGroup("Первая подгруппа", [
            ValueError("Некорректное значение"),
            KeyError("Ключ не найден"),
        ]),
        TypeError("Неверный тип данных"),
    ])
except ExceptionGroup as eg:
    pass
```

### Пример 4: Комбинирование и повторное создание ExceptionGroup

```python
def function_that_raises():
    errors = []
    try:
        raise ValueError("Первый ValueError")
    except ValueError as e:
        errors.append(e)

    try:
        raise TypeError("Первый TypeError")
    except TypeError as e:
        errors.append(e)

    if errors:
        raise ExceptionGroup("Группа исключений в функции", errors)

try:
    function_that_raises()
except ExceptionGroup as eg:
    pass
```

```pycon
>>> try:
...     raise ExceptionGroup("Ошибка выполнения операций", [
...         ValueError("Некорректное значение"),
...         TypeError("Неверный тип данных"),
...         KeyError("Ключ не найден")
...     ])
... except Exception as e:
...     print(e.exceptions)
...
(ValueError('Некорректное значение'), TypeError('Неверный тип данных'), KeyError('Ключ не найден'))
```
