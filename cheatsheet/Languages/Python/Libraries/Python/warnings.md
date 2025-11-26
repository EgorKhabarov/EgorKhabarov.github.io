Библиотека "warnings" в Python используется для управления предупреждениями, которые могут возникать во время выполнения программы
Она позволяет контролировать вывод предупреждений и принимать соответствующие действия

|                                                                          |                                                                                                                                                                |
|--------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `warn(message, warning_type, stacklevel)`                                | Генерирует предупреждение с указанным сообщением,<br/>типом предупреждения и уровнем стека                                                                     |
| `filterwarnings(action, message, category, module, lineno, append)`      | Устанавливает фильтр для предупреждений, определяя действие,<br/>текст сообщения, категорию предупреждения,<br/>модуль, номер строки и флаг добавления фильтра |
| `simplefilter(action, category=Warning, lineno=0, append=False)`         | Устанавливает простой фильтр для предупреждений<br/>с указанным действием, категорией, номером строки<br/>и флагом добавления фильтра                          |
| `resetwarnings()`                                                        | Сбрасывает все установленные фильтры предупреждений                                                                                                            |
| `showwarning(message, category, filename, lineno, file=None, line=None)` | Выводит предупреждение с указанным сообщением, категорией,<br/>исходным файлом, номером строки, файлом вывода и строкой кода                                   |
| `catch_warnings(*, record=False, module=None)`                           | Возвращает контекстный менеджер для временного перехвата<br/>предупреждений с опциональной записью в список или указанный модуль                               |

### warn
```python
import warnings

warnings.warn("This is a warning message", UserWarning, stacklevel=2)
```

### filterwarnings
`filterwarnings(action, message, category, module, lineno, append)` - устанавливает фильтр для предупреждений с указанными параметрами
```python
import warnings

warnings.filterwarnings("ignore", category=DeprecationWarning, module="my_module")
```

### simplefilter
`simplefilter(action, category=Warning, lineno=0, append=False)` - устанавливает простой фильтр для предупреждений с указанным действием и категорией
```python
import warnings

warnings.simplefilter("ignore", DeprecationWarning)
```

### resetwarnings
`resetwarnings()` - сбрасывает все установленные фильтры предупреждений
```python
import warnings

warnings.resetwarnings()
```

### showwarning
`showwarning(message, category, filename, lineno, file=None, line=None)` - выводит предупреждение с указанными параметрами
```python
import warnings

warnings.showwarning("This is a warning message", UserWarning, "example.py", 10)
```

### catch_warnings
`catch_warnings(*, record=False, module=None)` - контекстный менеджер для временного перехвата предупреждений
```python
import warnings

with warnings.catch_warnings(record=True) as w:
    warnings.warn("This is a warning message")
    print(w[0].message)
```
