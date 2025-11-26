Библиотека "nt" в Python используется для работы с функциями операционной системы Windows

Методы модуля "nt" и его подмодулей:

Модуль "nt":
nt.getcwd(): Возвращает текущую рабочую директорию
nt.listdir(path): Возвращает список файлов и директорий в указанном пути
nt.mkdir(path): Создает новую директорию по указанному пути
nt.remove(path): Удаляет файл по указанному пути
nt.rename(src, dst): Переименовывает файл или директорию
nt.system(command): Выполняет команду операционной системы

Подмодуль "ntpath":
ntpath.basename(path): Возвращает имя файла или директории из указанного пути
ntpath.dirname(path): Возвращает имя директории из указанного пути
ntpath.exists(path): Проверяет, существует ли файл или директория по указанному пути
ntpath.join(path, *paths): Объединяет пути в один
ntpath.split(path): Разделяет путь на имя директории и имя файла

Некоторые часто используемые методы и их описание:

nt.getcwd(): Возвращает текущую рабочую директорию

```python
import nt
current_dir = nt.getcwd()
print(current_dir)
```

nt.listdir(path): Возвращает список файлов и директорий в указанном пути


```python
import nt
file_list = nt.listdir("C:/Users")
print(file_list)
```

nt.mkdir(path): Создает новую директорию по указанному пути

```python
import nt
nt.mkdir("C:/Users/NewDirectory")
```

nt.remove(path): Удаляет файл по указанному пути

```python
import nt
nt.remove("C:/Users/example.txt")
```

nt.rename(src, dst): Переименовывает файл или директорию

```python
import nt
nt.rename("C:/Users/old_name.txt", "C:/Users/new_name.txt")
```

nt.system(command): Выполняет команду операционной системы

```python
import nt
nt.system("dir")
```
