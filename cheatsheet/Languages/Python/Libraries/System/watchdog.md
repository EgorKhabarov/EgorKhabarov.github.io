`watchdog` Python-библиотека для мониторинга изменений в файловой системе
Она позволяет отслеживать создание, удаление, модификацию файлов и папок, а также их перемещение

```bash
pip install watchdog
```

| Класс / Метод                                 | Описание                                                       |
|-----------------------------------------------|----------------------------------------------------------------|
| `Observer`                                    | Основной класс для запуска наблюдения за файловой системой     |
| `Observer.schedule(handler, path, recursive)` | Назначает обработчик событий для указанного пути               |
| `Observer.start()`                            | Запускает наблюдение                                           |
| `Observer.stop()`                             | Останавливает наблюдение                                       |
| `Observer.join()`                             | Блокирует поток до завершения наблюдения                       |
| `FileSystemEventHandler`                      | Базовый класс для создания обработчиков событий                |
| `on_created(event)`                           | Вызывается при создании файла или директории                   |
| `on_deleted(event)`                           | Вызывается при удалении файла или директории                   |
| `on_modified(event)`                          | Вызывается при изменении файла или директории                  |
| `on_moved(event)`                             | Вызывается при перемещении/переименовании файла или директории |
| `LoggingEventHandler`                         | Встроенный обработчик для логирования всех событий             |
| `PatternMatchingEventHandler`                 | Обработчик событий с поддержкой фильтрации по шаблонам         |
| `ignore_patterns`                             | Список шаблонов, которые нужно игнорировать                    |
| `patterns`                                    | Список шаблонов для отслеживания (например, `["*.txt"]`)       |

### Наблюдение за папкой

```python
import time

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


class MyHandler(FileSystemEventHandler):
    def on_created(self, event):
        print(f"Создан: {event.src_path}")

    def on_deleted(self, event):
        print(f"Удален: {event.src_path}")

    def on_modified(self, event):
        print(f"Изменен: {event.src_path}")

    def on_moved(self, event):
        print(f"Перемещен: {event.src_path} -> {event.dest_path}")


path = "./watch_folder"
event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler, path, recursive=True)
observer.start()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()
observer.join()
```

### Логирование изменений в папке
```python
import time

from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler


path = "./watch_folder"
event_handler = LoggingEventHandler()
observer = Observer()
observer.schedule(event_handler, path, recursive=True)
observer.start()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()
observer.join()
```

### Использование фильтров с `PatternMatchingEventHandler`
```python
import time

from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler


class MyHandler(PatternMatchingEventHandler):
    def __init__(self):
        super().__init__(patterns=["*.txt"], ignore_patterns=["*.log"], ignore_directories=False)

    def on_created(self, event):
        print(f"Текстовый файл создан: {event.src_path}")


path = "./watch_folder"
event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler, path, recursive=True)
observer.start()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()
observer.join()
```

### Отслеживание изменений в нескольких папках
```python
import time

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        print(f"Изменен: {event.src_path}")


paths = ["./folder1", "./folder2"]
observer = Observer()

for path in paths:
    observer.schedule(MyHandler(), path, recursive=True)

observer.start()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()
observer.join()
```

### Обработка больших директорий с буферизацией
```python
import time

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


class BufferedHandler(FileSystemEventHandler):
    def __init__(self):
        self.events = []

    def on_modified(self, event):
        self.events.append(f"Изменен: {event.src_path}")
        if len(self.events) >= 10:
            self.flush()

    def flush(self):
        print("\n".join(self.events))
        self.events.clear()


path = "./watch_folder"
event_handler = BufferedHandler()
observer = Observer()
observer.schedule(event_handler, path, recursive=True)
observer.start()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()
observer.join()
```

[https://habr.com/ru/articles/140649/](https://habr.com/ru/articles/140649/)
