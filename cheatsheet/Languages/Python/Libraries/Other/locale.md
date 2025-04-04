Библиотека "locale" в Python используется для обработки локализации и форматирования числовых
датовых и строковых значений в соответствии с настройками локали операционной системы

|                                    |                                                                                                                  |
|------------------------------------|------------------------------------------------------------------------------------------------------------------|
| `setlocale(category, locale=None)` | устанавливает текущую локаль для данной категории (категории определяют тип данных, например, числа, даты и др.) |

Подмодуль `localeconv`

|                |                                                                                 |
|----------------|---------------------------------------------------------------------------------|
| `localeconv()` | возвращает словарь с настройками форматирования чисел и валюты в текущей локали |

### setlocale(category, locale=None)
Этот метод позволяет установить локаль для определенной категории.
Например, `setlocale(locale.LC_NUMERIC, "en_US")` устанавливает локаль для чисел на английский (США).


```python
import locale

locale.setlocale(locale.LC_NUMERIC, "en_US")
formatted_number = locale.format_string("%.2f", 1234.5678)
print(formatted_number)
# 1,234.57
```
