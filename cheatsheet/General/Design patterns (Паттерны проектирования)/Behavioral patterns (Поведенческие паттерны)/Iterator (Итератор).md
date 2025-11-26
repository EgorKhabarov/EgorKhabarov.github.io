# Iterator (Итератор)

**Описание**: Предоставляет способ последовательного доступа ко всем элементам коллекции без раскрытия её внутреннего представления

**Когда использовать**: Когда нужно последовательно обойти элементы коллекции без раскрытия её внутренней структуры

```python
class Iterator:
    def __init__(self, collection):
        self._collection = collection
        self._index = 0

    def has_next(self):
        return self._index < len(self._collection)

    def next(self):
        if self.has_next():
            value = self._collection[self._index]
            self._index += 1
            return value
        raise StopIteration


collection = [1, 2, 3]
iterator = Iterator(collection)

while iterator.has_next():
    print(iterator.next())  # 1 2 3
```
