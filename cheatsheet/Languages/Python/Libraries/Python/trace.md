Библиотека "trace" используется в Python для отладки и трассировки выполнения программы.
Она предоставляет инструменты для отслеживания, как программа выполняется и какие функции вызываются.

|                                                          |                                                              |
|----------------------------------------------------------|--------------------------------------------------------------|
| `traceback.print_exc(limit=None, file=None, chain=True)` | Выводит трассировку текущего исключения в файл или stdout    |
| `traceback.format_exc(limit=None, chain=True)`           | Возвращает трассировку текущего исключения в виде строки     |
| `sys.settrace(tracefunc)`                                | Устанавливает функцию трассировки для последующих вызовов    |
| `sys.gettrace()`                                         | Возвращает текущую функцию трассировки                       |
| `sys.setprofile(profilefunc)`                            | Устанавливает функцию профилирования для последующих вызовов |
| `sys.getprofile()`                                       | Возвращает текущую функцию профилирования                    |


### print_exc
`traceback.print_exc()` - выводит трассировку текущего исключения в стандартный вывод
```python
try:
    # код, который может вызвать исключение
except Exception:
    traceback.print_exc()
```

### settrace
`sys.settrace()` - устанавливает функцию трассировки для отслеживания вызовов функций
```python
def trace_func(frame, event, arg):
    print(f"Calling function {frame.f_code.co_name}")
    return trace_func

sys.settrace(trace_func)
# код, вызывающий функции
sys.settrace(None)  # отключение трассировки
```

### setprofile
`sys.setprofile()` - устанавливает функцию профилирования для измерения времени выполнения функций
```python
import cProfile

def profile_func(frame, event, arg):
    profiler = cProfile.Profile()
    profiler.enable()
    return profiler

sys.setprofile(profile_func)
# код, вызывающий функции
sys.setprofile(None)  # отключение профилирования
```
