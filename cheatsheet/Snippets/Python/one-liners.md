### Рекурсивное разворачивание вложенных списков любой глубины

```python
flatten = lambda lst: [
    x
    for sub in lst
    for x in (
        flatten(sub)
        if isinstance(sub, list)
        else [sub]
    )
]
```

### Декоратор для мемоизации результатов функции

```python
memoize = lambda f: (
    lambda *args, _cache={}, **kwargs: _cache.setdefault(
        (args, tuple(kwargs.items())),
        f(*args, **kwargs),
    )
)
```

### Разбиение списка на куски длины n

```python
chunked = lambda lst, n: [lst[i:i+n] for i in range(0, len(lst), n)]
```

### Уникализация последовательности с сохранением порядка

```python
uniq = lambda seq: list(dict.fromkeys(seq))
```

### Глубокий доступ к вложенным ключам словаря

```python
deep_get = lambda d, *keys: __import__("functools").reduce(
    lambda a, k: a.get(k) if isinstance(a, dict) else None, keys, d
)
```

### Группировка списка словарей по значению ключа

```python
group_by = lambda seq, key: {
    k: [d for d in seq if d.get(key) == k]
    for k in set(d.get(key) for d in seq)
}
```
