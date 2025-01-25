## Классы
| Элемент            | Описание                                                                              |
|--------------------|---------------------------------------------------------------------------------------|
| `Enum`             | Базовый класс для создания перечислений                                               |
| `IntEnum`          | Подкласс `Enum`, значения должны быть целыми числами `int`                            |
| `StrEnum`          | Подкласс `Enum`, значения должны быть строками `str` (Начиная с _Python 3.11_)        |
| `Flag`             | Класс для битовых флагов. Позволяет комбинировать значения с помощью битовых операций |
| `IntFlag`          | Подкласс `Flag`, значения должны быть целыми числами `int`                            |

## Функции и атрибуты
| Элемент            | Описание                                                                                |
|--------------------|-----------------------------------------------------------------------------------------|
| `auto()`           | Функция для автоматической генерации значений перечисления                              |
| `unique()`         | Декоратор, который гарантирует, что все элементы перечисления имеют уникальные значения |
| `EnumMeta`         | Метакласс для создания перечислений                                                     |
| `Enum.__members__` | Возвращает словарь, содержащий все члены перечисления в порядке их определения          |
| `Enum.__name__`    | Возвращает имя перечисления                                                             |
| `Enum.value`       | Возвращает значение элемента перечисления                                               |
| `Enum.name`        | Возвращает имя элемента перечисления                                                    |

### Enum
Создание перечисления с именованными константами
```pycon
>>> from enum import Enum
>>>
>>> class Color(Enum):
...     RED = 1
...     GREEN = 2
...     BLUE = 3
...
>>> print(Color.RED)
Color.RED
>>> print(Color.RED.name)
RED
>>> print(Color.RED.value)
1
```

### IntEnum
Перечисление с целочисленными значениями
```pycon
>>> from enum import IntEnum
>>>
>>> class Status(IntEnum):
...     ACTIVE = 1
...     INACTIVE = 0
...
>>> print(Status.ACTIVE == 1)
True
>>> print(Status.INACTIVE + 1)
1
```

### StrEnum _(Python 3.11+)_
Перечисление со строковыми значениями
```pycon
>>> from enum import StrEnum
>>>
>>> class Role(StrEnum):
...     ADMIN = "admin"
...     USER = "user"
...
>>> print(Role.ADMIN.value, Role.ADMIN.value == "admin")
admin True
>>> print(Role.USER, Role.USER == "user")
user True
```

### Flag
Битовые флаги
```pycon
>>> from enum import Flag, auto
>>>
>>> class Permission(Flag):
...     READ = auto()
...     WRITE = auto()
...     EXECUTE = auto()
...
>>> combined = Permission.READ | Permission.WRITE
>>> print(combined)
Permission.READ|WRITE
>>> print(combined & Permission.READ)
Permission.READ
```

### IntFlag
Битовые флаги с целыми числами
```pycon
>>> from enum import IntFlag
>>>
>>> class Options(IntFlag):
...     OPTION1 = 1
...     OPTION2 = 2
...     OPTION3 = 4
...
>>> combo = Options.OPTION1 | Options.OPTION3
>>> print(combo, combo == Options.OPTION1 | Options.OPTION3)
5 True
```

### auto()
Автоматическая генерация значений
```pycon
>>> from enum import Enum, auto
>>>
>>> class State(Enum):
...     START = auto()
...     STOP = auto()
...     PAUSE = auto()
...
>>> print(list(State))
[<State.START: 1>, <State.STOP: 2>, <State.PAUSE: 3>]
```

### unique()
`@unique` гарантирует отсутствие дубликатов значений
```python
>>> from enum import Enum, unique
>>>
>>> @unique
... class Shape(Enum):
...     CIRCLE = 1
...     SQUARE = 2
...
>>> @unique
... class Shape(Enum):
...     CIRCLE = 1
...     SQUARE = 1
...
ValueError: duplicate values found in <enum 'Shape'>: SQUARE -> CIRCLE
```

### .\_\_members\_\_
Работа с элементами перечисления
```pycon
>>> from enum import Enum
>>>
>>> class Fruits(Enum):
...     APPLE = 1
...     ORANGE = 2
...
>>> print(Fruits.__members__)
{'APPLE': <Fruits.APPLE: 1>, 'ORANGE': <Fruits.ORANGE: 2>}
```

### EnumMeta
Пример работы с метаклассом
```pycon
>>> from enum import Enum, EnumMeta
>>>
>>> class MyEnumMeta(EnumMeta):
...     def __contains__(cls, item):
...         return item in cls._value2member_map_
...
>>> class Colors(Enum, metaclass=MyEnumMeta):
...     RED = 1
...     BLUE = 2
...
>>> print(1 in Colors)
True
>>> print(3 in Colors)
False
```

### Пользовательские методы и свойства
Перечисления могут содержать методы и дополнительные свойства
```python
from enum import Enum

class Day(Enum):
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7

    def is_weekend(self):
        return self in (Day.SATURDAY, Day.SUNDAY)

print(Day.SATURDAY.is_weekend())  # True
```

### Перегрузка операторов
Можно перегружать операторы в перечислениях
```python
from enum import IntEnum

class Level(IntEnum):
    LOW = 1
    MEDIUM = 2
    HIGH = 3

    def __ge__(self, other):
        return self.value >= other.value

print(Level.HIGH >= Level.MEDIUM)  # True
```

### Ошибки при работе с Enum

- `ValueError` Возникает, если обратиться к несуществующему значению ```python
print(Color(10))     # ValueError: 10 is not a valid Color
```
- `AttributeError` Возникает при обращении к несуществующему члену перечисления ```python
print(Color.YELLOW)  # AttributeError: YELLOW
```

### Особенности использования

- **Перечисления неизменяемы**: Невозможно присваивать новые значения или изменять существующие
- **Перечисления можно использовать как ключи словарей**, так как они неизменяемы и хешируемы
