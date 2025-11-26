Библиотека `lzma` в Python используется для сжатия и распаковки данных с использованием алгоритма сжатия `LZMA` (Lempel-Ziv-Markov chain Algorithm)

|                                                                                   |                                                                                |
|-----------------------------------------------------------------------------------|--------------------------------------------------------------------------------|
| `lzma.compress(data, format=lzma.FORMAT_XZ, check=-1)`                            | Сжимает данные, используя алгоритм сжатия `LZMA`                               |
| `lzma.decompress(data, format=lzma.FORMAT_XZ, memlimit=None, filters=None)`       | Распаковывает сжатые данные, сжатые с использованием алгоритма `LZMA`          |
| `lzma.LZMACompressor(format=lzma.FORMAT_XZ, check=-1, preset=None, filters=None)` | Создает объект компрессора `LZMA` для сжатия данных                            |
| `lzma.LZMADecompressor(format=lzma.FORMAT_XZ, memlimit=None, filters=None)`       | Создает объект декомпрессора `LZMA` для распаковки сжатых данных               |
| `lzma.is_check_supported(check)`                                                  | Проверяет, поддерживается ли заданный тип проверки сжатия                      |
| `lzma.CHECK_NONE`                                                                 | Константа, представляющая отсутствие проверки сжатия                           |
| `lzma.CHECK_CRC32`                                                                | Константа, представляющая проверку сжатия с использованием алгоритма `CRC32`   |
| `lzma.CHECK_CRC64`                                                                | Константа, представляющая проверку сжатия с использованием алгоритма `CRC64`   |
| `lzma.CHECK_SHA256`                                                               | Константа, представляющая проверку сжатия с использованием алгоритма `SHA-256` |

### lzma.compress(data)
Сжимает данные, используя алгоритм сжатия LZMA
```python
import lzma

data = b"Hello, World!"
compressed_data = lzma.compress(data)
```

### lzma.decompress(data)
Распаковывает сжатые данные, сжатые с использованием алгоритма `LZMA`
```python
import lzma

compressed_data = b"\xfd7zXZ\x00\x00\x04\xe6\xd6\xb4\x46\x02\x00!\x01\x16\x00\x00\x00t/\xe5\xfd\x01\x00\x00\x00\xff\xff"
decompressed_data = lzma.decompress(compressed_data)
```
