Модуль contextlib - это стандартная библиотека Python, который содержит утилиты для работы с контекстными менеджерами
Контекстные менеджеры могут использоваться, например, для управления ресурсами, такими как файлы или сетевые соединения

### contextmanager
Декоратор превращает генераторную функцию в контекстный менеджер
Генератор должен содержать точку входа и выхода из контекста

```python
import contextlib

@contextlib.contextmanager
def my_context():
    print("Entering context")
    yield
    print("Exiting context")

with my_context():
    print("Inside context")
```

В этом примере `my_context()` - это контекстный менеджер, который выводит сообщения при входе и выходе из контекста



### suppress
это контекстный менеджер, который подавляет указанные исключения
Он используется, когда вы хотите, чтобы программа продолжала работать даже при возникновении определенных ошибок


```python
import contextlib

with contextlib.suppress(FileNotFoundError):
    with open("non_existent_file.txt", "r") as f:
        print(f.read())
```

В этом примере `suppress` используется для подавления исключения `FileNotFoundError`, которое возникает, если файл `non_existent_file.txt` не найден
Вместо того, чтобы возбудить исключение, программа продолжит работу без выполнения блока кода внутри `with` выражения


### redirect_stdout и redirect_stderr
эти контекстные менеджеры перенаправляют стандартный вывод и стандартный вывод ошибок соответственно в файл или объект

```python
import contextlib
import io

with io.StringIO() as output:
    with contextlib.redirect_stdout(output):
        print("Hello, world!")
    contents = output.getvalue()

print(contents)
```

В этом примере стандартный вывод перенаправляется в объект `io.StringIO()`, а затем содержимое этого объекта выводится на экран

Модуль `contextlib` содержит и другие функции, такие как closing, `nullcontext` и `ExitStack`
Они все предназначены для упрощения работы с контекстными менеджерами в Python










### closing
Это функция, которая превращает объект с методом `close()` в контекстный менеджер
Это может быть полезно, например, для работы с файлами или соединениями

```python
import contextlib
from urllib.request import urlopen

with contextlib.closing(urlopen("https:&sol;&sol;www.example.com/")) as page:
    for line in page:
        print(line.decode("utf-8"))
```

В этом примере `urlopen("https://www.example.com/")` возвращает объект с методом `close()`, который используется внутри контекстного менеджера `closing`



### nullcontext
Это класс, который предоставляет пустой контекстный менеджер, который не делает ничего
Он может быть использован, когда нужен контекстный менеджер, но никакой реальной работы в контексте выполнять не требуется

```python
import contextlib

with contextlib.nullcontext():
    print("Hello, world!")
```

В этом примере ничего не происходит в контексте, но благодаря использованию `nullcontext`, код работает корректно в рамках контекстного менеджера


### ExitStack
Это класс, который предоставляет возможность управления несколькими контекстными менеджерами одновременно
Он может быть использован, когда требуется обеспечить надежное управление ресурсами в случае, когда ресурсы могут быть открыты и закрыты в произвольном порядке

```python
import contextlib

with contextlib.ExitStack() as stack:
    files = [stack.enter_context(open(f)) for f in ["file1.txt", "file2.txt", "file3.txt"]]
    for file in files:
        print(file.readline())
```

В этом примере `ExitStack` используется для управления тремя файлами, которые могут быть открыты и закрыты в любом порядке
Функция `stack.enter_context(open(f))` добавляет каждый файл в стек контекстных менеджеров, который гарантирует их правильное закрытие в конце работы с ними
