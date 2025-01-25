```python
from functools import cached_property


class Circle:
    def __init__(self, radius):
        self.radius = radius

    @cached_property
    def area(self):
        return 3.14 * self.radius ** 2


circle = Circle(10)
print(circle.area)
# Напечатает 314.0
print(circle.area)
# Вернет кешированное значение 314.0 без вычислений
```
