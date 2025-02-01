Библиотека `jsonpointer` используется для работы с указателями JSON (JSON pointers)
Она предоставляет функциональность для создания, обновления и извлечения данных из JSON-структур с использованием указателей

Методы модуля "jsonpointer" и их краткое описание

|                                         |                                                                                |
|-----------------------------------------|--------------------------------------------------------------------------------|
| `resolve_pointer(json_obj, pointer)`    | Разрешает указатель JSON и возвращает соответствующее значение из JSON-объекта |
| `set_pointer(json_obj, pointer, value)` | Устанавливает значение по указателю JSON в JSON-объекте                        |
| `remove_pointer(json_obj, pointer)`     | Удаляет значение по указателю JSON из JSON-объекта                             |
| `list_pointers(json_obj)`               | Возвращает список всех указателей JSON в JSON-объекте                          |
| `escape_pointer(pointer)`               | Экранирует специальные символы в указателе JSON                                |

### resolve_pointer(json_obj, pointer)
Разрешает указатель JSON и возвращает соответствующее значение из JSON-объекта
```python
import jsonpointer

json_obj = {"name": "John", "age": 30}
pointer = "/name"
value = jsonpointer.resolve_pointer(json_obj, pointer)
print(value)  # John
```

### set_pointer(json_obj, pointer, value)
Устанавливает значение по указателю JSON в JSON-объекте
```python
import jsonpointer

json_obj = {"name": "John", "age": 30}
pointer = "/name"
value = "Jane"
jsonpointer.set_pointer(json_obj, pointer, value)
print(json_obj)  # {"name": "Jane", "age": 30}
```

### remove_pointer(json_obj, pointer)
Удаляет значение по указателю JSON из JSON-объекта
```python
import jsonpointer

json_obj = {"name": "John", "age": 30}
pointer = "/name"
jsonpointer.remove_pointer(json_obj, pointer)
print(json_obj)  # {"age": 30}
```
