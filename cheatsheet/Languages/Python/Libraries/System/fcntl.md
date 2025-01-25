Библиотека "fcntl" в Python используется для обращения к системным вызовам управления файловыми дескрипторами и флагами файлового управления.

Методы модуля "fcntl" включают:

fcntl.flock(fd, operation): Блокирует или разблокирует файловый дескриптор при помощи операции блокировки.
fcntl.ioctl(fd, request, arg): Вызывает системный вызов IOCTL для управления устройством, связанным с файловым дескриптором.
fcntl.fcntl(fd, command, arg): Выполняет команду файлового управления на файловом дескрипторе, такую как получение или изменение флагов управления файла.
и другие...

Некоторые из наиболее распространенных методов "fcntl" включают:

fcntl.flock(fd, operation) Блокирует или разблокирует файловый дескриптор.

```python
import fcntl

file_descriptor = open("file.txt", "w")
fcntl.flock(file_descriptor, fcntl.LOCK_EX)
# Выполните операции с заблокированным файлом
fcntl.flock(file_descriptor, fcntl.LOCK_UN)
file_descriptor.close()
```

fcntl.ioctl(fd, request, arg) Выполняет системный вызов IOCTL для управления устройством.

```python
import fcntl

file_descriptor = open("/dev/sda", "r")
request_code = 123  # Код запроса, связанный с устройством
arg = 456  # Аргумент IOCTL
fcntl.ioctl(file_descriptor, request_code, arg)
file_descriptor.close()
```

fcntl.fcntl(fd, command, arg) Выполняет команду файлового управления на файловом дескрипторе.

```python
import fcntl

file_descriptor = open("file.txt", "r")
command = fcntl.F_GETFL  # Получить флаги управления файла
flags = fcntl.fcntl(file_descriptor, command, 0)
print(flags)
file_descriptor.close()
```
