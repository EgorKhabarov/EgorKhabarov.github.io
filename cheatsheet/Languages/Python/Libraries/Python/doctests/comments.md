# Специальные комментарии в Doctests

### ELLIPSIS
`# doctest: +ELLIPSIS`
Позволяет использовать "..." для обозначения пропущенных частей вывода.

### IGNORE_EXCEPTION_DETAIL
`# doctest: +IGNORE_EXCEPTION_DETAIL`
Игнорирует детали сообщений об ошибках (например, игнорируется описание ошибки, остаётся только её тип).
```python
def raise_error():
    """
    Игнорирование деталей исключения:

    >>> raise_error()
    Traceback (most recent call last):
      ...
    ZeroDivisionError
    # doctest: +IGNORE_EXCEPTION_DETAIL
    """
    raise ZeroDivisionError("division by zero")
```

### SKIP
`# doctest: +SKIP`
Пропускает выполнение конкретного теста.

### NORMALIZE_WHITESPACE
`# doctest: +NORMALIZE_WHITESPACE`
Игнорирует различия в пробелах (например, различия в количестве пробелов или табуляций).
```python
def whitespace_example():
    """
    Пример с игнорированием пробелов:

    >>> whitespace_example()
    'text with    spaces'
    # doctest: +NORMALIZE_WHITESPACE
    """
    return "text with    spaces"
```

### FAIL_FAST
`# doctest: +FAIL_FAST`
Прекращает тестирование при первой неудаче.
```python
def fail_fast_example():
    """
    Пример с быстрой ошибкой:

    >>> fail_fast_example()  # doctest: +FAIL_FAST
    100
    """
    return 50
```

### REPORT_NDIFF
`# doctest: +REPORT_NDIFF`
Показывает различия между выводом теста и ожидаемым результатом с использованием стиля `ndiff`
который даёт более подробный отчёт о различиях.
```python
def diff_report():
    """
    Пример с подробным отчетом:

    >>> diff_report()
    'Hello World'
    # doctest: +REPORT_NDIFF
    """
    return "Hello world"
```

### REPORT_ONLY_FIRST_FAILURE
`# doctest: +REPORT_ONLY_FIRST_FAILURE`
Показывает только первый неудачный тест (остальные ошибки игнорируются).
```python
def report_only_first():
    """
    Пример с отчетом только о первой неудаче:

    >>> report_only_first()  # doctest: +REPORT_ONLY_FIRST_FAILURE
    100
    """
    return 50
```

### ALLOW_UNICODE
`# doctest: +ALLOW_UNICODE`
Разрешает различия между байтовыми строками и строками Юникода в результатах тестов.
```python
def allow_unicode():
    """
    Пример с поддержкой Unicode:

    >>> allow_unicode()
    'тест'
    # doctest: +ALLOW_UNICODE
    """
    return "тест"
```

### ALLOW_BYTES
`# doctest: +ALLOW_BYTES`
Разрешает сравнивать строки с байтовыми строками.
```python
def allow_bytes():
    """
    Пример с байтовыми строками:

    >>> allow_bytes()
    b'hello'
    # doctest: +ALLOW_BYTES
    """
    return b"hello"
```

### FLOAT_CMP
`# doctest: +FLOAT_CMP`
Игнорирует незначительные различия при сравнении чисел с плавающей точкой (например, различия в точности).
```python
def float_cmp_example():
    """
    Пример с сравнением чисел с плавающей точкой:

    >>> float_cmp_example()
    0.3333333333333333
    # doctest: +FLOAT_CMP
    """
    return 1 / 3
```

### ALL
`# doctest: -ALL`
Отключает все флаги, которые были активированы до этого момента.
```python
def disable_all_flags():
    """
    Пример с отключением всех флагов:

    >>> disable_all_flags()
    42
    # doctest: +SKIP
    >>> disable_all_flags()  # doctest: -ALL
    42
    """
    return 42
```

# Дополнительные специальные комментарии
- `# doctest: +REQUIRES("module")` Пропускает тест, если указанный модуль не установлен.
```python
def requires_module():
    """
    Пример с проверкой наличия модуля:

    >>> requires_module()  # doctest: +REQUIRES("non_existent_module")
    """
    return 42
```

## Комбинирование специальных комментариев
Вы можете комбинировать несколько флагов в одном тесте, разделяя их запятыми:

```python
def combined_flags():
    """
    Пример с несколькими флагами:

    >>> combined_flags()
    'This is a long string ...'
    # doctest: +ELLIPSIS, +NORMALIZE_WHITESPACE
    """
    return "This is a long string with unnecessary    spaces"
```

## Запуск doctest с флагами
Вы можете запускать doctests с этими флагами через командную строку или внутри кода:
```bash
python -m doctest -v your_script.py
```

Или программно:
```python
import doctest
doctest.testmod(optionflags=doctest.ELLIPSIS | doctest.NORMALIZE_WHITESPACE)
```
