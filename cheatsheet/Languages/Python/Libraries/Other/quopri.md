Библиотека "quopri" в Python используется для кодирования и декодирования данных в формате Quoted-Printable
Quoted-Printable - это способ представления непечатных или специальных символов в текстовом формате, который используется в электронной почте и других приложениях

Методы и подмодули библиотеки "quopri":

|                                                 |                                                                                               |
|-------------------------------------------------|-----------------------------------------------------------------------------------------------|
| `quopri.encode(input, output, quotetabs=False)` | кодирует входные данные в формат Quoted-Printable и записывает результат в выходной поток     |
| `quopri.decode(input, output, headers=False)`   | декодирует входные данные из формата Quoted-Printable и записывает результат в выходной поток |
| `quopri.quote(data)`                            | возвращает строку, в которой данные закодированы в формате Quoted-Printable                   |
| `quopri.unquote(data)`                          | возвращает строку, в которой данные декодированы из формата Quoted-Printable                  |
| `quopri.encodestring(s)`                        | кодирует строку в формат Quoted-Printable и возвращает результат как строку                   |
| `quopri.decodestring(s)`                        | декодирует строку из формата Quoted-Printable и возвращает результат как строку               |

Самые часто используемые методы:

### encode(input, output, quotetabs=False)
Метод для кодирования данных в формат Quoted-Printable
Можно использовать для безопасной передачи данных по электронной почте или другим каналам связи
```python
import quopri

input_data = b"Hello, world!"
encoded_data = quopri.encode(input_data)
print(encoded_data)
```

### decode(input, output, headers=False)
Метод для декодирования данных из формата Quoted-Printable
Полезно при работе с данными, полученными из электронной почты или других источников, где данные могут быть закодированы в этом формате
```python
import quopri

encoded_data = b"Hello=2C=20world=21"
decoded_data = quopri.decode(encoded_data)
print(decoded_data)
```
