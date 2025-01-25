from decimal import Decimal

Библиотека decimal предоставляет более точный способ работы с десятичными числами, чем встроенные типы данных float и double.
Она позволяет представлять числа с фиксированной точностью и позволяет управлять точностью вычислений.
Это может быть полезно в тех случаях, когда требуется точный результат, например, при финансовых расчетах.

Класс Decimal
Класс Decimal используется для создания и работы с десятичными числами с фиксированной точностью. Вот несколько примеров:i

```python
from decimal import Decimal

# Создание десятичного числа
a = Decimal("10.5")

# Арифметические операции
b = Decimal("2")
a + b  # 12.5
a - b  # 8.5
a * b  # 21.0
a / b  # 5.25

# Округление
a.quantize(Decimal("1.00"))  # 10.50
a.quantize(Decimal("0.1"))   # 10.5

# Преобразование в разные форматы
a.to_eng_string()     # "10.5"
a.as_integer_ratio()  # (21, 2)
```

Класс Context
Класс Context представляет контекст округления, который управляет поведением операций с десятичными числами. Вот несколько примеров:

```python
from decimal import Decimal, Context

# Создание контекста округления
ctx = Context(prec=3, rounding=ROUND_HALF_UP)

# Создание десятичного числа с использованием контекста
a = Decimal("10.5", context=ctx)

# Арифметические операции с использованием контекста
b = Decimal("2", context=ctx)
c = a + b
d = a - b
e = a * b
f = a / b

# Округление с использованием контекста
g = a.quantize(Decimal("1.00"), context=ctx)
h = a.quantize(Decimal("0.1"), context=ctx)
```

Функции округления
Модуль decimal также предоставляет несколько функций округления, которые можно использовать с десятичными числами. Вот несколько примеров:

```python
from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_DOWN, ROUND_CEILING, ROUND_FLOOR

a = Decimal("10.555")

# Округление до двух знаков с округлением до ближайшего
a.quantize(Decimal("1.00"), rounding=ROUND_HALF_UP)  # 10.56

# Округление до двух знаков с округлением в меньшую сторону
a.quantize(Decimal("1.00"), rounding=ROUND_FLOOR)  # 10.55

# Округление до целого числа, округление до ближайшего
a.quantize(Decimal("1"), rounding=ROUND_HALF_UP)  # 11

# Округление до целого числа, округление в большую сторону
a.quantize(Decimal("1"), rounding=ROUND_CEILING)  # 11
```
