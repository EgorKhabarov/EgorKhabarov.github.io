# @property

Используется для определения методов, доступных как поля
Таким образом операции чтения/записи поля можно обрамить дополнительной логикой, например, проверкой допустимых значений входного аргумента или пересчетом внутренних переменных объекта

### Student
```python
class Student:
    def __init__(self):
        self._score = 0

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, s):
        if 0 <= s <= 100:
            self._score = s
        else:
            raise ValueError

user1 = Student()
print(user1.score)  # 0
user1.score = 1
print(user1.score)  # 1
user1._score = 999
print(user1.score)  # 999
user1.score = 999
print(user1.score)  # ValueError
```

### Rectangle
Создание свойства для доступа к атрибуту, добавление логики при его изменении, защита от удаления и предоставление только для чтения
```python
class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if value <= 0:
            raise ValueError("Width must be positive")
        self._width = value

    @width.deleter
    def width(self):
        raise AttributeError("Width cannot be deleted")

    @property
    def height(self):
        return self._height

    @property
    def area(self):
        return self._width * self._height


rect = Rectangle(5, 10)
print(f"Width: {rect.width}, Height: {rect.height}, Area: {rect.area}")
# Width: 5, Height: 10, Area: 50
rect.width = 7
print(f"Width: {rect.width}, Height: {rect.height}, Area: {rect.area}")
# Width: 7, Height: 10, Area: 70

try:
    rect.width = -3
except ValueError as e:
    print(e)  # Width must be positive

try:
    del rect.width
except AttributeError as e:
    print(e)  # Width cannot be deleted

try:
    rect.height = 15  # AttributeError: can't set attribute
except AttributeError as e:
    print(e)  # property 'height' of 'Rectangle' object has no setter
```

---

# Python example

```python
class MyProperty:
    def __init__(self, fget=None, fset=None, fdel=None, doc=None):
        self.fget = fget
        self.fset = fset
        self.fdel = fdel
        self.__doc__ = doc

    def __get__(self, instance, owner):
        if instance is None:
            return self  # Позволяет доступ к дескриптору через класс
        if self.fget is None:
            raise AttributeError("unreadable attribute")
        return self.fget(instance)

    def __set__(self, instance, value):
        if self.fset is None:
            raise AttributeError("can't set attribute")
        self.fset(instance, value)

    def __delete__(self, instance):
        if self.fdel is None:
            raise AttributeError("can't delete attribute")
        self.fdel(instance)

    def getter(self, fget):
        """
        Создает новую копию дескриптора с новым геттером
        """
        return type(self)(fget, self.fset, self.fdel, self.__doc__)

    def setter(self, fset):
        """
        Создает новую копию дескриптора с новым сеттером
        """
        return type(self)(self.fget, fset, self.fdel, self.__doc__)

    def deleter(self, fdel):
        """
        Создает новую копию дескриптора с новым дилитером
        """
        return type(self)(self.fget, self.fset, fdel, self.__doc__)


class MyClass:
    def __init__(self, value):
        self._value = value

    @MyProperty
    def value(self):
        """
        Это значение
        """
        return self._value

    @value.setter
    def value(self, new_value):
        if new_value < 0:
            raise ValueError("value must be >= 0")
        self._value = new_value

    @value.deleter
    def value(self):
        print("Удаление значения")
        del self._value


obj = MyClass(42)
print(obj.value)  # 42

obj.value = 10
print(obj.value)  # 10

del obj.value  # Удаление значения
```
