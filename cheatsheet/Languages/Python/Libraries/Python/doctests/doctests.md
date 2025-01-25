```python
def add(a, b):
    """
    Возвращает сумму двух чисел.

    >>> add(2, 3)
    5
    >>> add(0, 0)
    0
    >>> add(-1, 1)
    0
    """
    return a + b

if __name__ == "__main__":
    import doctest
    doctest.testmod()
```

# Основные функции и методы

| Функция/Метод                      | Описание                                                                      |
|------------------------------------|-------------------------------------------------------------------------------|
| `doctest.testmod()`                | Тестирует текущий модуль, ищет и выполняет doctests, написанные в docstring   |
| `doctest.run_docstring_examples()` | Запускает примеры doctest для указанной функции или объекта                   |
| `doctest.ELLIPSIS`                 | Разрешает использование "..." в примерах для пропуска некоторых частей вывода |
| `doctest.FAIL_FAST`                | Прекращает выполнение тестов после первой ошибки                              |
| `doctest.IGNORE_EXCEPTION_DETAIL`  | Игнорирует различия в деталях ошибок при проверке исключений                  |

### Пример с исключением и использованием опций

```python
def divide(a, b):
    """
    Делит число a на b.

    Пример:
    >>> divide(4, 2)
    2.0
    >>> divide(4, 0)
    Traceback (most recent call last):
        ...
    ZeroDivisionError: division by zero
    """
    return a / b

if __name__ == "__main__":
    import doctest
    doctest.testmod(optionflags=doctest.ELLIPSIS)
```

# Как запускать

### Через код
Включить `doctest.testmod()` в своем коде.

### Через командную строку
Ключ `-v` (verbose) выводит подробные результаты выполнения тестов.
```bash
python -m doctest -v your_script.py
```

### Пример с обработкой ошибок

```python
def safe_divide(a, b):
    """
    Делит a на b, возвращает 0, если деление на 0.

    >>> safe_divide(4, 2)
    2.0
    >>> safe_divide(4, 0)
    0
    """
    try:
        return a / b
    except ZeroDivisionError:
        return 0
```
