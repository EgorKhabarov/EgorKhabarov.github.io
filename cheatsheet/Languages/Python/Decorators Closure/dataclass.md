# \_\_all\_\_

| Название                   | Описание                                                                                                                                    |
|----------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| `@dataclass`               | Декоратор для автоматического создания методов класса, таких как `__init__`, `__repr__`, `__eq__`, и других                                 |
| `field`                    | Функция для настройки полей внутри датакласса. Позволяет задать значения по умолчанию, фабрики значений, а также управлять поведением полей |
| `Field`                    | Класс, представляющий метаинформацию о полях датакласса. Создаётся автоматически при использовании `field()`                                |
| `FrozenInstanceError`      | Исключение, которое возникает при попытке изменить поле объекта неизменяемого (`frozen=True`) датакласса                                    |
| `InitVar`                  | Специальный тип для переменных, которые используются только в `__init__` и не сохраняются как атрибуты класса                               |
| `KW_ONLY`                  | Специальная константа, используемая для обозначения полей, которые должны передаваться только через ключевые аргументы в `__init__`         |
| `MISSING`                  | Значение, указывающее на отсутствие значения по умолчанию для поля, используется библиотекой автоматически                                  |
| `fields`                   | Функция, возвращающая информацию о полях класса (список объектов `Field`)                                                                   |
| `asdict`                   | Функция, которая преобразует объект датакласса в словарь, где ключами являются имена полей, а значениями — данные этих полей                |
| `astuple`                  | Преобразует объект датакласса в кортеж с последовательными значениями полей                                                                 |
| `make_dataclass`           | Функция для динамического создания нового датакласса с указанными полями и их типами                                                        |
| `replace`                  | Возвращает копию объекта датакласса с изменёнными значениями указанных полей                                                                |
| `is_dataclass`             | Функция, проверяющая, является ли объект экземпляром датакласса                                                                             |

# Описание

## @dataclass
Основной декоратор для объявления классов данных. Автоматически генерирует методы `__init__`, `__repr__`, `__eq__`, и другие.

```python
from dataclasses import dataclass

@dataclass
class Person:
    name: str
    age: int
```
### Параметры dataclass

```python
@dataclass(
    *,
    init: bool = ...,
    repr: bool = ...,
    eq: bool = ...,
    order: bool = ...,
    unsafe_hash: bool = ...,
    frozen: bool = ...,
)
```

|               |                                                                                                                 |
|---------------|-----------------------------------------------------------------------------------------------------------------|
| `init`        | Нужно ли автоматически генерировать метод `__init__` для инициализации атрибутов класса                         |
| `repr`        | Нужно ли автоматически генерировать метод `__repr__` для вывода строкового представления объектов класса        |
| `eq`          | Нужно ли автоматически генерировать метод `__eq__` для сравнения объектов класса                                |
| `order`       | Нужно ли автоматически генерировать методы `__lt__`, `__le__`, `__gt__`, `__ge__` для сравнения объектов класса |
| `unsafe_hash` | Нужно ли автоматически генерировать метод `__hash__` для объектов класса.<br>Обычно этот аргумент следует использовать только для классов, объекты которых неизменяемы `frozen`,<br>так как изменяемые объекты могут привести к неожиданным результатам |
| `frozen`      | Нужно ли сделать объекты класса неизменяемыми `immutable`                                                       |

#### Значения по умолчанию

```python
@dataclass(
    *,
    init: bool = True,
    repr: bool = True,
    eq: bool = True,
    order: bool = True,
    unsafe_hash: bool = True,
    frozen: bool = False,
)
```

## field
Используется для более точной настройки полей.
Например, можно задать фабрику значений по умолчанию или исключить поле из конструктора.

```python
from dataclasses import dataclass, field

@dataclass
class Person:
    name: str
    age: int = field(default=18)  # Значение по умолчанию
    friends: list = field(default_factory=list)  # Фабрика для списка
```

## Field
Объект, создаваемый при использовании функции `field()`.
Содержит информацию о поле, его значении по умолчанию, фабрике значений и других метаданных.

## FrozenInstanceError
Исключение, которое генерируется, если пытаются изменить поле объекта неизменяемого датакласса.

