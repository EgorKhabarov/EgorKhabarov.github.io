Библиотека `subprocess` в Python используется для запуска новых процессов, выполнения команд в системе,
а также для управления стандартными потоками ввода, вывода и ошибок.
Эта библиотека предоставляет мощный интерфейс для взаимодействия с внешними процессами.

# Основные функции

| Функция                        | Описание                                                                                                          | Пример использования                                   |
|--------------------------------|-------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------|
| `subprocess.run()`             | Выполняет команду, ожидает завершения процесса<br>и возвращает результат в виде объекта `CompletedProcess`        | `result = subprocess.run(["ls", "-l"])`                |
| `subprocess.Popen()`           | Запускает новый процесс и возвращает объект `Popen`,<br>который можно использовать для взаимодействия с процессом | `process = subprocess.Popen(["ls", "-l"])`             |
| `subprocess.call()`            | Выполняет команду и возвращает код завершения процесса                                                            | `return_code = subprocess.call(["ls", "-l"])`          |
| `subprocess.check_call()`      | Выполняет команду и вызывает исключение,<br>если процесс завершился с ошибкой                                     | `subprocess.check_call(["ls", "-l"])`                  |
| `subprocess.check_output()`    | Выполняет команду и возвращает её вывод.<br>Если процесс завершился с ошибкой, вызывается исключение              | `output = subprocess.check_output(["ls", "-l"])`       |
| `subprocess.getoutput()`       | Выполняет команду и возвращает её вывод в виде строки.<br>Удобно для команд, не требующих сложного взаимодействия | `output = subprocess.getoutput("ls -l")`               |
| `subprocess.getstatusoutput()` | Выполняет команду и возвращает кортеж (код завершения, вывод)                                                     | `status, output = subprocess.getstatusoutput("ls -l")` |

## Класс Popen

| Метод                 | Описание                                                                                                   | Пример использования                               |
|-----------------------|------------------------------------------------------------------------------------------------------------|----------------------------------------------------|
| `Popen.poll()`        | Проверяет завершился ли процесс.<br>Возвращает код завершения или `None`, если процесс ещё выполняется     | `status = process.poll()`                          |
| `Popen.wait()`        | Ожидает завершения процесса и возвращает код завершения                                                    | `return_code = process.wait()`                     |
| `Popen.communicate()` | Отправляет данные на стандартный ввод процесса<br>и получает данные из стандартного вывода и вывода ошибок | `stdout, stderr = process.communicate(input_data)` |
| `Popen.terminate()`   | Посылает процессу сигнал `SIGTERM`, запрашивая его завершение                                              | `process.terminate()`                              |
| `Popen.kill()`        | Принудительно завершает процесс, посылая сигнал `SIGKILL`                                                  | `process.kill()`                                   |
| `Popen.stdin`         | Стандартный поток ввода процесса (если установлен `stdin=subprocess.PIPE`)                                 | `process.stdin.write(b"data")`                     |
| `Popen.stdout`        | Стандартный поток вывода процесса (если установлен `stdout=subprocess.PIPE`)                               | `output = process.stdout.read()`                   |
| `Popen.stderr`        | Стандартный поток ошибок процесса (если установлен `stderr=subprocess.PIPE`)                               | `error_output = process.stderr.read()`             |

## Управление потоками ввода-вывода

Пример взаимодействия с процессом через потоки ввода-вывода:

```python
import subprocess

process = subprocess.Popen(
    ["grep", "pattern"],
    stdin=subprocess.PIPE,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE
)

stdout, stderr = process.communicate(input=b"text\npattern\nanother line\n")
print(stdout.decode())  # "pattern\n"
```

# Примеры использования

### Простой запуск команды
```python
import subprocess

subprocess.run(["ls", "-l"])
```

### Получение вывода команды
```python
import subprocess

print(subprocess.check_output(["echo", "Hello, World!"]).decode())  # "Hello, World!\n"
```

### Проверка кода завершения
```python
import subprocess

try:
  subprocess.check_call(["false"])
except subprocess.CalledProcessError as e:
  print(f"Процесс завершился с ошибкой: {e.returncode}")
```

### Запуск процесса с передачей данных на ввод
```python
import subprocess

process = subprocess.Popen(["cat"], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
stdout, _ = process.communicate(input=b"Hello, World!\n")
print(stdout.decode())  # "Hello, World!\n"
```

# Исключения

| Исключение                      | Описание                                                                                       |
|---------------------------------|------------------------------------------------------------------------------------------------|
| `subprocess.CalledProcessError` | Вызывается, если процесс завершился с ненулевым кодом возврата                                 |
| `subprocess.TimeoutExpired`     | Вызывается, если процесс не завершился в течение указанного времени (используется с `timeout`) |
| `subprocess.SubprocessError`    | Базовое исключение для всех исключений, связанных с `subprocess`                               |

# Полезные параметры

| Параметр             | Описание                                                                                                                            |
|----------------------|-------------------------------------------------------------------------------------------------------------------------------------|
| `stdin`              | Определяет источник стандартного ввода процесса (например, `subprocess.PIPE`, `None`, или файловый объект)                          |
| `stdout`             | Определяет место, куда будет направлен стандартный вывод процесса (например, `subprocess.PIPE`, `None`, или файловый объект)        |
| `stderr`             | Определяет место, куда будет направлен стандартный поток ошибок процесса (например, `subprocess.PIPE`, `None`, или файловый объект) |
| `shell`              | Если `True`, команда будет выполнена через оболочку (shell). Будьте осторожны, так как это может быть небезопасно                   |
| `cwd`                | Устанавливает текущий рабочий каталог для процесса                                                                                  |
| `env`                | Определяет переменные окружения для процесса                                                                                        |
| `universal_newlines` | Если `True`, ввод-вывод будет интерпретироваться как текст (строки), а не байты                                                     |
| `timeout`            | Определяет максимальное время ожидания завершения процесса, после чего будет вызвано исключение `TimeoutExpired`                    |

# Советы по безопасности

1. **Избегайте использования `shell=True`**, особенно с данными, полученными от пользователя, так как это может привести к уязвимостям типа `shell injection`.
2. **Используйте абсолютные пути** к командам для повышения безопасности и предсказуемости поведения скрипта.
3. **Управляйте таймаутами** для долгих процессов с помощью параметра `timeout`.

# Полезные ссылки

- [Официальная документация](https://docs.python.org/3/library/subprocess.html)
- [Real Python - Guide to Subprocess](https://realpython.com/python-subprocess/)
