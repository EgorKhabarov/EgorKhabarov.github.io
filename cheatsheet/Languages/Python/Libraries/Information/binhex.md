Библиотека `binhex` в Python используется для преобразования двоичных данных в шестнадцатеричный формат и обратно
Она предоставляет функции для кодирования и декодирования данных, а также для чтения и записи файлов в формате `binhex`

Методы модуля `binhex` и его подмодулей

|                            |                                                                    |
|----------------------------|--------------------------------------------------------------------|
| `hexlify(data)`            | Преобразует двоичные данные в шестнадцатеричный формат             |
| `unhexlify(hexdata)`       | Преобразует данные из шестнадцатеричного формата в двоичный формат |
| `binhex(binfile, hexfile)` | Кодирует двоичный файл в файл в формате binhex                     |
| `hexbin(hexfile, binfile)` | Декодирует файл в формате binhex в двоичный файл                   |

### hexlify(data)
Преобразует двоичные данные в шестнадцатеричный формат
```python
import binhex

data = b"Hello, World!"
hex_data = binhex.hexlify(data)
print(hex_data)
```

### unhexlify(hexdata)
Преобразует данные из шестнадцатеричного формата в двоичный формат
```python
import binhex

hex_data = "48656c6c6f2c20576f726c6421"
data = binhex.unhexlify(hex_data)
print(data)
```

### binhex(binfile, hexfile)
Кодирует двоичный файл в файл в формате `binhex`
```python
import binhex

bin_file = "input.bin"
hex_file = "output.hex"
binhex.binhex(bin_file, hex_file)
```

### hexbin(hexfile, binfile)
Декодирует файл в формате `binhex` в двоичный файл
```python
import binhex

hex_file = "input.hex"
bin_file = "output.bin"
binhex.hexbin(hex_file, bin_file)
```
