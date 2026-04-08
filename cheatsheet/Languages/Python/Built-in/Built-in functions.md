### abs
Получения абсолютного значения числа
```pycon
>>> abs(-42)
42
```

### aiter
### all
### anext
### any
### ascii

### bin
Получения двоичного представления числа

```pycon
>>> bin(42)
"0b101010"
```

### bool
### breakpoint

### bytearray
Изменяемый тип данных, представляющий собой массив байтов
Последовательность целых чисел в диапазоне `0 ≤ X < 256`

Параметр **source** можно использовать для начальной инициализации массива:
Если source является строкой, вы также должны указать кодировку encoding и опционально **errors**
Если source является целым числом, массив будет иметь размер **source** и инициализирован байтами со значением `0`
Если source является объектом, то он должен поддерживать интерфейс буфера
Для инициализации массива байт будет использован буфер, предназначенный для чтения
Если **source** является итерируемым объектом, его элементами должны быть целыми числами в диапазоне `0 ≤ X < 256`
Этими числами и будет инициализирован массив
Если **source** не передан, вернет пустой **bytearray**

```pycon
>>> bytearray("Привет, Python!", "UTF-8")
bytearray(b"\xd0\x9f\xd1\x80\xd0\xb8\xd0\xb2\xd0\xb5\xd1\x82, Python!")
>>> bytearray(5)
bytearray(b"\x00\x00\x00\x00\x00")
>>> bytearray([1, 2, 3])
bytearray(b"\x01\x02\x03")
```

### bytes
Неизменяемый тип данных, представляющий собой массив байтов

```pycon
>>> bytes([1, 2, 3, 4, 5])
b"\x01\x02\x03\x04\x05"
```

### callable
Является ли объект вызываемым (т.е. функцией или методом)

```pycon
>>> def my_func():
...     pass
...
>>> class MyClass:
...     def my_method(self):
...         pass
...
>>> callable(my_func)
True
>>> callable(MyClass().my_method)
True
>>> callable(42)
False
```

### chr
Получение символа Unicode по его коду

```pycon
>>> chr(97)
"a"
```

### classmethod
Создание метода класса. Этот метод может быть вызван без создания экземпляра класса

```pycon
>>> class MyClass:
...     my_class_attr = 42
...     @classmethod
...     def my_class_method(cls):
...         print(cls.my_class_attr)
... 
>>> MyClass.my_class_method()
42
```

### compile
Для компиляции строки с кодом Python в объект-код

```pycon
>>> exec(compile('print("Hello, world!")', "<string>", "exec"))
Hello, world!
```

### complex
Для создания комплексного числа

```pycon
>>> complex(1, 2)
(1+2j)
```

### copyright
### credits

### delattr
Удаление атрибута объекта

### dict

### dir
Получение списка всех атрибутов объекта

```pycon
>>> dir([1, 2, 3])
["__add__", "__class__", "__class_getitem__", ...]
```

### divmod
Получения частного и остатка от деления двух чисел

```pycon
>>> divmod(42, 5)
(8, 2)
```

### enumerate
### eval
### exec
### exit

### filter
Фильтрация элементов последовательности с помощью функции

```pycon
>>> list(filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5]))
[2, 4]
```

### float
### format

### frozenset
Неизменяемый тип данных, представляющий собой неупорядоченное множество уникальных элементов

```pycon
>>> frozenset([1, 2, 2, 3, 4])
frozenset({1, 2, 3, 4})
```

### getattr
Для получения значения атрибута объекта по его имени

```pycon
>>> class MyClass:
...     def __init__(self):
...         self.my_attr = 42
...
>>> getattr(MyClass(), "my_attr")
42
```

### globals
Для получения словаря с глобальными переменными в текущем модуле

```pycon
>>> my_var = 42
>>> globals()
{"__name__": "__main__", "__doc__": None, "__package__": None, "my_var": 42, ...}
```

### hasattr
Для проверки наличия атрибута (метода или свойства) у объекта

```pycon
>>> class MyClass:
...     def __init__(self):
...         self.my_attr = 42
...
>>> my_obj = MyClass()
>>> hasattr(my_obj, "my_attr")
True
>>> hasattr(my_obj, "non_existent_attr")
False
```

### hash
### help
### hex
### id
### input
### int
### isinstance
### issubclass

