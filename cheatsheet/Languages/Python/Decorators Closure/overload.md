# @overload
Декоратор `@overload` позволяет описывать разные варианты вызова функций с конкретными типами параметров,
но его следует использовать вместе с одной фактической реализацией функции.

```python
from typing import overload

class Calculator:
    @overload
    def operate(self, a: int) -> int: ...

    @overload
    def operate(self, a: str) -> str: ...

    def operate(self, a):
        if isinstance(a, int):
            return a * 2
        elif isinstance(a, str):
            return a.upper()

calc = Calculator()
print(calc.operate(10))    # 20
print(calc.operate("abc")) # ABC
```

## \_\_init\_\_

```python
from typing import overload

class Person:
    @overload
    def __init__(self, name: str): ...

    @overload
    def __init__(self, age: int): ...

    def __init__(self, arg):
        if isinstance(arg, str):
            self.name = arg
            self.age = None
        elif isinstance(arg, int):
            self.age = arg
            self.name = None

p1 = Person("Alice")
p2 = Person(30)
```
