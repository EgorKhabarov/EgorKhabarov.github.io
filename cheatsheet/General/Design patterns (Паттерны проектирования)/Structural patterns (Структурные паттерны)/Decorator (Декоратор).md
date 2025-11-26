## Decorator (Декоратор)

**Описание:** Позволяет динамически добавлять новое поведение объектам, оборачивая их в класс-оболочку

**Когда использовать:** Когда нужно добавлять дополнительные функциональности объектам без изменения их класса

```python
class Component:
    def operation(self):
        pass


class ConcreteComponent(Component):
    def operation(self):
        return "ConcreteComponent"


class Decorator(Component):
    def __init__(self, component):
        self._component = component

    def operation(self):
        return f"Decorator({self._component.operation()})"


component = ConcreteComponent()
decorated = Decorator(component)
print(decorated.operation())  # "Decorator(ConcreteComponent)"
```
