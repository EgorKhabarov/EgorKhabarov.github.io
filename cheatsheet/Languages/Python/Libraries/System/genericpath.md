Библиотека "genericpath" в Python используется для работы с путями и файловой системой на разных платформах.
Она предоставляет универсальные методы для обработки путей, создания новых путей, проверки наличия файлов и директорий,
а также для работы с именами файлов.

Таблица методов и их описания в модуле "genericpath":

| Метод              | Описание                                                              |
|--------------------|-----------------------------------------------------------------------|
| isdir(path)        | Проверяет, является ли указанный путь директорией                     |
| isfile(path)       | Проверяет, является ли указанный путь файлом                          |
| exists(path)       | Проверяет, существует ли указанный путь                               |
| lexists(path)      | Проверяет, существует ли указанный путь (обходя символические ссылки) |
| split(path)        | Разделяет путь на директорию и базовое имя файла                      |
| splitext(path)     | Разделяет путь на базовое имя файла и расширение                      |
| basename(path)     | Возвращает последний компонент пути (имя файла или директории)        |
| dirname(path)      | Возвращает директорию из пути                                         |
| join(path, *paths) | Объединяет пути в переносимый образ                                   |
| normpath(path)     | Преобразует путь, удаляя избыточные разделители и ссылки "." и ".."   |
| abspath(path)      | Возвращает абсолютный путь                                            |


### isdir(path)
Проверяет, является ли указанный путь директорией
```python
import os.path

path = "/path/to/directory"
if os.path.isdir(path):
    print(f"{path} is a directory.")
```

### isfile(path)
Проверяет, является ли указанный путь файлом
```python
import os.path

path = "/path/to/file.txt"
if os.path.isfile(path):
    print(f"{path} is a file.")
```

### exists(path)
Проверяет, существует ли указанный путь
```python
import os.path

path = "/path/to/file.txt"
if os.path.exists(path):
    print(f"{path} exists.")
```

### splitext(path)
Разделяет путь на базовое имя файла и расширение
```python
import os.path

path = "/path/to/file.txt"
base_name, extension = os.path.splitext(path)
print(f"Base name: {base_name}")
print(f"Extension: {extension}")
```
