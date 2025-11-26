Библиотека io в Python предоставляет возможности работы с потоками ввода-вывода

io.StringIO() - создание в памяти строкового потока

```python
import io

stream = io.StringIO()
stream.write("Hello, world!")
stream.seek(0)
print(stream.read())  # Hello, world!
```

io.BytesIO() - создание в памяти потока байт

```python
import io

stream = io.BytesIO()
stream.write(b"Hello, world!")
stream.seek(0)
print(stream.read())  # b"Hello, world!"
```

io.open() - открытие файла в нужном режиме

```python
import io

with io.open("example.txt", "w") as file:
    file.write("Hello, world!")

with io.open("example.txt", "r") as file:
    print(file.read())  # Hello, world!
```

io.TextIOWrapper() - обертка для текстовых потоков

```python
import io

with io.open("example.txt", "w") as file:
    wrapper = io.TextIOWrapper(file, encoding="utf-8")
    wrapper.write("Привет, мир!")

with io.open("example.txt", "r") as file:
    wrapper = io.TextIOWrapper(file, encoding="utf-8")
    print(wrapper.read())  # Привет, мир!
```

io.BufferedWriter() - буферизированный записывающий поток

```python
import io

with io.open("example.txt", "wb") as file:
    writer = io.BufferedWriter(file)
    writer.write(b"Hello, world!")

with io.open("example.txt", "rb") as file:
    reader = io.BufferedReader(file)
    print(reader.read())  # b"Hello, world!"
```

io.BufferedReader() - буферизированный читающий поток

```python
import io

with io.open("example.txt", "wb") as file:
    file.write(b"Hello, world!")

with io.open("example.txt", "rb") as file:
    reader = io.BufferedReader(file)
    print(reader.read())  # b"Hello, world!"
```

io.FileIO() - создание потока для работы с файлом в бинарном режиме

```python
import io

with io.FileIO("example.txt", "w") as file:
    file.write(b"Hello, world!")

with io.FileIO("example.txt", "r") as file:
    print(file.read())  # b"Hello, world!"
```

io.TextIOBase() - базовый класс для всех текстовых потоков

```python
import io

class UpperTextIO(io.TextIOBase):
    def __init__(self, stream):
        self._stream = stream

    def write(self, text):
        self._stream.write(text.upper())

with io.open("example.txt", "w") as file:
    wrapper = io.TextIOWrapper(file, encoding="utf-8")
    upper_wrapper = UpperTextIO(wrapper)
    upper_wrapper.write("hello, world!")
    wrapper.flush()

with io.open("example.txt", "r") as file:
    wrapper = io.TextIOWrapper(file, encoding="utf-8")
    print(wrapper.read())  # HELLO, WORLD!
```

io.StringIO.getvalue() - получение содержимого из строкового потока

```python
import io

stream = io.StringIO()
stream.write("Hello, world!")
print(stream.getvalue())  # Hello, world!
```

io.BytesIO.getvalue() - получение содержимого из потока байт

```python
import io

stream = io.BytesIO()
stream.write(b"Hello, world!")
print(stream.getvalue())  # b"Hello, world!"
```

io.TextIOWrapper.detach() - отсоединение потока от обертки

```python
import io

with io.open("example.txt", "w") as file:
    wrapper = io.TextIOWrapper(file, encoding="utf-8")
    wrapper.write("Hello, world!")
    stream = wrapper.detach()
    stream.write(b"!!!")

with io.open("example.txt", "r") as file:
    wrapper = io.TextIOWrapper(file, encoding="utf-8")
    print(wrapper.read())  # Hello, world!!!
```

io.BufferedRandom() - буферизированный поток с произвольным доступом

```python
import io

with io.open("example.txt", "wb") as file:
    writer = io.BufferedRandom(file)
    writer.write(b"Hello, world!")
    writer.flush()
    writer.seek(-6, io.SEEK_CUR)
    writer.write(b"Python!")

with io.open("example.txt", "rb") as file:
    reader = io.BufferedReader(file)
    print(reader.read())  # b"Hello, Python!"
```
