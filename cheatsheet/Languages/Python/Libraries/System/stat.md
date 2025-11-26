Библиотека "stat" в Python используется для работы с информацией о файловой системе, такой как атрибуты файла, права доступа и временные метки

|                     |                                                    |
|---------------------|----------------------------------------------------|
| stat.S_ISDIR(mode)  | Проверяет, является ли файл директорией            |
| stat.S_ISREG(mode)  | Проверяет, является ли файл обычным файлом         |
| stat.S_ISLNK(mode)  | Проверяет, является ли файл символической ссылкой  |
| stat.S_ISSOCK(mode) | Проверяет, является ли файл сокетом                |
| stat.S_ISFIFO(mode) | Проверяет, является ли файл каналом FIFO           |
| stat.S_ISBLK(mode)  | Проверяет, является ли файл блочным устройством    |
| stat.S_ISCHR(mode)  | Проверяет, является ли файл символьным устройством |
| stat.S_IMODE(mode)  | Возвращает режим доступа к файлу                   |
| stat.S_IFMT(mode)   | Возвращает тип файла и режим доступа               |

### Примеры

```python
import os
import stat

file_path = "path/to/file.txt"
file_stat = os.stat(file_path)

if stat.S_ISDIR(file_stat.st_mode):
    print("File is a directory")
else:
    print("File is not a directory")

if stat.S_ISREG(file_stat.st_mode):
    print("File is a regular file")
else:
    print("File is not a regular file")

print("File mode:", stat.S_IMODE(file_stat.st_mode))
```
