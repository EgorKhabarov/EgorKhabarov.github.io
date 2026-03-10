# set

### add
set`.add`(element)
Добавляет элемент `element` во множество
Если элемент уже присутствует, ничего не происходит
```pycon
>>> s = {1, 2, 3}
>>> s.add(4)
>>> s
{1, 2, 3, 4}
>>> s.add(3)
>>> s
{1, 2, 3, 4}
```
### issubset
set`.issubset`(set2)
Проверяет, является ли `set` подмножеством `set2`
Возвращает `True`, если так, иначе `False`
```pycon
>>> {1, 2, 3}.issubset({0, 1, 2, 3, 4})
True
>>> {1, 2, 3}.issubset({0, 1, 3, 4})
False
```
### isdisjoint
set`.isdisjoint`(set2)
Проверяет, есть ли общие элементы между `set` и `set2`
Возвращает `True`, **если нет**, иначе `False`
```pycon
>>> {1, 2, 3}.isdisjoint({4, 5, 6})
True
>>> {1, 2, 3}.isdisjoint({3, 4, 5})
False
```
### issuperset
set`.issuperset`(set2)
Проверяет, является ли `set` надмножеством `set2`
Возвращает `True`, если так, иначе `False`
```pycon
>>> {0, 1, 2, 3, 4}.issuperset({1, 2, 3})
True
>>> {0, 1, 3, 4}.issuperset({1, 2, 3})
False
```
### copy
set`.copy()`
Возвращает копию множества
```pycon
>>> first_set = {1, 2, 3}
>>> id(first_set)
...........64
>>> id(first_set.copy())
...........88
```
### | и union
`|` и set`.union`(set2)
Возвращает новое множество, содержащее все элементы из `set` и `set2`
```pycon
>>> {1, 2} | {1, 2, 3, 4}
{1, 2, 3, 4}
>>> {1, 2}.union({1, 2, 3, 4})
{1, 2, 3, 4}
```
### - и difference
`-` и set`.difference`(set2)
Возвращает новое множество, содержащее элементы из `set`, которые отсутствуют в `set2`
```pycon
>>> {1, 2, 3, 4} - {2, 3}
{1, 4}
>>> {1, 2, 3, 4}.difference({2, 3})
{1, 4}
```
### & и intersection
`&` и set`.intersection`(set2)
Возвращает новое множество, содержащее только элементы, присутствующие одновременно в `set` и `set2`
```pycon
>>> {1, 2, 3} & {2, 3, 4}
{2, 3}
>>> {1, 2, 3}.intersection({2, 3, 4})
{2, 3}
```
### ^ и symmetric_difference
`^` и set`.symmetric_difference`(set2)
Возвращает новое множество, содержащее элементы, присутствующие только в одном из `set` и `set2`
```pycon
>>> {1, 2, 3} ^ {3, 4, 5}
{1, 2, 4, 5}
>>> {1, 2, 3}.symmetric_difference({3, 4, 5})
{1, 2, 4, 5}
```
### |= и update
`|=` и set`.update`(set2)
Обновляет множество, добавляя элементы из `set2`
```pycon
>>> s1 = {1, 2, 3}
>>> s1 |= {2, 3, 4, 5}
>>> s1
{1, 2, 3, 4, 5}
>>> s1.update({4, 5, 6, 7})
>>> s1
{1, 2, 3, 4, 5, 6, 7}
```
### -= и difference_update
`-=` и set`.difference_update`(set2)
Обновляет множество, удаляя элементы из `set`, которые присутствуют в `set2`
```pycon
>>> s1 = {1, 2, 3}
>>> s1 -= {3, 4, 5}
>>> s1
{1, 2}
>>> s1.difference_update({2})
>>> s1
{1}
```
### &= и intersection_update
`&=` и set`.intersection_update`(set2)
Обновляет множество, оставляя только элементы, присутствующие одновременно в `set` и `set2`
```pycon
>>> s1 = {1, 2, 3}
>>> s1 &= {2, 3, 4}
>>> s1
{2, 3}
>>> s1.intersection_update({1, 2, 3, 4})
>>> s1
{2, 3}
```
### ^= и symmetric_difference_update
`^=` и set`.symmetric_difference_update`(set2)
Обновляет множество, оставляя только элементы, присутствующие только в одном из `set` и `set2`
```pycon
>>> s1 = {1, 2, 3}
>>> s1 ^= {3, 4, 5}
>>> s1
{1, 2, 4, 5}
>>> s1.symmetric_difference_update({4, 5, 6})
>>> s1
{1, 2, 6}
```
### pop
set`.pop()`
Удаляет и возвращает произвольный элемент из множества
Если множество пустое, возникает исключение `KeyError`
```pycon
>>> {1, 2, 3}.pop()
1
```
### clear
set`.clear()`
Удаляет все элементы из множества, делая его пустым
```pycon
>>> s = {1, 2, 3}
>>> s.clear()
>>> s
set()
```
### remove
set`.remove`(element)
Удаляет элемент `element` из множества
Если элемент не найден, возникает исключение `KeyError`
```pycon
>>> s = {1, 2, 3}
>>> s.remove(2)
>>> s
{1, 3}
>>> s.remove(145)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 145
```
### discard
set`.discard`(element)
Удаляет элемент `element` из множества
Если элемент не найден, ничего не происходит
```pycon
>>> s = {1, 2, 3}
>>> s.discard(2)
>>> s
{1, 3}
>>> s.discard(145)
>>> s
{1, 3}
```
### < или > и \_\_lt\_\_ или \_\_gt\_\_
Оператор `>` для множеств в Python проверяет, содержит ли первое множество
все элементы второго и при этом **имеет хотя бы один дополнительный элемент**
```pycon
>>> {1, 2, 3} < {1, 2, 3, 4}
True
>>> {1, 2, 3} < {1, 3, 4, 5}
False
```
# frozenset
В Python замороженный означает, что объект не может быть изменен
```pycon
>>> s = {1, 2, 3}
>>> s
{1, 2, 3}
>>> s.add(4)
>>> s
{1, 2, 3, 4}
>>> fs = frozenset((1, 2, 3))
>>> fs
frozenset({1, 2, 3})
>>> fs.add(4)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'frozenset' object has no attribute 'add'
```
