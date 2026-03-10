# list

### append
list.`append`(object)
Добавляет элемент в конец списка
```pycon
>>> lst = [1, 2, 3]
>>> lst.append(4)
>>> lst
[1, 2, 3, 4]
```
### clear
list.`clear`()
Удаляет все элементы списка
```pycon
>>> lst = [1, 2, 3]
>>> lst.clear()
>>> lst
[]
```
### сору
list.`сору`()
Возвращает поверхностную копию списка
```pycon
>>> lst = [1, 2, 3]
>>> lst1 = lst.copy()
>>> lst
[1, 2, 3]
>>> lst == lst1
True
>>> lst is lst1
False
```
### count
list.`count`(value)
Возвращает количество вхождений значения
```pycon
>>> [1, 1, 2].count(1)
2
```
### extend
list.`extend`(iterable)
Добавляет все элементы из итерируемого объекта
```pycon
>>> lst = [1, 2, 3]
>>> lst.extend([4, 5])
>>> lst
[1, 2, 3, 4, 5]
```
### index
list.`index`(value\[, start=0\[, stop=sys.maxsize]])
Возвращает индекс первого вхождения
```pycon
>>> [1, 2, 3].index(2)
1
```
### insert
list.`insert`(index, object)
Вставляет элемент по индексу
```pycon
>>> lst = [1, 2, 3]
>>> lst.insert(3, 4)
>>> lst
[1, 2, 3, 4]
```
### pop
list.`pop`(index=-1)
Удаляет и возвращает элемент по индексу (по умолчанию последний)
```pycon
>>> lst = [1, 2, 3]
>>> lst.pop(2)
3
>>> lst
[1, 2]
```
### remove
list.`remove`(value)
Удаляет первое вхождение значения
```pycon
>>> lst = [1, 2, 3]
>>> lst.remove(2)
>>> lst
[1, 3]
```
### reverse
list.`reverse`()
Разворачивает список на месте
```pycon
>>> lst = [1, 2, 3]
>>> lst.reverse()
>>> lst
[3, 2, 1]
```
### sort
list.`sort`(*, key=None, reverse=False)
Сортирует список на месте
```pycon
>>> lst = [4, 3, 5]
>>> lst.sort()
>>> lst
[3, 4, 5]
>>> lst.sort(reverse=True)
[5, 4, 3]
>>> lst.sort(key=lambda x: x > 4)
[4, 3, 5]
```
### \_\_add\_\_
list.`__add__`(other) и `+`
```pycon
>>> a, b = [1, 2], [3, 4]
>>> a + b
[1, 2, 3, 4]
>>> a.__add__(b)
[1, 2, 3, 4]
```
### \_\_iadd\_\_
list.`__iadd__`(other) и `+=`
```pycon
>>> a = [1, 2]
>>> a += [3, 4]
>>> a
[1, 2, 3, 4]
>>> a.__iadd__([5])
>>> a
[1, 2, 3, 4, 5]
```
### \_\_mul\_\_ и \_\_rmul\_\_
list.`__mul__`(n) и `*`
```pycon
>>> [1, 2] * 3
[1, 2, 1, 2, 1, 2]
>>> [1, 2].__mul__(3)
[1, 2, 1, 2, 1, 2]
>>> 3 * [1, 2]
[1, 2, 1, 2, 1, 2]
>>> [1, 2].__rmul__(3)
[1, 2, 1, 2, 1, 2]
```
### \_\_imul\_\_
list.`__imul__`(n) и `*=`
```pycon
>>> a = [1, 2]
>>> a *= 3
>>> a
[1, 2, 1, 2, 1, 2]
>>> [1, 2].__imul__(3)
[1, 2, 1, 2, 1, 2]
```
### \_\_eq\_\_
list.`__eq__`(other) и `==`
```pycon
>>> [1, 2] == [1, 2]
True
>>> [1, 2].__eq__([1, 2])
True
```
### \_\_lt\_\_ и \_\_gt\_\_
list.`__lt__`(other) или list.`__gt__`(other) и `<` или `>`
Проверяет "меньше" или "больше" (лексикографически)
```pycon
>>> [1, 2] < [1, 3]
True
>>> [1, 2].__lt__([1, 3])
True
>>> [2] > [1]
True
>>> [2].__gt__([1])
True
```
### \_\_le\_\_ и \_\_ge\_\_
list.`__le__`(other) или list.`__ge__`(other) и `<=` или `>=`
```pycon
>>> [1, 2] <= [1, 2]
True
>>> [1, 2].__le__([1, 2])
True
>>> [2] >= [1]
True
>>> [2].__ge__([1])
True
```
