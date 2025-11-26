# Динамическое создание классов

- Генерация классов по параметрам (ORM, API-стабы, формы, прокси)
- Фабрики классов (разные реализации для разных конфигураций)
- Автогенерация DTO / dataclass / namedtuple по описанию
- Паттерны (singleton через метакласс, регистрация плагинов)
- Тесты / мок-объекты / runtime-композиция

### type(name, bases, dict)

Самый простой и часто используемый `type(name, bases, dict)`

```python
def __init__(self, name):
    self.name = name

def greet(self):
    return f"Hello, {self.name}"

Person = type("Person", (object,), {
    "__init__": __init__,
    "greet": greet,
})

p = Person("Alice")
print(p.greet())  # Hello, Alice
```

### types.new_class()

Контролируем namespace через callback `types.new_class()`
Можно заполнить namespace с логикой, похожей на `class`-блок

```python
import types

def exec_body(namespace):
    namespace["x"] = 42
    def hello(self):
        return "hi"
    namespace["hello"] = hello

MyClass = types.new_class("MyClass", (object,), exec_body=exec_body)
obj = MyClass()
print(obj.x, obj.hello())  # 42 hi
```

### exec

Генерация кода как строки - гибко, но опасно

```python
namespace = {}
src = """
class Dyn:
    def __init__(self, x):
        self.x = x

    def inc(self):
        self.x += 1
"""
exec(src, globals(), namespace)
Dyn = namespace["Dyn"]
d = Dyn(10)
d.inc()
print(d.x)  # 11
```

### dataclasses.make_dataclass (Python 3.7+)

Удобно для автогенерации DTO/форм по метаданным
`dataclasses.make_dataclass`

```python
from dataclasses import make_dataclass, field

Person = make_dataclass(
    "Person",
    [
        ("name", str),
        ("age", int, field(default=0)),
    ],
)
p = Person("Bob", age=30)
print(p)  # Person(name="Bob", age=30)
```

### collections.namedtuple or typing.NamedTuple

Для иммутабельных записей `collections.namedtuple` or `typing.NamedTuple`

```python
from collections import namedtuple

Point = namedtuple("Point", ["x", "y"])
print(Point(1, 2))

# or

from typing import NamedTuple

Point2 = NamedTuple("Point2", [("x", int), ("y", int)])
```

### Динамическое добавление методов/атрибутов

```python
class A:
    pass

def greet(self):
    return "hi"

# Добавить метод в класс
A.greet = greet
print(A().greet())  # hi

# Добавить метод только конкретному экземпляру
from types import MethodType

a = A()
a.greet = MethodType(lambda self: "hello", a)
print(a.greet())  # hello
```

### Свойства и дескрипторы программно

```python
def prop_factory(name):
    def fget(self):
        return getattr(self, "_" + name)

    def fset(self, value):
        setattr(self, "_" + name, value)

    return property(fget, fset)

attrs = {
    "__init__": lambda self, v: setattr(self, "_val", v),
    "val": prop_factory("val")
}
C = type("C", (), attrs)
c = C(10)
print(c.val)  # 10
c.val = 20
print(c.val)  # 20
```

Или дескриптор:

```python
class Descriptor:
    def __init__(self, name):
        self.name = name

    def __get__(self, obj, cls):
        return obj.__dict__.get(self.name)

    def __set__(self, obj, value):
        obj.__dict__[self.name] = value

D = type("D", (), {"x": Descriptor("x")})
d = D()
d.x = 5
print(d.x)
```

### Метаклассы - контроль при создании класса

```python
class RegistryMeta(type):
    registry = {}
    def __new__(mcls, name, bases, namespace):
        cls = super().__new__(mcls, name, bases, namespace)
        mcls.registry[name] = cls
        return cls

class Base(metaclass=RegistryMeta):
    pass

class A(Base):
    pass

print(RegistryMeta.registry)  # {"Base": <class ...>, "A": <class ...>}
```

