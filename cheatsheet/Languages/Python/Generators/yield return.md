```pycon
>>> def generator():
...     yield 1
...     yield 2
...     return 3
... 
>>> gen = generator()
>>> next(gen)
1
>>> next(gen)
1
>>> try:
...     next(gen)
... except StopIteration as err:
...     print(err.value)
... 
3
```
