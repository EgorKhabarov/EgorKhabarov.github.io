# Abstract Factory (Абстрактная фабрика)

**Описание**: Предоставляет интерфейс для создания семейств связанных объектов без указания их конкретных классов.

**Когда использовать**: Когда нужно создавать семейства объектов, которые должны использоваться вместе.

```python
class AbstractProductA:
    def do_something(self):
        pass

class ConcreteProductA1(AbstractProductA):
    def do_something(self):
        return "Product A1"

class ConcreteProductA2(AbstractProductA):
    def do_something(self):
        return "Product A2"

class AbstractFactory:
    def create_product_a(self):
        pass

class ConcreteFactory1(AbstractFactory):
    def create_product_a(self):
        return ConcreteProductA1()

class ConcreteFactory2(AbstractFactory):
    def create_product_a(self):
        return ConcreteProductA2()

factory1 = ConcreteFactory1()
product_a1 = factory1.create_product_a()
print(product_a1.do_something())  # Product A1

factory2 = ConcreteFactory2()
product_a2 = factory2.create_product_a()
print(product_a2.do_something())  # Product A2
```
