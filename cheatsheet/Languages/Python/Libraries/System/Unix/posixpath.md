Библиотека "posixpath" в Python используется для работы с путями файловой системы в POSIX-совместимых операционных системах
Она предоставляет функции и методы для манипуляции, анализа и навигации по путям к файлам и директориям

Методы и подмодули библиотеки "posixpath":

`posixpath.basename(path)`: Возвращает базовое имя файла или директории из заданного пути
`posixpath.dirname(path)`: Возвращает имя директории из заданного пути
`posixpath.isabs(path)`: Проверяет, является ли заданный путь абсолютным
`posixpath.join(path, *paths)`: Объединяет компоненты пути в один
`posixpath.normcase(path)`: Возвращает нормализованную версию заданного пути с учетом регистра символов
`posixpath.normpath(path)`: Возвращает нормализованную версию заданного пути с учетом символов ".", ".." и разделителей
`posixpath.realpath(path)`: Возвращает каноническое имя (полный путь) для заданного пути
`posixpath.split(path)`: Разделяет заданный путь на имя директории и базовое имя файла или директории

Некоторые из наиболее часто используемых методов библиотеки "posixpath":

`basename(path)`: Возвращает имя файла из заданного пути

```python
import posixpath

path = "/home/user/example.txt"
filename = posixpath.basename(path)
print(filename)  # example.txt
```

`dirname(path)`: Возвращает имя директории из заданного пути

```python
import posixpath

path = "/home/user/example.txt"
directory = posixpath.dirname(path)
print(directory)  # /home/user
```

`isabs(path)`: Проверяет, является ли заданный путь абсолютным

```python
import posixpath

path = "/home/user/example.txt"
is_absolute = posixpath.isabs(path)
print(is_absolute)  # True
```
