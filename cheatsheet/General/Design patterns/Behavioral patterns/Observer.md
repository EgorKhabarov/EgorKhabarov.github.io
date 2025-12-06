## Observer

Наблюдатель

**Описание**: Определяет зависимость один ко многим между объектами,
так что при изменении состояния одного объекта все зависимые объекты уведомляются и обновляются автоматически

**Когда использовать**: Когда изменение состояния одного объекта требует обновления других объектов,
и вы не хотите, чтобы объекты были жестко связаны

```python
class Observer:
    def update(self, message):
        pass

class ConcreteObserver(Observer):
    def update(self, message):
        print(f"Received message: {message}")

class Subject:
    def __init__(self):
        self._observers = []

    def add_observer(self, observer):
        self._observers.append(observer)

    def remove_observer(self, observer):
        self._observers.remove(observer)

    def notify_observers(self, message):
        for observer in self._observers:
            observer.update(message)


subject = Subject()
subject.add_observer(ConcreteObserver())
subject.add_observer(ConcreteObserver())
subject.notify_observers("Hello Observers!")
# Received message: Hello Observers!
# Received message: Hello Observers!
```
