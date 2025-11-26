## Декораторы

Специальные функции, которые позволяют модифицировать поведение других функций
Они часто используются для добавления нового функционала к существующим функциям без изменения их кода

```python
def cache_decorator(func):
    cache = {}
    def wrapper(*args, **kwargs):
        key = f"{args}:{kwargs}"
        if key not in cache:
            cache[key] = func(*args, **kwargs)
        return cache[key]
    return wrapper

@cache_decorator
def expensive_function(x):
    # дорогая расчетная функция
    return x**2

print(expensive_function(2))  # 4
print(expensive_function(2))  # 4 (значение берется из кеша)
print(expensive_function(3))  # 9
print(expensive_function(3))  # 9 (значение берется из кеша)
```

## closure (Замыкания)

Функции, которые ссылаются на переменные, определенные вне этой функции
Они позволяют сохранять состояние переменных между вызовами функции
Замыкания часто используются в Python для создания функций-генераторов, которые возвращают новые функции с измененными параметрами

Например, следующий код создает функцию-генератор, которая возвращает функции, увеличивающие число на указанное значение:

```python
def make_incrementor(n):
    def incrementor(x):
        return x + n
    return incrementor

plus_3 = make_incrementor(3)
plus_5 = make_incrementor(5)

print(plus_3(10))  # 13
print(plus_5(10))  # 15
```
