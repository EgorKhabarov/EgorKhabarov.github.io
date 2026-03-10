# int

### as_integer_ratio
int.`as_integer_ratio`()
Возвращает кортеж, представляющий рациональное число, близкое к данному целому числу
```pycon
>>> (10).as_integer_ratio()
(10, 1)
```
### bit_count
int.`bit_count`()
Возвращает количество установленных битов (битов со значением 1) в двоичном представлении числа
```pycon
>>> (123).bit_count()
6
>>> bin(123).count("1")
6
```
### bit_length
int.`bit_length`()
Возвращает количество битов, необходимых для представления числа в двоичном виде
```pycon
>>> (256).bit_length()
9
>>> len(bin(256)[2:])
9
```
### conjugate
int.`conjugate`()
Возвращает сопряженное комплексное число
```pycon
>>> (3 + 4j).conjugate()
(3-4j)
```
### from_bytes
int.`from_bytes`(bytes, byteorder="big", signed=False)
Преобразует байтовую последовательность в целое число, используя указанный порядок байтов и знак
```pycon
>>> int.from_bytes(b"\x00\x10", byteorder="big", signed=False)
16
>>> int.from_bytes(b'\x01\x00', "big")
256
```
### to_bytes
int.`to_bytes`(length=1, byteorder="big", signed=False)
Преобразует целое число в байтовую последовательность, используя указанный порядок байтов и знак
```pycon
>>> (1024).to_bytes(length=2, byteorder="big", signed=False)
b"\x04\x00"
>>> (256).to_bytes(2, "big")
b'\x01\x00'
```
#### byteorder
"big" big-endian Старший байт первым
"little" little-endian Младший байт первым
```pycon
>>> 0x1234.to_bytes(2, "big")
b'\x12\x34'
>>> 0x1234.to_bytes(2, "little")
b'\x34\x12'
```
#### signed
`signed=True` Позволяет хранить отрицательные числа
```pycon
>>> (-1).to_bytes(1, "big")
Traceback (most recent call last):
  File "<input>", line 1, in <module>
    (-1).to_bytes(1, "big")
    ~~~~~~~~~~~~~^^^^^^^^^^
OverflowError: can't convert negative int to unsigned
>>> (-1).to_bytes(1, "big", signed=True)
b'\xff'
```
### imag
int.`imag`
Возвращает мнимую часть комплексного числа
```pycon
>>> (5).imag
0
>>> (3 + 4j).imag
4.0
```
### real
int.`real`
Возвращает действительную часть комплексного числа
```pycon
>>> (5).real
5
>>> (3 + 4j).real
3.0
```
### numerator
int.`numerator`
Возвращает числитель числа в виде рациональной дроби
```pycon
>>> (3).numerator
3
```
### denominator
int.`denominator`
Возвращает знаменатель числа в виде рациональной дроби
```pycon
>>> (3).denominator
1
```
### is_integer
int.`is_integer`()
Всегда возвращает True (для совместимости с float)
```pycon
>>> (5).is_integer())
True
```
