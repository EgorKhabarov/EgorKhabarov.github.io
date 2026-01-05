# functools

`functools` - Утилиты для работы с функциями, упрощая их применение, создание и комбинирование

| Функция/Атрибут          | Описание                                                                                                                                                                        | Пример использования                                                                |
|--------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------|
| `partial()`              | Создает новую функцию с частично фиксированными аргументами,<br>позволяя упростить вызов функции с заранее определенными аргументами                                            | `double = partial(multiply, y=2)`                                                   |
| `reduce()`               | Последовательно применяет функцию, принимающую два аргумента,<br>к элементам последовательности, сводя их к одному результату                                                   | `result = reduce(lambda x, y: x + y, numbers)`                                      |
| `lru_cache()`            | Декоратор для кэширования результатов функции,<br>что помогает избежать повторных вычислений при одинаковых входных данных                                                      | `@lru_cache(maxsize=None)`                                                          |
| `wraps()`                | Декоратор, сохраняющий метаданные оригинальной функции<br>(например, `__name__`, `__doc__`) при использовании декораторов                                                       | `@wraps(func)`                                                                      |
| `total_ordering()`       | Класс-декоратор, который автоматически добавляет все методы сравнения<br>(`<`, `<=`, `>`, `>=`), если определены `__eq__`<br>и один из (`__lt__`, `__le__`, `__gt__`, `__ge__`) | `@total_ordering`                                                                   |
| `cmp_to_key()`           | Преобразует функцию сравнения старого стиля в функцию,<br>возвращающую ключ для сортировки<br>(например, для использования в `sorted()` или `min()`)                            | `sorted_data = sorted(data, key=cmp_to_key(compare))`                               |
| `cache()`                | Декоратор для кэширования результатов функции,<br>аналогичный `lru_cache`, но без ограничений на размер кэша                                                                    | `@cache`                                                                            |
| `update_wrapper()`       | Обновляет метаданные функции-декоратора,<br>чтобы они соответствовали оригинальной функции                                                                                      | `update_wrapper(wrapper, wrapped)`                                                  |
| `partialmethod()`        | Позволяет создавать методы с частично<br>фиксированными аргументами для использования в классах                                                                                 | `partialmethod(func, arg1, arg2)`                                                   |
| `singledispatch()`       | Декоратор, который преобразует функцию<br>в обобщенную функцию с поддержкой однотипного диспетчеризации,<br>позволяя создавать перегрузки для разных типов аргументов           | `@singledispatch`                                                                   |
| `singledispatchmethod()` | Версия `singledispatch`, предназначенная<br>для использования в классах как метод, а не как функция                                                                             | `@singledispatchmethod`                                                             |
| `cached_property()`      | Декоратор, который превращает метод класса в свойство,<br>кэшируемое после первого вычисления                                                                                   | `@cached_property`                                                                  |
| `WRAPPER_ASSIGNMENTS`    | Список атрибутов, которые копируются<br>из оригинальной функции в функцию-декоратор                                                                                             | По умолчанию: `__module__` `__name__`<br>`__qualname__` `__doc__` `__annotations__` |
| `WRAPPER_UPDATES`        | Список атрибутов, которые обновляются<br>из оригинальной функции в функцию-декоратор                                                                                            | По умолчанию: `__dict__`                                                            |


# partial
Создает новую функцию с частично фиксированными аргументами
Удобно для переиспользования функций с предустановленными параметрами
```python
from functools import partial

def multiply(x, y):
    return x * y

# `y` всегда равен 2
print(partial(multiply, y=2)(5))  # 10
```

# reduce
Последовательно применяет функцию, принимающую два аргумента,
к элементам последовательности, сводя их к одному результату
```python
from functools import reduce

numbers = [1, 2, 3, 4, 5]
print(reduce(lambda x, y: x + y, numbers))  # 15
```

# lru_cache
Кэширует результаты функции, улучшая производительность за счет предотвращения повторных вычислений
С ограничением на количество сохраненных значений
Это полезно для оптимизации рекурсивных функций
```python
from functools import lru_cache

@lru_cache(maxsize=None)
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

@lru_cache(maxsize=128)
def factorial(n):
    return n * factorial(n-1) if n else 1

print(fibonacci(10))  # 55
print(factorial(5))  # 120
```

# wraps
Используется для создания декораторов, которые сохраняют метаданные декорируемой функции
```python
from functools import wraps

def my_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Вызов функции {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

@my_decorator
def greet(name):
    """Приветствие пользователя"""
    return f"Hello, {name}!"

print(greet("Alice"))  # "Hello, Alice!"
print(greet.__name__)  # "greet"
print(greet.__doc__)   # "Приветствие пользователя"
```

