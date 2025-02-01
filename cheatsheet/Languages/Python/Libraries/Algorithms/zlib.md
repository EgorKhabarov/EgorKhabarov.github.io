Библиотека `zlib` используется в Python для сжатия и распаковки данных с использованием алгоритма сжатия `Deflate`

|                                                           |                                                     |
|-----------------------------------------------------------|-----------------------------------------------------|
| `compress(data, level=-1)`                                | Сжимает данные с использованием алгоритма `Deflate` |
| `decompress(data, wbits=MAX_WBITS, bufsize=DEF_BUF_SIZE)` | Распаковывает сжатые данные                         |
| `crc32(data, value=0)`                                    | Вычисляет контрольную сумму `CRC-32` для данных     |

# zlib.compressobj

|                                                                                                                 |                                                       |
|-----------------------------------------------------------------------------------------------------------------|-------------------------------------------------------|
| `\_\_init\_\_(level=-1, method=DEFLATED, wbits=MAX_WBITS, memLevel=DEF_MEM_LEVEL, strategy=Z_DEFAULT_STRATEGY)` | Создает объект для сжатия данных                      |
| `compress(data)`                                                                                                | Сжимает данные и возвращает сжатый буфер              |
| `flush(mode)`                                                                                                   | Завершает сжатие и возвращает оставшийся сжатый буфер |

# zlib.decompressobj

|                                  |                                                                  |
|----------------------------------|------------------------------------------------------------------|
| `\_\_init\_\_(wbits=MAX_WBITS)`  | Создает объект для распаковки данных                             |
| `decompress(data, max_length=0)` | Распаковывает данные и возвращает распакованный буфер            |
| `flush(mode)`                    | Завершает распаковку и возвращает оставшийся распакованный буфер |

### compress(data, level=-1)
Сжимает данные с использованием алгоритма Deflate
```python
import zlib
compressed_data = zlib.compress(b"Hello, world!")
```

### decompress(data, wbits=MAX_WBITS, bufsize=DEF_BUF_SIZE)
Распаковывает сжатые данные
```python
import zlib
decompressed_data = zlib.decompress(compressed_data)
```

### crc32(data, value=0)
Вычисляет контрольную сумму CRC-32 для данных
```python
import zlib
checksum = zlib.crc32(b"Hello, world!")
```
