| Класс/Функция             | Описание                                                                                        |
|---------------------------|-------------------------------------------------------------------------------------------------|
| `Cache`                   | Базовый класс для всех кэшей. Не используется напрямую, а служит основой для других типов кэшей |
| `FIFOCache(maxsize)`      | Кэш с алгоритмом замещения **FIFO** (First In, First Out)                                       |
| `LFUCache(maxsize)`       | Кэш с алгоритмом замещения **LFU** (Least Frequently Used)                                      |
| `LRUCache(maxsize)`       | Кэш с алгоритмом замещения **LRU** (Least Recently Used)                                        |
| `MRUCache(maxsize)`       | Кэш с алгоритмом замещения **MRU** (Most Recently Used)                                         |
| `RRCache(maxsize)`        | Кэш с случайным замещением (Random Replacement)                                                 |
| `TLRUCache(maxsize, ttl)` | Кэш с временным ограничением и алгоритмом замещения **LRU** (Time-aware Least Recently Used)    |
| `TTLCache(maxsize, ttl)`  | Кэш с временным ограничением (**Time-to-Live**) и алгоритмом замещения **LRU**                  |
| `cached(cache)`           | Декоратор для кэширования возвращаемого значения функции                                        |
| `cachedmethod(cache)`     | Декоратор для кэширования возвращаемого значения метода класса                                  |

# Cache
Базовый класс для всех кэшей.
Он не используется напрямую, но служит основой для других классов,
предоставляя основные методы для работы с кэшем.

# FIFOCache
Использует алгоритм **FIFO** (First In, First Out).
Когда кэш заполняется, самый старый элемент удаляется, чтобы освободить место для нового.
```python
from cachetools import FIFOCache

cache = FIFOCache(maxsize=3)
cache["a"] = 1
cache["b"] = 2
cache["c"] = 3

print(cache)  # FIFOCache([("a", 1), ("b", 2), ("c", 3)])

cache["d"] = 4
print(cache)  # FIFOCache([("b", 2), ("c", 3), ("d", 4)])
```

# LFUCache
Использует алгоритм **LFU** (Least Frequently Used).
Наименее часто используемые элементы удаляются первыми при необходимости освобождения места.
```python
from cachetools import LFUCache

cache = LFUCache(maxsize=2)
cache["a"] = 1
cache["b"] = 2

cache["a"]  # Доступ к элементу увеличивает счетчик использования
cache["c"] = 3  # Удаляет "b", так как он использовался реже

print(cache)  # LFUCache([("a", 1), ("c", 3)])
```

# LRUCache
Использует алгоритм **LRU** (Least Recently Used).
Наименее недавно используемые элементы удаляются первыми.
```python
from cachetools import LRUCache

cache = LRUCache(maxsize=2)
cache["a"] = 1
cache["b"] = 2

cache["a"]  # Доступ к элементу делает его "самым недавно использованным"
cache["c"] = 3  # Удаляет "b", так как он был использован давнее всего

print(cache)  # LRUCache([("a", 1), ("c", 3)])
```

# MRUCache
Использует алгоритм **MRU** (Most Recently Used).
Самый недавно использованный элемент удаляется первым при необходимости освобождения места.
```python
from cachetools import MRUCache

cache = MRUCache(maxsize=2)
cache["a"] = 1
cache["b"] = 2

cache["a"]  # Доступ к элементу делает его "самым недавно использованным"
cache["c"] = 3  # Удаляет "a", так как он был использован последним

print(cache)  # MRUCache([("b", 2), ("c", 3)])
```

# RRCache
Использует случайное замещение (Random Replacement).
Элементы удаляются случайным образом, когда кэш заполняется.
```python
from cachetools import RRCache

cache = RRCache(maxsize=2)
cache["a"] = 1
cache["b"] = 2
cache["c"] = 3

print(cache)  # Один из элементов ("a" или "b") будет удален случайным образом
```

# TLRUCache
Сочетает в себе временное ограничение (`ttl`) и алгоритм **LRU**.
Элементы удаляются либо при истечении времени жизни, либо по принципу **LRU**.
```python
from cachetools import TLRUCache
import time

cache = TLRUCache(maxsize=2, ttl=5)
cache["a"] = 1
time.sleep(6)  # Ждем 6 секунд
cache["b"] = 2

print(cache)  # "a" будет удален, так как его TTL истек
```

# TTLCache
Кэш с временным ограничением (Time-to-Live) и алгоритмом **LRU**.
Элементы удаляются либо по истечению времени жизни (`ttl`), либо по принципу **LRU**, если кэш переполнен.
```python
from cachetools import TTLCache
import time

cache = TTLCache(maxsize=2, ttl=5)
cache["a"] = 1
time.sleep(6)  # Ждем 6 секунд
cache["b"] = 2

print(cache)  # "a" будет удален, так как его TTL истек
```

# cached
Декоратор, который используется для кэширования возвращаемого значения функции.
Он может использовать любой из предоставленных кэшей.
```python
from cachetools import cached, LRUCache

cache = LRUCache(maxsize=2)

@cached(cache)
def get_value(x):
    return x * 2

print(get_value(2))  # Вычисляет и кэширует результат
print(get_value(2))  # Возвращает кэшированный результат
```

# cachedmethod
Декоратор для кэширования возвращаемого значения метода класса.
Декоратор позволяет задать кэш на уровне экземпляра класса.
```python
from cachetools import cachedmethod, LRUCache

class MyClass:
    def __init__(self):
        self._cache = LRUCache(maxsize=2)

    @cachedmethod(cache=lambda self: self._cache)
    def get_value(self, x):
        return x * 2

obj = MyClass()
print(obj.get_value(2))  # Вычисляет и кэширует результат
print(obj.get_value(2))  # Возвращает кэшированный результат
```
