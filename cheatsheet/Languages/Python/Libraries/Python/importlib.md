```pycon
>>> def im():
...     import math
...
>>> math
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'math' is not defined
>>> im()
>>> math
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'math' is not defined
```

```python
import importlib

importlib.reload(my_module)
```

```python
import subprocess
import importlib

library_name = input("Введите название библиотеки, которую вы хотите установить: ")

# проверяем, установлена ли библиотека
try:
    importlib.import_module(library_name)
    print(f"Библиотека {library_name} уже установлена.")
except ImportError:
    # устанавливаем библиотеку
    subprocess.call(["pip", "install", library_name])
    print(f"Библиотека {library_name} установлена успешно.")

```