```python
from dataclasses import dataclass, FrozenInstanceError

@dataclass(frozen=True)
class Point:
    x: int
    y: int

p = Point(1, 2)
# p.x = 10  # Вызовет FrozenInstanceError
```

## InitVar
Используется для создания переменных, которые существуют только на этапе инициализации и не сохраняются в объекте.

```python
from dataclasses import dataclass, InitVar

@dataclass
class Person:
    name: str
    age: InitVar[int]  # Не сохраняется в объекте
```

## KW_ONLY
Позволяет указать, что некоторые поля должны передаваться только как именованные аргументы при создании объекта.

```python
from dataclasses import dataclass, KW_ONLY

@dataclass
class Person:
    name: str
    KW_ONLY
    age: int
```

## MISSING
Специальное значение, используемое библиотекой `dataclasses` для обозначения отсутствия значения по умолчанию для поля.

## fields
Возвращает список полей класса в виде объектов `Field`.

```python
from dataclasses import dataclass, fields

@dataclass
class Person:
    name: str
    age: int

print(fields(Person))  # Выводит информацию о полях класса
```

## asdict
Преобразует объект датакласса в словарь.

```python
from dataclasses import dataclass, asdict

@dataclass
class Person:
    name: str
    age: int

p = Person("Alice", 30)
print(asdict(p))  # {"name": "Alice", "age": 30}
```

## astuple
Преобразует объект датакласса в кортеж.

```python
from dataclasses import astuple

print(astuple(p))  # ("Alice", 30)
```

## make_dataclass
Создаёт новый датакласс на лету с указанными полями.

```python
from dataclasses import make_dataclass

Point = make_dataclass("Point", [("x", int), ("y", int)])
p = Point(1, 2)
print(p)  # Point(x=1, y=2)
```

## replace
Возвращает новую копию объекта с изменёнными полями.

```python
from dataclasses import replace

p2 = replace(p, age=35)
print(p2)  # Person(name="Alice", age=35)
```

## is_dataclass
Проверяет, является ли объект экземпляром датакласса.

```python
from dataclasses import is_dataclass

print(is_dataclass(p))  # True
```




## \_\_post_init\_\_

Специальный метод, используемый **только в датаклассах** (аннотированных с помощью декоратора `@dataclass`).
Его основное предназначение — выполнить дополнительные действия или инициализацию после того, как автоматически сгенерированный метод `__init__` завершит свою работу.
В обычных классах этот метод не используется автоматически и его наличие не имеет смысла без использования библиотеки `dataclasses`.

Когда создается объект датакласса, Python сначала автоматически вызывает метод `__init__`, который создается на основе полей, объявленных в классе.
После этого, если в классе определен метод `__post_init__`, он будет вызван **сразу после** инициализации полей.

### Пример

```python
from dataclasses import dataclass

@dataclass
class Employee:
    name: str
    base_salary: float
    bonus_percentage: float = 0.0
    total_salary: float = 0.0

    def __post_init__(self):  # Выполняется сразу после создания объекта
        # Рассчитываем итоговую зарплату на основе бонуса
        self.total_salary = self.base_salary + (self.base_salary * self.bonus_percentage / 100)

emp = Employee(name="Alice", base_salary=1000, bonus_percentage=10)
print(emp)  # Employee(name="Alice", base_salary=1000, bonus_percentage=10, total_salary=1100.0)
```

### Особенности

1. **Модификация значений полей**: `__post_init__` часто используется для выполнения дополнительных вычислений или проверок,
требующих значений уже инициализированных полей
2. **Работа с `InitVar`**: Если в датаклассе используются поля `InitVar`, они передаются в `__post_init__`,
так как они не сохраняются как обычные атрибуты. Это полезно для временных параметров и инициализаций

### Пример с InitVar
Значение `celsius` передается в метод `__post_init__` и используется для вычисления значения поля `fahrenheit`
```python
from dataclasses import dataclass, InitVar

@dataclass
class TemperatureConverter:
    celsius: InitVar[float]
    fahrenheit: float = 0.0

    def __post_init__(self, celsius):
        # Преобразование градусов Цельсия в Фаренгейты
        self.fahrenheit = celsius * 9/5 + 32

temp = TemperatureConverter(celsius=25)
print(temp)  # TemperatureConverter(fahrenheit=77.0)
```
