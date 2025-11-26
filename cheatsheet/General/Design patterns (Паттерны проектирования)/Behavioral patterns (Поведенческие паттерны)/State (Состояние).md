# State (Состояние)

**Описание**: Позволяет объекту изменять своё поведение в зависимости от внутреннего состояния, меняя свой класс

**Когда использовать**: Когда объект может находиться в одном из нескольких состояний, и поведение объекта меняется в зависимости от его состояния

```python
class State:
    def handle(self, context):
        pass

class ConcreteStateA(State):
    def handle(self, context):
        context.state = ConcreteStateB()
        print("Transition to ConcreteStateB")

class ConcreteStateB(State):
    def handle(self, context):
        context.state = ConcreteStateA()
        print("Transition to ConcreteStateA")

class Context:
    def __init__(self, state):
        self.state = state

    def request(self):
        self.state.handle(self)


context = Context(ConcreteStateA())
context.request()  # Transition to ConcreteStateB
context.request()  # Transition to ConcreteStateA
```
