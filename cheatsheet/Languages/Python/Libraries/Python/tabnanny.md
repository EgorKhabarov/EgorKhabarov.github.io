Модуль tabnanny в Python используется для проверки исходных файлов
на наличие проблем с табуляцией, которые могут вызвать синтаксические ошибки.

| Метод                  | Описание                                              |
|------------------------|-------------------------------------------------------|
| process_tokens(tokens) | Проверяет токены файла на проблемы с табуляцией       |
| NannyToken(token)      | Конструктор класса токенов, используемый для проверки |

**process_tokens(tokens)** Проверяет токены файла на наличие проблем с табуляцией.

```python
import tokenize
from tabnanny import process_tokens

with open("file.py", "rb") as f:
    process_tokens(tokenize.generate_tokens(f.readline))
```
