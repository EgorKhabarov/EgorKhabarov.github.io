## slice

```python
print([1, 2, 3, 4, 5][1:4])  # [2, 3, 4]
print([1, 2, 3, 4, 5][slice(1, 4)])  # [2, 3, 4]
```

## frozenset
Неизменяемый тип данных, представляющий собой неупорядоченное множество уникальных элементов

```python
print(frozenset([1, 2, 2, 3, 4]))  # frozenset({1, 2, 3, 4})
```

## memoryview
Доступ к буферу памяти объекта без копирования его данных

```pycon
>>> mv = memoryview(bytearray("ABC", "UTF-8"))
>>> mv[0]           # доступ к нулевому индексу представления памяти
65
>>> bytes(mv[0:2])  # создать байт из представления памяти
b"AB"
>>> list(mv[0:3])   # создать список из представления памяти
[65, 66, 67]
```

## hasattr
Для проверки наличия атрибута (метода или свойства) у объекта

```python
class MyClass:
    def __init__(self):
        self.my_attr = 42

my_obj = MyClass()
print(hasattr(my_obj, "my_attr"))  # True
print(hasattr(my_obj, "non_existent_attr"))  # False
```

## reversed
Для переворачивания последовательности (sequence)

```python
my_list = [1, 2, 3, 4, 5]
reversed_list = reversed(my_list)
print(list(reversed_list))  # [5, 4, 3, 2, 1]
```

## &#95;&#95;import&#95;&#95;
Для импорта модуля во время выполнения программы

```python
math = __import__("math")
print(math.pi)  # 3.141592653589793
```

## staticmethod
Для создания метода класса, который не принимает первый аргумент self (или cls для методов класса)

```python
class MyClass:
    @staticmethod
    def my_static_method():
        print("This is a static method")

MyClass.my_static_method()  # This is a static method
```

## setattr
Для установки значения атрибута объекта

```python
class MyClass:
    def __init__(self):
        self.my_attr = 42

my_obj = MyClass()
setattr(my_obj, "my_attr", 43)
print(my_obj.my_attr)  # 43
```

## property
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
        self._my_attr
```

## object
Базовый класс, от которого наследуются все остальные классы в Python

```python
class MyClass(object):
    pass
```

## locals
Для получения словаря с локальными переменными в текущем контексте выполнения

```python
def my_func():
    a = 1
    b = 2
    print(locals())

my_func()  # {"a": 1, "b": 2}
```

## globals
Для получения словаря с глобальными переменными в текущем модуле

```python
my_var = 42
print(globals())  # {"__name__": "__main__", "__doc__": None, "__package__": None, "my_var": 42, ...}
```

## getattr
Для получения значения атрибута объекта по его имени

```python
class MyClass:
    def __init__(self):
        self.my_attr = 42

print(getattr(MyClass(), "my_attr"))  # 42
```

## complex
Для создания комплексного числа

```python
print(complex(1, 2))  # (1+2j)
```

## compile
Для компиляции строки с кодом Python в объект-код

```python
exec(compile('print("Hello, world!")', "<string>", "exec"))  # Hello, world!
```

## bytearray
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

## abs
Получения абсолютного значения числа

```python
print(abs(-42))  # 42
```

## bin
Получения двоичного представления числа

```python
print(bin(42))  # 0b101010
```

## bytes
Неизменяемый тип данных, представляющий собой массив байтов

```python
print(bytes([1, 2, 3, 4, 5]))  # b"\x01\x02\x03\x04\x05"
```

## callable
Является ли объект вызываемым (т.е. функцией или методом)

```python
def my_func():
    pass

class MyClass:
    def my_method(self):
        pass

print(callable(my_func))  # True
print(callable(MyClass().my_method))  # True
print(callable(42))  # False
```

## chr
Получение символа Unicode по его коду

```python
print(chr(97))  # "a"
```

## classmethod
Создание метода класса. Этот метод может быть вызван без создания экземпляра класса

```python
class MyClass:
    my_class_attr = 42

    @classmethod
    def my_class_method(cls):
        print(cls.my_class_attr)

MyClass.my_class_method()  # 42
```

## delattr
Удаление атрибута объекта

```python
class MyClass:
    my_attr = 42

my_obj = MyClass()
delattr(my_obj, "my_attr")
print(hasattr(my_obj, "my_attr"))  # False
```

## dir
Получение списка всех атрибутов объекта

```python
print(dir([1, 2, 3]))  # ["__add__", "__class__", "__contains__", ...]
```

## divmod
Получения частного и остатка от деления двух чисел

```python
print(divmod(42, 5))  # (8, 2)
```

## filter
Фильтрация элементов последовательности с помощью функции

```python
print(list(filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5])))  # [2, 4]
```

## oct
Получение восьмеричного представления числа

```python
print(oct(42))  # 0o52
```

## nonlocal
Объявление переменной из внешней области видимости внутри функции

```python
def my_func():
    my_var = 42
    def inner_func():
        nonlocal my_var
        my_var = 43
    inner_func()
    print(my_var)

my_func()  # 43
```
