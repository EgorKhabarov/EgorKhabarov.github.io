Библиотека "psutil" в Python используется для доступа и управления информацией о системе и процессах
Она предоставляет функции для получения информации о процессоре, памяти, дисках, сети и др
Это полезно для мониторинга системы, оптимизации ресурсов и отладки

| Метод                    | Описание                                        |
|--------------------------|-------------------------------------------------|
| psutil.cpu_percent()     | Возвращает процент использования ЦП             |
| psutil.virtual_memory()  | Возвращает информацию о виртуальной памяти      |
| psutil.disk_usage()      | Возвращает использование дискового пространства |
| psutil.net_io_counters() | Возвращает сетевые счетчики ввода-вывода        |
| psutil.process_count()   | Возвращает количество запущенных процессов      |

### cpu_percent()
Возвращает текущий процент использования CPU в виде числа от 0 до 100
```python
import psutil

cpu_percent = psutil.cpu_percent()
print("Текущий процент использования CPU:", cpu_percent)
```

### virtual_memory()
Возвращает информацию о виртуальной памяти в виде объекта
Можно получить доступ к атрибутам, таким как "total" (всего памяти), "available" (доступно памяти), "used" (используется памяти) и др
```python
import psutil

virtual_memory = psutil.virtual_memory()
print("Общая доступная память:", virtual_memory.total)
print("Доступная память:", virtual_memory.available)
print("Используется памяти:", virtual_memory.used)
```

### disk_usage()
Возвращает информацию об использовании дискового пространства для указанного пути в виде объекта
Можно получить доступ к атрибутам, таким как "total" (всего пространства), "used" (используется пространство), "free" (свободное пространство) и др
```python
import psutil

disk_usage = psutil.disk_usage("/")
print("Общее пространство диска:", disk_usage.total)
print("Используется пространства диска:", disk_usage.used)
print("Свободное пространство диска:", disk_usage.free)
```

### net_io_counters()
Возвращает сетевые счетчики ввода-вывода в виде объекта
Можно получить доступ к атрибутам, таким как "bytes_sent" (отправленные байты), "bytes_recv" (полученные байты), "packets_sent" (отправленные пакеты) и др
```python
import psutil

net_io_counters = psutil.net_io_counters()
print("Отправленные байты:", net_io_counters.bytes_sent)
print("Полученные байты:", net_io_counters.bytes_recv)
```

### process_count()
Возвращает количество текущих запущенных процессов
```python
import psutil

process_count = psutil.process_count()
print("Количество запущенных процессов:", process_count)
```
