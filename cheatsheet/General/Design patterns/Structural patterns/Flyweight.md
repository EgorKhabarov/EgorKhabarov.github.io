## Flyweight

Легковес

**Описание**: Оптимизация использования памяти за счёт разделения общих данных между множеством объектов

**Когда использовать**: Когда нужно создать много мелких объектов, которые имеют общие части данных

```python
class Flyweight:
    def __init__(self, shared_state):
        self.shared_state = shared_state

class FlyweightFactory:
    def __init__(self):
        self._flyweights = {}

    def get_flyweight(self, shared_state):
        if shared_state not in self._flyweights:
            self._flyweights[shared_state] = Flyweight(shared_state)
        return self._flyweights[shared_state]

factory = FlyweightFactory()
flyweight1 = factory.get_flyweight("shared")
flyweight2 = factory.get_flyweight("shared")
print(flyweight1 is flyweight2)  # True
```
