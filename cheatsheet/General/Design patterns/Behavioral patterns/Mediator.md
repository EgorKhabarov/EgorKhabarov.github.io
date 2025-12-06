## Mediator

Посредник

**Описание**: Определяет объект, инкапсулирующий взаимодействие между наборами объектов, чтобы предотвратить их прямую связь

**Когда использовать**: Когда нужно уменьшить связанность между объектами и централизовать управление их взаимодействием

```python
class Mediator:
    def notify(self, sender, event):
        pass

class ConcreteMediator(Mediator):
    def __init__(self, component1, component2):
        self._component1 = component1
        self._component2 = component2
        self._component1.mediator = self
        self._component2.mediator = self

    def notify(self, sender, event):
        if sender == self._component1 and event == "event1":
            return self._component2.do_action()
        elif sender == self._component2 and event == "event2":
            return self._component1.do_action()

class Component:
    def __init__(self):
        self.mediator = None

    def do_action(self):
        return "Action performed"

    def trigger(self, event):
        return self.mediator.notify(self, event)


component1 = Component()
component2 = Component()
mediator = ConcreteMediator(component1, component2)
print(component1.trigger("event1"))  # Action performed
print(component2.trigger("event2"))  # Action performed
```
