<div class="container-row">
```pycon
>>> a = [[]]*3
>>> for x in a:
...     print(id(x))
...
3276075832448
3276075832448
3276075832448
>>> a[1].append(1)
>>> a
[[1], [1], [1]]
```
&nbsp;
```pycon
>>> b = [[] for _ in range(3)]
>>> for x in b:
...     print(id(x))
...
3276075828928
3276075828992
3276075828864
>>> b[1].append(1)
>>> b
[[], [1], []]
```
</div>
<div class="container-row">
```pycon
>>> c = [[]]
>>> print(id(c[0]))
3276075894784
>>> for x in (c + c):
...     print(id(x))
...
3276075894784
3276075894784
```
&nbsp;
```pycon
>>> d = ((),)*3
>>> for x in d:
...     print(id(d))
...
3276075830656
3276075830656
3276075830656
```
</div>