### iter
iter(callable, sentinel)
Создает итератор пока не встретится значение
```pycon
>>> from random import randint
>>> for x in iter(lambda: randint(1, 10), 5):
...     print(x)
... 
```
Остановится когда выпадет 5

### len
### license
### list
### locals
### map
### max

### memoryview
Доступ к буферу памяти объекта без копирования его данных

```pycon
>>> mv = memoryview(bytearray("ABC", "UTF-8"))
>>> mv[0]  # Доступ к нулевому индексу представления памяти
65
>>> bytes(mv[0:2])  # Создать байт из представления памяти
b"AB"
>>> list(mv[0:3])  # Создать список из представления памяти
[65, 66, 67]
>>> b = bytearray(b"hello")
>>> m = memoryview(b)
>>> m[0] = ord("H")
>>> b
bytearray(b'Hello')
```

### min
### next

### object
Базовый класс, от которого наследуются все остальные классы в Python

```pycon
>>> class MyClass(object):
...     pass
... 
```

### oct
Получение восьмеричного представления числа

```pycon
>>> oct(42)
"0o52"
```

### open
### ord
### pow
### print

### property
Для создания свойства объекта, которое можно читать и записывать, как обычный атрибут

```python
class MyClass:
    def __init__(self):
        self._my_attr = 42

    @property
    def my_attr(self):
        return self._my_attr

    @my_attr.setter
    def my_attr(self, value):
        self._my_attr = value
```

### quit
### range
### repr

### reversed
Для переворачивания последовательности (sequence)

```pycon
>>> my_list = [1, 2, 3, 4, 5]
>>> reversed_list = reversed(my_list)
>>> list(reversed_list)
[5, 4, 3, 2, 1]
```

### round
### set

### setattr
Для установки значения атрибута объекта

```pycon
>>> class MyClass:
...     def __init__(self):
...         self.my_attr = 42
... 
>>> my_obj = MyClass()
>>> setattr(my_obj, "my_attr", 43)
>>> my_obj.my_attr
43
```

### slice

```pycon
>>> [1, 2, 3, 4, 5][1:4]
[2, 3, 4]
>>> [1, 2, 3, 4, 5][slice(1, 4)]
[2, 3, 4]
>>> slice(1, 10, 2).indices(5)
(1, 5, 2)
>>> slice(-3, None).indices(10)
(7, 10, 1)
>>> slice(-100, 100).indices(5)
(0, 5, 1)
>>> slice(None, None, -1).indices(5)
(4, -1, -1)
>>> def getitem(seq, key):
...     if isinstance(key, slice):
...         start, stop, step = key.indices(len(seq))
...         return [seq[i] for i in range(start, stop, step)]
...     else:
...         return seq[key]
... 
```

### sorted

### staticmethod
Для создания метода класса, который не принимает первый аргумент self (или cls для методов класса)

```pycon
>>> class MyClass:
...     @staticmethod
...     def my_static_method():
...         print("This is a static method")
... 
>>> MyClass.my_static_method()
This is a static method
```

### str
### sum
### super
### tuple
### type
### vars
### zip

# .

### &#95;&#95;import&#95;&#95;
Для импорта модуля во время выполнения программы

```pycon
>>> math = __import__("math")
>>> math.pi
3.141592653589793
```

### locals
Для получения словаря с локальными переменными в текущем контексте выполнения

```pycon
>>> def my_func():
...     a = 1
...     b = 2
...     print(locals())
... 
>>> my_func()
{"a": 1, "b": 2}
```

### nonlocal
Объявление переменной из внешней области видимости внутри функции

```pycon
>>> def my_func():
...     my_var = 42
...     def inner_func():
...         nonlocal my_var
...         my_var = 43
...     inner_func()
...     print(my_var)
... 
>>> my_func()
43
```

# ..
abs
aiter
all
anext
any
ascii
bin
bool
breakpoint
bytearray
bytes
callable
chr
classmethod
compile
complex
copyright
credits
delattr
dict
dir
divmod
enumerate
eval
exec
exit
filter
float
format
frozenset
getattr
globals
hasattr
hash
help
hex
id
input
int
isinstance
issubclass
iter
len
license
list
locals
map
max
memoryview
min
next
object
oct
open
ord
pow
print
property
quit
range
repr
reversed
round
set
setattr
slice
sorted
staticmethod
str
sum
super
tuple
type
vars
zip
