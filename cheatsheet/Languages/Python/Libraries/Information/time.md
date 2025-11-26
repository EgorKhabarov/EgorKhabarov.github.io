# time

| Функция                         | Описание                                                                                                             | Пример использования                                           |
|---------------------------------|----------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------|
| `time.time()`                   | Возвращает текущее время в секундах с эпохи (`01.01.1970 00:00:00 UTC`)                                              | `time.time()`                                                  |
| `time.sleep(seconds)`           | Останавливает выполнение программы на указанное количество секунд                                                    | `time.sleep(1.5)`                                              |
| `time.ctime([secs])`            | Преобразует время (в секундах с эпохи) в удобочитаемую строку.<br>Если `secs` не указано, используется текущее время | `time.ctime()`                                                 |
| `time.gmtime([secs])`           | Преобразует время (в секундах с эпохи)<br>в структуру `struct_time` в формате UTC                                    | `time.gmtime()`                                                |
| `time.localtime([secs])`        | Преобразует время (в секундах с эпохи)<br>в структуру `struct_time` для текущего часового пояса                      | `time.localtime()`                                             |
| `time.mktime(t)`                | Преобразует объект `struct_time` обратно в секунды с эпохи                                                           | `time.mktime(time.localtime())`                                |
| `time.strftime(format, t)`      | Преобразует `struct_time` в строку по указанному формату                                                             | `time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())`         |
| `time.strptime(string, format)` | Парсит строку времени в объект `struct_time` на основе заданного формата                                             | `time.strptime("2024-12-25", "%Y-%m-%d")`                      |
| `time.perf_counter()`           | Возвращает высокоточный таймер для измерения временных интервалов                                                    | `start = time.perf_counter()`<br>`time.perf_counter() - start` |
| `time.process_time()`           | Возвращает процессорное время выполнения текущего процесса                                                           | `time.process_time()`                                          |
| `time.monotonic()`              | Возвращает значение монотонного таймера (всегда возрастает)                                                          | `time.monotonic()`                                             |
| `time.thread_time()`            | Возвращает процессорное время потока                                                                                 | `time.thread_time()`                                           |

## Таблица констант

| Константа       | Описание                                                                         |
|-----------------|----------------------------------------------------------------------------------|
| `time.timezone` | Смещение текущего часового пояса в секундах от UTC (для стандартного времени)    |
| `time.altzone`  | Смещение текущего часового пояса в секундах от UTC (для летнего времени)         |
| `time.daylight` | Показывает, используется ли переход на летнее время (1 - да, 0 - нет)            |
| `time.tzname`   | Кортеж строк с названиями стандартного и летнего времени, например, `(UTC, BST)` |

# Примеры

### Таймер выполнения
```python
import time
start = time.perf_counter()
time.sleep(2)  # Задержка на 2 секунды
end = time.perf_counter()
print(f"{end - start:.2f}")
```

### Форматирование времени
```python
import time
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
```

### Парсинг строки времени
```pycon
>>> import time
>>> print(time.strptime("2024-12-25", "%Y-%m-%d"))
time.struct_time(tm_year=2024, tm_mon=12, tm_mday=25, tm_hour=0, tm_min=0, tm_sec=0, tm_wday=2, tm_yday=360, tm_isdst=-1)
```

### Работа с UTC и локальным временем
```python
import time
print("UTC:", time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime()))
print("Local:", time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
```
