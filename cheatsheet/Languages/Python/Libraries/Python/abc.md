`abc` предоставляет инструменты для работы с абстрактными базовыми классами (ABC)
Эти классы используются для определения интерфейсов, которые должны реализовывать дочерние классы


### Основные компоненты

- **`ABC`** абстрактный базовый класс
- **`abstractmethod`** декоратор для определения абстрактных методов,
которые должны быть реализованы в дочерних классах


```python
from abc import ABC, abstractmethod


class MyAbstractClass(ABC):
    @abstractmethod
    def my_method(self):
        pass

    # Пример абстрактного свойства
    @property
    @abstractmethod
    def my_property(self):
        pass


class ConcreteClass(MyAbstractClass):
    def my_method(self):
        return "Method implemented"

    @property
    def my_property(self):
        return "Property value"


# Попытка создать экземпляр абстрактного класса напрямую вызовет ошибку
# my_abstract_instance = MyAbstractClass()  # Это вызовет TypeError

# Создание экземпляра класса, который реализует все абстрактные методы
concrete_instance = ConcreteClass()
print(concrete_instance.my_method())  # Method implemented
print(concrete_instance.my_property)  # Property value
```

> [!IMPORTANT]
> Абстрактный метод в `ABC` не имеет реализации и должен быть переопределён в дочернем классе.
