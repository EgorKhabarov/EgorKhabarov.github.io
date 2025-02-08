# @property
Используется для определения методов, доступных как поля
Таким образом операции чтения/записи поля можно обрамить дополнительной логикой,
например, проверкой допустимых значений входного аргумента или пересчетом внутренних переменных объекта
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
