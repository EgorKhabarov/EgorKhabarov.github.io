from fractions import Fraction

Модуль fractions предоставляет класс Fraction, который позволяет работать с дробными числами в виде объектов.
Класс Fraction позволяет представлять дробное число в виде числителя и знаменателя.
Он автоматически упрощает дробь, позволяет выполнять арифметические операции с дробями
и конвертировать дроби в различные форматы (например, вещественные числа или строки).

Вот примеры использования класса Fraction:

```python
from fractions import Fraction

# создание дроби с помощью числителя и знаменателя
print(Fraction(3, 4))    # 3/4

# создание дроби из вещественного числа
print(Fraction(0.5))    # 1/2

# арифметические операции с дробями
print(Fraction(1, 4) + Fraction(1, 2))    # 3/4

# конвертирование дроби в вещественное число
print(float(Fraction(3, 4)))    # 0.75

# конвертирование дроби в строку
print(str(Fraction(3, 4)))    # "3/4"
```

Класс Fraction может быть полезен в тех случаях, когда требуется более точный
и удобный способ работы с дробными числами, чем встроенные типы данных.
Он может использоваться, например, при работе с финансовыми расчетами,
при расчете вероятностей или в других задачах, связанных с математикой.





Fraction
Класс для представления рациональных чисел.
Этот класс позволяет создавать объекты, которые представляют дроби в виде числителя и знаменателя.
Например, Fraction(3, 4) создаст дробь 3/4.

```python
from fractions import Fraction

print(Fraction(3, 4) + Fraction(1, 2))  # 5/4
```

gcd

Функция для вычисления наибольшего общего делителя двух чисел.

```python
from fractions import gcd

print(gcd(6, 9))  # 3
```

lcm
Функция для вычисления наименьшего общего кратного двух чисел.

```python
from fractions import lcm

print(lcm(6, 9))  # 18
```

limit_denominator
Метод объекта Fraction, который позволяет получить рациональное число,
ближайшее к данному, с знаменателем не превосходящим указанное значение.

```python
from fractions import Fraction

print(Fraction(7, 12).limit_denominator(5))  # 3/5
```

Fraction.from_float
Метод класса Fraction, который позволяет создать рациональное число,
представляющее указанное число с плавающей точкой.

```python
from fractions import Fraction

print(Fraction.from_float(0.5))  # 1/2
```

Fraction.from_decimal
Метод класса Fraction, который позволяет создать рациональное число, представляющее указанное десятичное число.

```python
from fractions import Fraction

print(Fraction.from_decimal("0.75"))  # 3/4
```

is_integer
Метод объекта Fraction, который возвращает True, если данная дробь представляет целое число, и False в противном случае.

```python
from fractions import Fraction

print(Fraction(3, 2).is_integer())  # False
print(Fraction(6, 4).is_integer())  # True
```

Fraction.as_integer_ratio
Метод объекта Fraction, который возвращает кортеж из двух целых чисел,
представляющих данную дробь в виде несократимой простой дроби.

```python
from fractions import Fraction

print(Fraction(5, 15).as_integer_ratio())  # (1, 3)
```

Fraction.from_ratio
Метод класса Fraction, который позволяет создать рациональное число на основе заданного отношения двух целых чисел.

```python
from fractions import Fraction

print(Fraction.from_ratio(5, 15))  # 1/3
```

Fraction.limit_denominator(max_denominator=1000000):
Метод объекта Fraction, который возвращает рациональное число, ближайшее к данному,
с знаменателем не превосходящим указанное значение.
Если аргумент max_denominator не указан, то по умолчанию он равен 1 миллиону.

```python
from fractions import Fraction

print(Fraction(3, 4).limit_denominator(10))  # 1/1
```

Fraction.from_jedec
Метод класса Fraction, который позволяет создать рациональное число на основе заданной строки в формате JEDEC.

```python
from fractions import Fraction

print(Fraction.from_jedec("1/2"))  # 1/2
```

Fraction.from_tuple
Метод класса Fraction, который позволяет создать рациональное число на основе заданного кортежа из двух целых чисел (числителя и знаменателя).

```python
from fractions import Fraction

print(Fraction.from_tuple((3, 4)))  # 3/4
```
