# heapq

`heapq` реализует **очередь с приоритетом** на базе **мин-кучи**

Модуль `heapq` предоставляет алгоритмы для работы с **мин-кучей** - бинарной кучи, где на вершине находится наименьший элемент
Все функции работают **in-place** с обычным списком (`list`), который должен быть **представлен как куча**

- Куча представляется списком
- Базируется на **мин-куче** (`heap[0]` - минимальный элемент)
- Работает **in-place**

| Название           | Назначение                               |
|--------------------|------------------------------------------|
| `heapify`          | Преобразует список в кучу (min-heap)     |
| `heappush`         | Добавляет элемент в кучу                 |
| `heappop`          | Удаляет и возвращает наименьший элемент  |
| `heappushpop`      | Вставляет и сразу удаляет наименьший     |
| `heapreplace`      | Удаляет и сразу вставляет новый элемент  |
| `merge`            | Итератор по отсортированным итерациям    |
| `nlargest`         | `N` наибольших элементов из итерируемого |
| `nsmallest`        | `N` наименьших элементов из итерируемого |
| `_heapify_max`     | Вспомогательная: делает max-кучу         |
| `_heappop_max`     | Вспомогательная: pop из max-кучи         |
| `_heapreplace_max` | Вспомогательная: replace в max-куче      |
| `_siftdown`        | Внутренняя: просеивание вниз (min-heap)  |
| `_siftup`          | Внутренняя: просеивание вверх (min-heap) |
| `_siftdown_max`    | Вспомогательная: sift вниз (max-heap)    |
| `_siftup_max`      | Вспомогательная: sift вверх (max-heap)   |

## Основные функции (min-heap)
### `heapify(iterable)`
Превращает список в кучу за `O(n)`
```python
import heapq

data = [3, 1, 4, 1, 5]
heapq.heapify(data)
print(data)  # [1, 1, 4, 3, 5]
```
### `heappush(heap, item)`
Добавляет элемент в кучу
```python
heapq.heappush(data, 2)
print(data)  # [1, 1, 2, 3, 5, 4]
```
### `heappop(heap)`
Удаляет и возвращает наименьший элемент
```python
min_item = heapq.heappop(data)
print(min_item)  # 1
```
### `heappushpop(heap, item)`
Добавляет элемент и возвращает наименьший
Быстрее, чем `heappush` + `heappop`
```python
result = heapq.heappushpop(data, 0)
print(result)  # 0
```
### `heapreplace(heap, item)`
Удаляет наименьший и добавляет новый
Быстрее, но не сохраняет item, если heap пуст
```python
result = heapq.heapreplace(data, 10)
print(result)  # 1 (удалён)
print(data)    # [1, 3, 4, 5, 10]
```
### `merge(*iterables, key=None, reverse=False)`
Возвращает итератор по отсортированному объединению отсортированных последовательностей
```python
a = [1, 3, 5]
b = [2, 4, 6]
for x in heapq.merge(a, b):
    print(x, end=' ')  # 1 2 3 4 5 6
```
### `nsmallest(n, iterable, key=None)`
N наименьших элементов (подходит, если n небольшое)
```python
heapq.nsmallest(2, [5, 3, 1, 7])  # [1, 3]
```
### `nlargest(n, iterable, key=None)`
N наибольших элементов
```python
heapq.nlargest(2, [5, 3, 1, 7])  # [7, 5]
```
## Дополнительные (max-heap)
> Работают так же, но делают **максимальную** кучу (неофициальные, начинаются с `_`)

| Функция              | Описание                            |
|----------------------|-------------------------------------|
| `_heapify_max()`     | Преобразует список в max-heap       |
| `_heappop_max()`     | Удаляет и возвращает наибольший     |
| `_heapreplace_max()` | Удаляет наибольший и добавляет item |

```python
from heapq import _heapify_max, _heappop_max

data = [1, 3, 5, 7]
_heapify_max(data)
print(data)          # [7, 3, 5, 1]
print(_heappop_max(data))  # 7
```
## Внутренние функции (используются внутри)

| Функция          | Назначение                           |
|------------------|--------------------------------------|
| `_siftdown`      | Проталкивает элемент вниз (min-heap) |
| `_siftup`        | Поднимает элемент вверх (min-heap)   |
| `_siftdown_max`  | Проталкивает вниз (max-heap)         |
| `_siftup_max`    | Поднимает вверх (max-heap)           |

Обычно не нужны при обычном использовании

## Таблица сравнений

| Операция             | Назначение                     | Время      |
|----------------------|--------------------------------|------------|
| `heapify`            | Из списка в кучу               | O(n)       |
| `heappush`           | Добавить элемент               | O(log n)   |
| `heappop`            | Удалить минимальный элемент    | O(log n)   |
| `heappushpop`        | Вставить и сразу удалить       | O(log n)   |
| `heapreplace`        | Удалить и сразу вставить       | O(log n)   |
| `nlargest/nsmallest` | Топ-n элементов                | O(n log k) |

## Пример использования кучи как очереди с приоритетом
```python
import heapq

class PriorityQueue:
    def __init__(self):
        self.heap = []
        self.counter = 0  # для поддержки FIFO при равных приоритетах

    def push(self, item, priority):
        heapq.heappush(self.heap, (priority, self.counter, item))
        self.counter += 1

    def pop(self):
        return heapq.heappop(self.heap)[-1]

pq = PriorityQueue()
pq.push("task1", 2)
pq.push("task2", 1)
pq.push("task3", 3)

print(pq.pop())  # task2
```

## Заметки

`heapq` работает только с **мин-кучей**
Для max-heap используйте `-x` или `_heapify_max`
Быстрая альтернатива `sorted(iterable)[:n]` - `nsmallest(n, iterable)`





<!--
Библиотека `heapq` в Python используется для работы с `heapq`, имплементации алгоритма `heap queue` (очереди с приоритетами)
Это набор функций для эффективной работы с `heap` (кучей) - структурой данных,
которая обеспечивает быстрый доступ к наименьшему (или наибольшему) элементу

|                           |                                                                |
|---------------------------|----------------------------------------------------------------|
| `heapify(iterable)`       | Перестраивает итерируемый объект в кучу                        |
| `heappush(heap, item)`    | Добавляет элемент в кучу                                       |
| `heappop(heap)`           | Извлекает и возвращает наименьший элемент из кучи              |
| `heappushpop(heap, item)` | Добавляет элемент в кучу и сразу возвращает наименьший элемент |
| `heapreplace(heap, item)` | Заменяет наименьший элемент и возвращает его                   |

|            |                                                                                    |
|------------|------------------------------------------------------------------------------------|
| `heappush` | Добавляет элемент в кучу `heapq.heappush(heap, item)`                              |
| `heappop`  | Извлекает и возвращает наименьший элемент из кучи `smallest = heapq.heappop(heap)` |

-->