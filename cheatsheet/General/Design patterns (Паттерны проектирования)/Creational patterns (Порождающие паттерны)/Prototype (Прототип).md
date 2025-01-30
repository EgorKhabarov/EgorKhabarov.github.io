# Prototype (Прототип)

**Описание**: Позволяет создавать новые объекты путем копирования существующих экземпляров (прототипов).

**Когда использовать**: Когда создание объектов дорогое или сложное, а также когда нужно избежать повторного выполнения инициализационного кода.

```python
import copy


class Prototype:
    def __init__(self, value):
        self.value = value

    def clone(self):
        return copy.deepcopy(self)


prototype = Prototype(42)
clone = prototype.clone()
print(clone.value)  # 42
```
