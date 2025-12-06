# Memento

Снимок

**Описание**: Позволяет сохранять и восстанавливать внутреннее состояние объекта без раскрытия его реализации

**Когда использовать**: Когда нужно сохранить состояние объекта и при необходимости восстановить его позже, не нарушая инкапсуляции

```python
class Memento:
    def __init__(self, state):
        self._state = state

    def get_state(self):
        return self._state

class Originator:
    def __init__(self, state):
        self._state = state

    def set_state(self, state):
        self._state = state

    def create_memento(self):
        return Memento(self._state)

    def restore_memento(self, memento):
        self._state = memento.get_state()

class Caretaker:
    def __init__(self):
        self._mementos = []

    def add_memento(self, memento):
        self._mementos.append(memento)

    def get_memento(self, index):
        return self._mementos[index]


originator = Originator("State1")
caretaker = Caretaker()
caretaker.add_memento(originator.create_memento())
originator.set_state("State2")
print(originator._state)  # State2
originator.restore_memento(caretaker.get_memento(0))
print(originator._state)  # State1
```
