# Основные функции и атрибуты

| Функция/Атрибут                   | Описание                                                                                                                                          |
|-----------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------|
| `accumulate()`                    | Возвращает итератор, который вычисляет частичные суммы<br>(или другие накопленные функции, если указана) от переданного итератора                 |
| `chain()`                         | Принимает несколько итераторов и возвращает один итератор,<br>объединяющий все их элементы последовательно                                        |
| `combinations()`                  | Возвращает все возможные комбинации заданной длины из элементов итератора (без повторений)                                                        |
| `combinations_with_replacement()` | Возвращает все возможные комбинации с повторениями заданной длины из элементов итератора                                                          |
| `compress()`                      | Возвращает элементы из первого итератора,<br>где соответствующий элемент из второго итератора (маски) истинный                                    |
| `count()`                         | Возвращает итератор, который генерирует последовательность чисел,<br>начиная с `start` (по умолчанию 0) с шагом `step` (по умолчанию 1)           |
| `cycle()`                         | Бесконечно повторяет элементы переданного итератора                                                                                               |
| `dropwhile()`                     | Возвращает элементы из итератора, начиная с первого элемента,<br>для которого условие становится ложным                                           |
| `filterfalse()`                   | Возвращает элементы итератора, для которых условие ложно (противоположно `filter`)                                                                |
| `groupby()`                       | Группирует элементы последовательности по ключу (или значению функции).<br>Возвращает итератор с парами `(ключ, группа)`                          |
| `islice()`                        | Возвращает срез итератора (аналогично `slice()` для списков)                                                                                      |
| `pairwise()`                      | Выдаёт пары соседних элементов из `iterable`                                                                                                      |
| `permutations()`                  | Возвращает все возможные перестановки заданной длины (или длины итератора)                                                                        |
| `product()`                       | Возвращает декартово произведение входных итераторов (все возможные комбинации)                                                                   |
| `repeat()`                        | Повторяет переданный элемент `object` бесконечно или заданное количество раз `times`                                                              |
| `starmap()`                       | Применяет функцию к каждому элементу итератора, передавая элементы<br>как аргументы по позициям (аналогично `map()`, но с распаковкой аргументов) |
| `takewhile()`                     | Возвращает элементы из итератора до тех пор, пока условие истинно                                                                                 |
| `tee()`                           | Разделяет итератор на заданное количество независимых копий                                                                                       |
| `zip_longest()`                   | Объединяет элементы из нескольких итераторов, заполняя отсутствующие значения `fillvalue`                                                         |


# accumulate
Возвращает итератор, который вычисляет частичные суммы (или другие накопленные функции)
```python
from itertools import accumulate

print(list(accumulate([1, 2, 3, 4])))
# [1, 3, 6, 10]
```

# chain
Объединяет несколько итераторов в один
```python
from itertools import chain

print(list(chain("ABC", "DEF")))
# ["A", "B", "C", "D", "E", "F"]
```

# combinations
Возвращает все возможные комбинации заданной длины без повторений
```python
from itertools import combinations

print(list(combinations("ABC", 2)))
# [("A", "B"), ("A", "C"), ("B", "C")]
```

# combinations_with_replacement
Возвращает все возможные комбинации заданной длины с повторениями
```python
from itertools import combinations_with_replacement

print(list(combinations_with_replacement("AB", 2)))
# [("A", "A"), ("A", "B"), ("B", "B")]
```

# compress
Возвращает элементы из первого итератора, где соответствующий элемент из второго итератора истинный
```python
from itertools import compress

print(list(compress("ABCDEF", [1, 0, 1, 0, 1, 0])))
# ["A", "C", "E"]
```

# count
Создает бесконечный итератор, который начинает с заданного числа и увеличивается на заданный шаг
```python
from itertools import count

for i in count(10, 2):
    if i > 20:
        break
    print(i)
# 10, 12, 14, 16, 18, 20
```

# cycle
Бесконечно повторяет элементы из итератора
```python
from itertools import cycle

counter = 0
for item in cycle("AB"):
    if counter >= 6:
        break
    print(item)  # A, B, A, B, A, B
    counter += 1
```

# dropwhile
Пропускает элементы, пока условие истинно, затем возвращает оставшиеся элементы
```python
from itertools import dropwhile

print(list(dropwhile(lambda x: x < 5, [1, 4, 6, 7])))
# [6, 7]
```

# filterfalse
Возвращает элементы итератора, для которых условие ложно
```python
from itertools import filterfalse

print(list(filterfalse(lambda x: x % 2, range(10))))
# [0, 2, 4, 6, 8]
```

# groupby
Группирует элементы по ключу
Возвращает итератор с парами `(ключ, группа)`
```python
from itertools import groupby

for key, group in groupby("AAAABBBCCDA"):
    print(key, list(group))
# A ["A", "A", "A", "A"]
# B ["B", "B", "B"]
# C ["C", "C"]
# D ["D"]
# A ["A"]
```

# islice
Возвращает срез итератора
```python
from itertools import islice

print(list(islice(range(10), 2, 8, 2)))  # [2, 4, 6]
```

# pairwise
```python
from itertools import pairwise

print(list(pairwise("ABcd12")))
# [("A", "B"), ("B", "c"), ("c", "d"), ("d", "1"), ("1", "2")]
```

# permutations
Возвращает все возможные перестановки заданной длины
```python
from itertools import permutations

print(list(permutations("ABC", 2)))
# [("A", "B"), ("A", "C"), ("B", "A"), ("B", "C"), ("C", "A"), ("C", "B")]
```

# product
Возвращает декартово произведение входных итераторов
```python
from itertools import product

print(list(product("AB", "12")))
# [("A", "1"), ("A", "2"), ("B", "1"), ("B", "2")]
```

# repeat
Повторяет указанный элемент бесконечно или заданное количество раз
```python
from itertools import repeat

for i in repeat(10, 3):
    print(i)
# 10, 10, 10
```

# starmap
Применяет функцию к каждому элементу итератора, распаковывая элементы как аргументы
```python
from itertools import starmap

print(list(starmap(pow, [(2, 5), (3, 2), (10, 3)])))  # [32, 9, 1000]
```

# takewhile
Возвращает элементы из итератора до тех пор, пока условие истинно
```python
from itertools import takewhile

print(list(takewhile(lambda x: x < 5, [1, 4, 6, 7])))  # [1, 4]
```

# tee
Создает несколько независимых копий одного итератора
```python
from itertools import tee

it1, it2 = tee(range(5), 2)
print(list(it1))  # [0, 1, 2, 3, 4]
print(list(it2))  # [0, 1, 2, 3, 4]
```

# zip_longest
Объединяет элементы из нескольких итераторов, заполняя отсутствующие значения `fillvalue`
```python
from itertools import zip_longest

print(list(zip_longest("AB", "12", fillvalue="-")))
# [("A", "1"), ("B", "2")]
```
