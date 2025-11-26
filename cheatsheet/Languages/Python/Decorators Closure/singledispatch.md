# @singledispatch
`@singledispatch` позволяет перегружать функцию по типу первого аргумента
Он полезен для функций, работающих с разными типами данных

[[Languages/Python/Libraries/Python/functools]]

```python
from functools import singledispatch

@singledispatch
def process(arg):
    print(f"Unsupported type: {type(arg)}")

@process.register(int)
def _(arg: int):
    print(f"Integer: {arg * 2}")

@process.register(str)
def _(arg: str):
    print(f"String: {arg.upper()}")

process(10)       # Integer: 20
process("hello")  # String: HELLO
```
## @singledispatch для методов

Чтобы использовать `@singledispatch` с методами, нужно добавить дополнительный декоратор
[@staticmethod](?Languages/Python/Decorators%20Closure/staticmethod) или [@classmethod](?Languages/Python/Decorators%20Closure/classmethod), чтобы метод не принимал первый параметр `self`

```python
from functools import singledispatch

class Processor:
    @singledispatch
    @staticmethod
    def process(arg):
        print(f"Unsupported type: {type(arg)}")

    @process.register(int)
    @staticmethod
    def _(arg: int):
        print(f"Processing integer: {arg * 2}")

    @process.register(str)
    @staticmethod
    def _(arg: str):
        print(f"Processing string: {arg.upper()}")

Processor.process(10)       # Processing integer: 20
Processor.process("hello")  # Processing string: HELLO
```
