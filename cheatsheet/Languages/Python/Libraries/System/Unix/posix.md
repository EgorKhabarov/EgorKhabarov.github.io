Библиотека "posix" в Python используется для взаимодействия с функциями и операциями,
специфичными для POSIX-совместимых операционных систем, таких как Linux и macOS.

Таблица методов модуля "posix" и его подмодулей и краткое описание:

Модуль "posix":
getpid(): Возвращает идентификатор текущего процесса.
getuid(): Возвращает идентификатор пользователя текущего процесса.
getgid(): Возвращает идентификатор группы текущего процесса.
chmod(path, mode): Изменяет права доступа к файлу или директории.
chown(path, uid, gid): Изменяет владельца и группу файловой системы.
getcwd(): Возвращает текущую рабочую директорию.
listdir(path): Возвращает список файлов и директорий в указанной директории.

Подмодуль "posixpath":
join(path1, path2): Объединяет два пути в один.
isfile(path): Проверяет, является ли путь файлом.
isdir(path): Проверяет, является ли путь директорией.
basename(path): Возвращает базовое имя последнего компонента пути.
dirname(path): Возвращает каталог пути.

Список часто используемых методов, их краткое описание и

getpid(): Возвращает идентификатор текущего процесса.

```python
import os
print(os.getpid())
```

getcwd(): Возвращает текущую рабочую директорию.

```python
import os
print(os.getcwd())
```

listdir(path): Возвращает список файлов и директорий в указанной директории.

```python
import os
print(os.listdir("/path/to/directory"))
```
