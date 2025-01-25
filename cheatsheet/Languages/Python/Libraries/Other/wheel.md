Библиотека "wheel" в Python используется для упрощения установки пакетов и их распространения.
Она представляет собой формат пакета, который содержит предварительно
скомпилированные бинарные файлы, что позволяет ускорить процесс установки.

### Методы модуля "wheel"
`convert`: используется для преобразования исходных файлов пакета в формат wheel.
`install`: позволяет установить пакет из wheel-файла.
`unpack`: распаковывает содержимое wheel-файла.
`pack`: упаковывает исходные файлы пакета в wheel-файл.

### Подмодули
`metadata`: содержит методы для работы с метаданными пакета, такими как версия, автор и описание.
`tags`: предоставляет информацию о поддерживаемых платформах и интерпретаторах.
`signatures`: позволяет работать с подписями wheel-файлов.
`pep425tags`: предоставляет методы для работы с тегами PEP 425,
которые описывают совместимость пакетов с определенными версиями Python и операционных систем.


### convert
Преобразует исходные файлы пакета в формат wheel.

```python
from wheel import convert

convert.pack("path/to/source/package")
```

### install
Устанавливает пакет из wheel-файла.

```python
from wheel import install

install.install("path/to/wheel/file.whl")
```

### unpack
Распаковывает содержимое wheel-файла.

```python
from wheel import unpack

unpack.unpack("path/to/wheel/file.whl", "path/to/destination")
```

### pack</h3>
Упаковывает исходные файлы пакета в wheel-файл.

```python
from wheel import pack

pack.pack("path/to/source/package", "path/to/destination/file.whl")
```
