Библиотека "warnings" в Python используется для управления предупреждениями, которые могут возникать во время выполнения программы.
Она позволяет контролировать вывод предупреждений и принимать соответствующие действия.

Методы и подмодули библиотеки "warnings":

`warn(message, warning_type, stacklevel)` - генерирует предупреждение с указанным сообщением, типом предупреждения и уровнем стека.
`filterwarnings(action, message, category, module, lineno, append)` - устанавливает фильтр для предупреждений, определяя действие, текст сообщения, категорию предупреждения, модуль, номер строки и флаг добавления фильтра.
`simplefilter(action, category=Warning, lineno=0, append=False)` - устанавливает простой фильтр для предупреждений с указанным действием, категорией, номером строки и флагом добавления фильтра.
`resetwarnings()` - сбрасывает все установленные фильтры предупреждений.
`showwarning(message, category, filename, lineno, file=None, line=None)` - выводит предупреждение с указанным сообщением, категорией, исходным файлом, номером строки, файлом вывода и строкой кода.
`catch_warnings(*, record=False, module=None)` - возвращает контекстный менеджер для временного перехвата предупреждений с опциональной записью в список или указанный модуль.

`warn(message, warning_type, stacklevel)` - генерирует предупреждение с заданным сообщением, типом предупреждения и уровнем стека.

```python
import warnings

warnings.warn("This is a warning message", UserWarning, stacklevel=2)
```

`filterwarnings(action, message, category, module, lineno, append)` - устанавливает фильтр для предупреждений с указанными параметрами.

```python
import warnings

warnings.filterwarnings("ignore", category=DeprecationWarning, module="my_module")
```

`simplefilter(action, category=Warning, lineno=0, append=False)` - устанавливает простой фильтр для предупреждений с указанным действием и категорией.

```python
import warnings

warnings.simplefilter("ignore", DeprecationWarning)
```

`resetwarnings()` - сбрасывает все установленные фильтры предупреждений.

```python
import warnings

warnings.resetwarnings()
```

`showwarning(message, category, filename, lineno, file=None, line=None)` - выводит предупреждение с указанными параметрами.

```python
import warnings

warnings.showwarning("This is a warning message", UserWarning, "example.py", 10)
```

`catch_warnings(*, record=False, module=None)` - контекстный менеджер для временного перехвата предупреждений.

```python
import warnings

with warnings.catch_warnings(record=True) as w:
    warnings.warn("This is a warning message")
    print(w[0].message)
```
