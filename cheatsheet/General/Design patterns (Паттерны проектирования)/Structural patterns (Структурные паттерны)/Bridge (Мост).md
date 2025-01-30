# Bridge (Мост)

**Описание**: Разделяет абстракцию и реализацию, позволяя изменять их независимо друг от друга.

**Когда использовать**: Когда нужно разделить абстракцию и реализацию для независимой модификации и избежать жесткой связанности.

```python
class Implementation:
    def operation(self):
        pass

class ConcreteImplementationA(Implementation):
    def operation(self):
        return "Implementation A"

class ConcreteImplementationB(Implementation):
    def operation(self):
        return "Implementation B"

class Abstraction:
    def __init__(self, implementation):
        self._implementation = implementation

    def execute(self):
        return self._implementation.operation()

abstraction_a = Abstraction(ConcreteImplementationA())
abstraction_b = Abstraction(ConcreteImplementationB())

print(abstraction_a.execute())  # Implementation A
print(abstraction_b.execute())  # Implementation B
```