# total_ordering
Класс-декоратор, который добавляет методы сравнения (`<`, `<=`, `>`, `>=`) к классу,
если определены `__eq__` и один из (`__lt__`, `__le__`, `__gt__`, `__ge__`)
```python
from functools import total_ordering

@total_ordering
class Number:
    def __init__(self, value):
        self.value = value

    def __eq__(self, other):
        return self.value == other.value

    def __lt__(self, other):
        return self.value < other.value

n1 = Number(1)
n2 = Number(2)

print(n1 < n2)  # True
print(n1 > n2)  # False
```

# cmp_to_key
Преобразует функцию сравнения старого стиля в функцию, возвращающую ключ для сортировки
```python
from functools import cmp_to_key

def compare(x, y):
    return x - y

sorted_list = sorted([5, 3, 6, 2, 1], key=cmp_to_key(compare))
print(sorted_list)  # [1, 2, 3, 5, 6]
```

# cache
Декоратор, который кэширует результаты вызовов функции `func`
с одинаковыми аргументами, чтобы избежать повторных вычислений
```python
from functools import cache

@cache
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

@cache
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print(factorial(5))  # 120
print(fibonacci(10))  # 55
```

# update_wrapper
Обновляет метаданные функции-декоратора, чтобы они соответствовали оригинальной функции

```python
from functools import update_wrapper

def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("До вызова функции")
        return func(*args, **kwargs)
    return update_wrapper(wrapper, func)

@my_decorator
def my_function():
    print("Выполнение функции")

my_function()  # До вызова функции Выполнение функции
```

# partialmethod
Аналог `partial`, но используется для создания методов с частично фиксированными аргументами

```python
from functools import partialmethod

class MyClass:
    def multiply(self, x, y):
        return x * y

    double = partialmethod(multiply, y=2)

obj = MyClass()
print(obj.double(5))  # 10
```

# singledispatch
Позволяет создавать обобщенные функции с поддержкой
однотипного диспетчеризации (перегрузки) на основе типа первого аргумента

[[Languages/Python/Decorators Closure/singledispatch]]

```python
from functools import singledispatch

@singledispatch
def process(value):
    print(f"Обработка объекта: {value}")

@process.register(int)
def _(value):
    print(f"Обработка целого числа: {value}")

@process.register(str)
def _(value):
    print(f"Обработка строки: {value}")

process(10)   # Обработка целого числа: 10
process("hi") # Обработка строки: hi
```

# singledispatchmethod
То же самое, что `singledispatch`, но используется как метод класса

```python
from functools import singledispatchmethod

class Processor:
    @singledispatchmethod
    def process(self, value):
        print(f"Обработка объекта: {value}")

    @process.register(int)
    def _(self, value):
        print(f"Обработка целого числа: {value}")

    @process.register(str)
    def _(self, value):
        print(f"Обработка строки: {value}")

processor = Processor()
processor.process(10)   # Обработка целого числа: 10
processor.process("hi") # Обработка строки: hi
```

# cached_property
Позволяет кэшировать результат вычислений метода и использовать его как свойство
Значение вычисляется только один раз

```python
from functools import cached_property

class MyClass:
    @cached_property
    def heavy_computation(self):
        print("Выполняется вычисление...")
        return 42

obj = MyClass()
print(obj.heavy_computation)  # Выполняется вычисление ... 42
print(obj.heavy_computation)  # 42 (вычисление не выполняется повторно)
```

# WRAPPER_ASSIGNMENTS
Это кортеж, определяющий, какие атрибуты копируются из оригинальной функции в декорированную
По умолчанию копируются атрибуты: `__module__`, `__name__`, `__qualname__`, `__doc__`, `__annotations__`

# WRAPPER_UPDATES
Это кортеж, определяющий, какие атрибуты обновляются в декорированной функции
По умолчанию обновляется `__dict__`


# Частые применения
1. Оптимизация работы с функциями - использование `partial()` и `lru_cache()` для ускорения работы с часто вызываемыми функциями
2. Создание декораторов - с сохранением метаданных функции с помощью `wraps()`
3. Упрощение сравнения - автоматическое добавление методов сравнения с `total_ordering()`

# Полезные ссылки
- [Официальная документация](https://docs.python.org/3/library/functools.html)
- [Real Python - Guide to Python’s functools Module](https://realpython.com/python-functools/)
