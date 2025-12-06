## Chain of Responsibility

Цепочка обязанностей

**Описание**: Позволяет передавать запрос по цепочке обработчиков, где каждый обработчик решает, обработать запрос или передать следующему

**Когда использовать**: Когда нужно передавать запрос последовательно через ряд обработчиков, не определяя явно, какой обработчик его обработает

```python
class Handler:
    def __init__(self, successor=None):
        self._successor = successor

    def handle(self, request):
        if self._successor:
            return self._successor.handle(request)
        return None

class ConcreteHandlerA(Handler):
    def handle(self, request):
        if request == "A":
            return "Handled by A"
        return super().handle(request)

class ConcreteHandlerB(Handler):
    def handle(self, request):
        if request == "B":
            return "Handled by B"
        return super().handle(request)


handler = ConcreteHandlerA(ConcreteHandlerB())
print(handler.handle("A"))  # Handled by A
print(handler.handle("B"))  # Handled by B
print(handler.handle("C"))  # None
```