Метаклассы - мощный инструмент: вы можете изменить namespace, добавлять методы, валидировать и регистрировать классы

### `__init_subclass__` - лёгкая альтернатива метаклассам

`init_subclass`

```python
class Base:
    registry = {}
    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        Base.registry[cls.__name__] = cls

class A(Base):
    pass

print(Base.registry)  # {"A": <class ...>}
```

Удобно, когда нужно реагировать на создание подклассов, не создавая метакласс

# Полезные приёмы и шаблоны

### Кэширование фабрик (чтобы не создавать одинаковые классы несколько раз)

```python
from functools import lru_cache

@lru_cache(maxsize=None)
def make_point_class(dim):
    # Простая фабрика, создающая класс PointND
    attrs = {}

    def __init__(self, *coords):
        if len(coords) != dim:
            raise TypeError("wrong coords")
        for i, v in enumerate(coords):
            setattr(self, f"_{i}", v)

    attrs["__init__"] = __init__
    cls = type(f"Point{dim}D", (), attrs)
    cls.__doc__ = f"Point {dim}D"
    return cls

P3 = make_point_class(3)
p = P3(1, 2, 3)
```

### Singleton через метакласс

```python
class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

class S(metaclass=SingletonMeta):
    pass
```

### Автоматическое добавление методов (декоратор класса)

```python
def add_repr(cls):
    def __repr__(self):
        return f"<{cls.__name__} {self.__dict__!r}>"

    cls.__repr__ = __repr__
    return cls

@add_repr
class X: 
    def __init__(self, a):
        self.a = a
```

# Инспекция / аннотации / типы

* Можно задавать `__annotations__` в dict при `type` для совместимости с `dataclass`/статической типизацией

```python
attrs = {
    "__annotations__": {"x": int, "y": int},
    "__init__": lambda self, x, y: (setattr(self, "x", x), setattr(self, "y", y))
}
C = type("C", (), attrs)
```

* `inspect.getmembers`, `dir`, `vars(cls)`, `cls.__mro__` - для отладки/инспекции

# Подводные камни и предостережения

- **Безопасность `exec`**: никогда не выполняйте код, полученный от пользователя
- **Pickle**: динамически созданные классы часто **не сериализуются** корректно, т.к. pickle импортирует класс по имени из модуля. Решения: установить `cls.__module__ = 'my.module'` и/или зарегистрировать функции pickling через `copyreg`
- **MRO / конфликты метаклассов**: при множественном наследовании нужно следить за совместимостью метаклассов
- **Отладка**: stack traces могут быть менее информативны, если классы созданы динамично (проверьте `__name__`, `__qualname__`, `__module__`)
- **Производительность**: создание классов - дороже, чем создание экземпляров; кэшируйте, если создаёте много раз
- **Слоты и динамика**: если используете `__slots__`, нельзя динамически добавлять атрибуты в экземпляр, если слот не предусмотрен

# Практические советы

- Для простых структур - `namedtuple` или `make_dataclass`
- Для сложной логики / условных родителей - `type()` или `types.new_class`
- Для изменения процесса создания класса - `__init_subclass__` (легко) или метакласс (мощно)
- Для безопасной генерации кода - предпочтите фабрики на основе `type()` вместо `exec`, если возможно
- Для pickling: выставьте `cls.__module__` на модуль, который можно импортировать

# Короткие примеры-шаблоны

**Фабрика классов с параметром и кэшем**

```python
from functools import lru_cache

@lru_cache(None)
def make_serializer(name, fields):
    attrs = {"__slots__": tuple("_" + f for f in fields)}

    def __init__(self, *vals):
        for f, v in zip(fields, vals):
            setattr(self, "_" + f, v)

    attrs["__init__"] = __init__
    cls = type(name, (), attrs)
    cls.__module__ = __name__  # Помогает с pickle
    return cls
```

**Авто-регистрирующийся плагин (через `__init_subclass__`)**

```python
class PluginBase:
    registry = {}

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        PluginBase.registry[cls.__name__] = cls
```
