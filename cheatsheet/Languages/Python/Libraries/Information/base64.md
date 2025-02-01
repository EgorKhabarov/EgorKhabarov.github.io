Библиотека `base64` в Python используется для кодирования и декодирования данных в формате `base64`
`Base64` является способом представления двоичных данных в виде текста, что удобно для передачи и хранения данных,
которые не могут быть безопасно переданы в обычном двоичном формате

|                  |                                                                                   |
|------------------|-----------------------------------------------------------------------------------|
| `b64encode`      | Кодирует данные в формате `base64`                                                |
| `b64decode`      | Декодирует данные из формата `base64`                                             |
| `b64encodebytes` | Кодирует данные в формате `base64` и возвращает байтовую строку                   |
| `b64decodebytes` | Декодирует байтовую строку из формата `base64` и возвращает декодированные данные |

Подмодуль `base64.urlsafe`

|                   |                                                                                                                  |
|-------------------|------------------------------------------------------------------------------------------------------------------|
| urlsafe_b64encode | Кодирует данные в формате `base64` для `URL` без использования символов, которые могут вызывать проблемы в `URL` |
| urlsafe_b64decode | Декодирует данные из формата `base64` для `URL`                                                                  |

### b64encode
Кодирует данные в формате `base64`
```python
import base64

data = b"Hello, World!"
encoded_data = base64.b64encode(data)
print(encoded_data)
```

### b64decode
Декодирует данные из формата base64
```python
import base64

encoded_data = b"SGVsbG8sIFdvcmxkIQ=="
decoded_data = base64.b64decode(encoded_data)
print(decoded_data)
```

### urlsafe_b64encode
Кодирует данные в формате base64 для `URL` без использования символов, которые могут вызывать проблемы в `URL`
```python
import base64

data = b"Hello, World!"
encoded_data = base64.urlsafe_b64encode(data)
print(encoded_data)
```

### urlsafe_b64decode
Декодирует данные из формата base64 для URL
```python
import base64

encoded_data = b"SGVsbG8sIFdvcmxkIQ=="
decoded_data = base64.urlsafe_b64decode(encoded_data)
print(decoded_data)
```
