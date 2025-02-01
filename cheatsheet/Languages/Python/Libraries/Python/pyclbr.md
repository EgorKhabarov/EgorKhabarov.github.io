Библиотека "pyclbr" в Python используется для анализа и чтения исходного кода классов и функций в модуле.
Она позволяет получить информацию о структуре программы, такую как классы, методы, атрибуты и их связи.

Таблица методов модуля "pyclbr" и его подмодулей:

|  Метод                | Описание                                                                        |
|-----------------------|---------------------------------------------------------------------------------|
|   `readmodule()`      | Читает и анализирует модуль, возвращая словарь классов и функций                |
|   `readmodule_ex()`   | Похож на `readmodule()`, но также возвращает дополнительную информацию о модуле |
|   `Class`             | Класс, представляющий отдельный класс из исходного кода                         |
|   `Function`          | Класс, представляющий отдельную функцию из исходного кода                       |
|   `Module`            | Класс, представляющий модуль и его структуру                                    |

### readmodule()
Читает и анализирует модуль, возвращая словарь классов и функций
```python
import pyclbr

module_data = pyclbr.readmodule("module_name")

for class_name, class_data in module_data.items():
    print(f"Class: {class_name}")
    for method_name, method_data in class_data.methods.items():
        print(f"Method: {method_name}")
```

### Class
Класс, представляющий отдельный класс из исходного кода
```python
import pyclbr

class_data = pyclbr.Class("class_name")

print(f"Class: {class_data.name}")
for method_name, method_data in class_data.methods.items():
    print(f"Method: {method_name}")
```

### Function
Класс, представляющий отдельную функцию из исходного кода
```python
import pyclbr

function_data = pyclbr.Function("function_name")

print(f"Function: {function_data.name}")
print(f"Start line: {function_data.lineno}")
```

### Module
Класс, представляющий модуль и его структуру
```python
import pyclbr

module_data = pyclbr.Module("module_name")

print(f"Module: {module_data.name}")
for class_name, class_data in module_data.classes.items():
    print(f"Class: {class_name}")
```
