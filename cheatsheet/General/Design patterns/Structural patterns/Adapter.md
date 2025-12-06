## Adapter

Адаптер

**Описание**: Позволяет объектам с несовместимыми интерфейсами работать вместе, преобразуя интерфейс одного объекта в интерфейс, ожидаемый другим

**Когда использовать**: Когда нужно использовать существующий класс с несовместимым интерфейсом

```python
class Adaptee:
    def specific_request(self):
        return "Adaptee behavior"

class Adapter:
    def __init__(self, adaptee):
        self._adaptee = adaptee

    def request(self):
        return self._adaptee.specific_request()

adaptee = Adaptee()
adapter = Adapter(adaptee)
print(adapter.request())  # Adaptee behavior
```
