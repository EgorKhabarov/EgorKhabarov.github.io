Библиотека "logging" в Python используется для добавления логирования,
то есть записи информации о работе программы, чтобы отслеживать ее выполнение и находить ошибки или проблемы.

Методы модуля "logging" и его подмодулей:

`getLogger()`: Возвращает объект логгера для указанного имени.
`basicConfig()`: Конфигурирует логгинг с использованием базовых параметров.
`Logger.setLevel()`: Устанавливает уровень логгирования для указанного логгера.
`Logger.addHandler()`: Добавляет обработчик к указанному логгеру.
`Formatter.format()`: Форматирует записи логгера в определенном формате.
`StreamHandler`: Обработчик, который выводит сообщения логгера в поток (например, на консоль).
`FileHandler`: Обработчик, который выводит сообщения логгера в файл.
`RotatingFileHandler`: Обработчик, который выводит сообщения логгера в файл с возможностью
автоматического поворота лог-файла при достижении определенного размера или количества записей.

Наиболее часто используемые методы:

`logging.debug()`: Регистрирует отладочное сообщение.

```python
import logging
logging.debug("This is a debug message")
```

`logging.info()`: Регистрирует информационное сообщение.

```python
import logging
logging.info("This is an info message")
```

`logging.warning()`: Регистрирует предупреждение.

```python
import logging
logging.warning("This is a warning message")
```

`logging.error()`: Регистрирует сообщение об ошибке.

```python
import logging
logging.error("This is an error message")
```

`logging.critical()`: Регистрирует критическое сообщение.

```python
import logging
logging.critical("This is a critical message")
```




import logging

Запись в файл

```python
logging.basicConfig(filename="example.log",
                    level=logging.DEBUG)
```

Запись в консоль

```python
logging.basicConfig(level=logging.DEBUG,
                    format="%(message)s")
```

Запись в файл и в консоль

```python
logging.basicConfig(filename="example.log",
                    level=logging.DEBUG,
                    format="%(asctime)s %(levelname)s %(message)s",
                    datefmt="%Y-%m-%d %H:%M:%S")
console = logging.StreamHandler()
console.setLevel(logging.DEBUG)
formatter = logging.Formatter("%(asctime)s "
                              "%(levelname)s "
                              "%(message)s",
                              datefmt="%Y-%m-%d %H:%M:%S")
console.setFormatter(formatter)
logging.getLogger("").addHandler(console)
```

Для самих сообщений

```
%s           строка
%d           для целых чисел
%c           для имени логгера
%f           для чисел с плавающей точкой
%r           для строковых представлений объектов
%m           для сообщения журнала
%x           целое число в шестнадцатеричной системе исчисления
%o           целое число в восьмеричной системе исчисления
%e, %E       число в экспоненциальной форме
```

Для настроек логгирования

```
%(message)s     сообщение журнала

%(asctime)s     время записи сообщения в формате (по умолчанию YYYY-MM-DD HH:MM:SS,sss настраивать в basicConfig(datefmt))
%(created)f     время записи сообщения в секундах, начиная с 1 января 1970 года

%(filename)s    имя файла, в котором был вызван логгер
%(funcName)s    имя функции, в которой был вызван логгер
%(name)s        имя логгера, который записывает сообщение
%(module)s      имя модуля, в котором был вызван логгер
%(threadName)s  имя потока, в котором был вызван логгер
%(processName)s имя процесса, в котором был вызван логгер

%(levelname)s   уровень журнала (например, DEBUG, INFO, WARNING, ERROR, CRITICAL)
%(levelno)s     уровень журнала в числовом формате (10 для DEBUG, 20 для INFO и т. д.)

%(lineno)d      номер строки, в которой был вызван логгер
%(pathname)s    полный путь к файлу, в котором был вызван логгер
%(process)d     идентификатор процесса, в котором был вызван логгер
%(thread)d      идентификатор потока, в котором был вызван логгер
```


Код для применения функций к тексту

```python
logging.info = lambda msg, *args, f=logging.info: f(Up(msg), *args)
```
