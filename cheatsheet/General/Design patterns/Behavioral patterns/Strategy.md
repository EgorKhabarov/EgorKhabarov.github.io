# Strategy

Стратегия

**Описание**: Определяет семейство алгоритмов, инкапсулирует их и делает их взаимозаменяемыми

**Когда использовать**: Когда нужно выбрать один из нескольких алгоритмов на этапе выполнения программы

```python
class Strategy:
    def execute(self, a, b):
        pass

class AddStrategy(Strategy):
    def execute(self, a, b):
        return a + b

class MultiplyStrategy(Strategy):
    def execute(self, a, b):
        return a * b

class Context:
    def __init__(self, strategy):
        self.strategy = strategy

    def execute_strategy(self, a, b):
        return self.strategy.execute(a, b)


context = Context(AddStrategy())
print(context.execute_strategy(5, 3))  # 8

context = Context(MultiplyStrategy())
print(context.execute_strategy(5, 3))  # 15
```
