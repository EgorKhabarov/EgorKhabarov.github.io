**Метаклассы** в Python — это классы, которые создают другие классы.
Они определяют, как классы будут создаваться и как будут вести себя в процессе их создания.

Метакласс — это класс, который наследует от `type`. Он управляет созданием и поведением других классов.
`type` — встроенный метакласс, который является метаклассом для всех классов в Python.

```python
class MyMeta(type):
    def __new__(cls, name, bases, dct):
        print(f"Creating class {name}")
        return super().__new__(cls, name, bases, dct)


class MyClass(metaclass=MyMeta):
   pass


obj = MyClass()  # При создании класса MyClass вызовется MyMeta.__new__
```

`__new__(cls, name, bases, dct)` — создаёт новый класс.

- `name` — имя создаваемого класса.
- `bases` — кортеж базовых классов.
- `dct` — словарь, содержащий атрибуты класса.

`__init__(cls, name, bases, dct)` — инициализирует созданный класс.
Можно использовать для добавления атрибутов или методов.


### Пример метакласса с изменением поведения

```python
class AddHelloMeta(type):
    """
    Автоматически добавляет метод hello
    """
    def __new__(cls, name, bases, dct):
        dct["hello"] = lambda self: "Hello, world!"
        return super().__new__(cls, name, bases, dct)


class MyClass(metaclass=AddHelloMeta):
   pass


obj = MyClass()
print(obj.hello())  # Hello, world!
```


### Пример [[General/Design%20patterns%20(Паттерны%20проектирования)/Creational%20patterns%20(Порождающие%20паттерны)/Singleton%20(Одиночка)]] с использованием метакласса

```python
class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


class Singleton(metaclass=SingletonMeta):
    pass


a = Singleton()
b = Singleton()
print(a is b)  # True
```
