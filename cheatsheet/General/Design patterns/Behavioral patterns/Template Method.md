## Template Method

Шаблонный метод

**Описание**: Определяет скелет алгоритма, позволяя подклассам переопределять некоторые шаги, не изменяя структуру алгоритма

**Когда использовать**: Когда нужно задать общий алгоритм, но позволить подклассам изменять отдельные шаги

```python
class AbstractClass:
    def template_method(self):
        self.step_one()
        self.step_two()

    def step_one(self):
        pass

    def step_two(self):
        pass

class ConcreteClass(AbstractClass):
    def step_one(self):
        print("Step One Implemented")

    def step_two(self):
        print("Step Two Implemented")


obj = ConcreteClass()
obj.template_method()
# Step One Implemented
# Step Two Implemented
```
