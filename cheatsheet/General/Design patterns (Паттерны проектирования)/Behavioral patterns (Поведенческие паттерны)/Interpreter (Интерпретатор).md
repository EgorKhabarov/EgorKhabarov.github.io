# Interpreter (Интерпретатор)

**Описание**: Определяет грамматику языка и интерпретирует предложения в этом языке.

**Когда использовать**: Когда нужно анализировать и исполнять предложения в специфическом языке или грамматике.

```python
class Expression:
    def interpret(self, context):
        pass

class Number(Expression):
    def __init__(self, value):
        self.value = value

    def interpret(self, context):
        return self.value

class Add(Expression):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def interpret(self, context):
        return self.left.interpret(context) + self.right.interpret(context)


context = {}
expr = Add(Number(3), Number(4))
print(expr.interpret(context))  # 7
```
