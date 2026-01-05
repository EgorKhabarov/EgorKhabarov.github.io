# itertools

## Infinite iterators

Потенциально бесконечные итераторы
Всегда требуют явного ограничения

### count

Возвращает итератор, который генерирует последовательность чисел,
начиная с `start` (по умолчанию 0) с шагом `step` (по умолчанию 1)

```python
from itertools import count

for i in count(10, 2):
    if i > 20:
        break
    print(i)
"""
10
12
14
16
18
20
"""
```

### cycle

Бесконечно повторяет элементы переданного итератора

```python
from itertools import cycle

counter = 0
for item in cycle("AB"):
    if counter == 6:
        break
    print(item)
    counter += 1
"""
A
B
A
B
A
B
"""
```

### repeat

Повторяет переданный элемент `object` бесконечно или заданное количество раз `times`

```python
from itertools import repeat

list(repeat(10, 3))
# [10, 10, 10]
```

## Iterators terminating on the shortest input sequence

Итераторы, которые завершаются при исчерпании входных данных

### accumulate

Возвращает итератор, который вычисляет частичные суммы
(или другие накопленные функции, если указана) от переданного итератора

```python
from itertools import accumulate

list(accumulate([1, 2, 3, 4]))
# [1, 3, 6, 10]
```

### batched

Разбивает iterable на последовательные блоки фиксированного размера
Последний блок может быть короче

**Python 3.12+**

```python
from itertools import batched

list(batched("ABCDEFG", 3))
# [("A", "B", "C"), ("D", "E", "F"), ("G",)]
```

### chain

Принимает несколько итераторов и возвращает один итератор,
объединяющий все их элементы последовательно

```python
from itertools import chain

list(chain("ABC", "DEF"))
# ["A", "B", "C", "D", "E", "F"]
```

### compress

Возвращает элементы из первого итератора,
где соответствующий элемент из второго итератора (маски) истинный

```python
from itertools import compress

list(compress("ABCDEF", [1, 0, 1, 0, 1, 0]))
# ["A", "C", "E"]
```

### dropwhile

Возвращает элементы из итератора, начиная с первого элемента,
для которого условие становится ложным

```python
from itertools import dropwhile

list(dropwhile(lambda x: x < 5, [1, 4, 6, 7]))
# [6, 7]
```

### takewhile

Возвращает элементы из итератора до тех пор, пока условие истинно

```python
from itertools import takewhile

list(takewhile(lambda x: x < 5, [1, 4, 6, 7]))
# [1, 4]
```

### filterfalse

Возвращает элементы итератора, для которых условие ложно (противоположно `filter`)

```python
from itertools import filterfalse

list(filterfalse(lambda x: x % 2, range(10)))
# [0, 2, 4, 6, 8]
```

### groupby

Группирует элементы последовательности по ключу (или значению функции)
Возвращает итератор с парами `(ключ, группа)`

Работает только с подряд идущими элементами
Часто требуется предварительная сортировка

```python
from itertools import groupby

for key, group in groupby("AAAABBBCCDA"):
    print(key, list(group))
"""
A ["A", "A", "A", "A"]
B ["B", "B", "B"]
C ["C", "C"]
D ["D"]
A ["A"]
"""
```

### islice

Возвращает срез итератора (аналогично `slice()` для списков)

```python
from itertools import islice

list(islice(range(10), 2, 8, 2))
# [2, 4, 6]
```

### pairwise

Выдаёт пары соседних элементов из `iterable`

```python
from itertools import pairwise

list(pairwise("ABcd12"))
# [("A", "B"), ("B", "c"), ("c", "d"), ("d", "1"), ("1", "2")]
```

### starmap

Применяет функцию к каждому элементу итератора, передавая элементы
как аргументы по позициям (аналогично `map()`, но с распаковкой аргументов)

```python
from itertools import starmap

list(starmap(pow, [(2, 5), (3, 2), (10, 3)]))
# [32, 9, 1000]
```

### tee

Разделяет итератор на заданное количество независимых копий

Важно
tee буферизует данные в памяти при неравномерном потреблении итераторов

```python
from itertools import tee

it1, it2 = tee(range(5), 2)
list(it1)
list(it2)
# [0, 1, 2, 3, 4]
# [0, 1, 2, 3, 4]
```

### zip_longest

Объединяет элементы из нескольких итераторов, заполняя отсутствующие значения `fillvalue`

```python
from itertools import zip_longest

list(zip_longest("AB", "12", fillvalue="-"))
# [("A", "1"), ("B", "2")]
```

## Combinatoric generators

Генераторы для комбинаторных последовательностей

### product

Возвращает декартово произведение входных итераторов (все возможные комбинации)

```python
from itertools import product

list(product("AB", "12"))
# [("A", "1"), ("A", "2"), ("B", "1"), ("B", "2")]
```

### permutations

Возвращает все возможные перестановки заданной длины (или длины итератора)

```python
from itertools import permutations

list(permutations("ABC", 2))
# [("A", "B"), ("A", "C"), ("B", "A"), ("B", "C"), ("C", "A"), ("C", "B")]
```

### combinations

Возвращает все возможные комбинации заданной длины из элементов итератора (без повторений)

```python
from itertools import combinations

list(combinations("ABC", 2))
# [("A", "B"), ("A", "C"), ("B", "C")]
```

### combinations_with_replacement

Возвращает все возможные комбинации с повторениями заданной длины из элементов итератора

```python
from itertools import combinations_with_replacement

list(combinations_with_replacement("AB", 2))
# [("A", "A"), ("A", "B"), ("B", "B")]
```
