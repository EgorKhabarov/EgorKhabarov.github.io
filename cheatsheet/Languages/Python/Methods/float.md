# float

### as_integer_ratio
float.`as_integer_ratio`()
Возвращает кортеж, представляющий рациональное число, близкое к данному целому числу
```pycon
>>> 10.5.as_integer_ratio()
(21, 2)
```
### conjugate
float.`conjugate`()
Возвращает сопряженное комплексное число
```pycon
>>> 10.5.conjugate()
10.5
```
### fromhex
float.`fromhex`(string)
```pycon
>>> float.fromhex("ff")
255.0
```
### hex
float.`hex`()
```pycon
>>> (-0.1).hex()
"-0x1.999999999999ap-4"
>>> 3.14159.hex()
"0x1.921f9f01b866ep+1"
```
### imag
float.`imag`
Возвращает мнимую часть комплексного числа
```pycon
>>> 10.5.imag
0.0
```
### real
float.`real`
Возвращает действительную часть комплексного числа
```pycon
>>> 10.0.real
10.0
```
### is_integer
float.`is_integer`()
```pycon
>>> 10.5.is_integer()
False
>>> 10.0.is_integer()
True
```
