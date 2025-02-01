Библиотека "gettext" в Python используется для локализации и перевода текстовых сообщений в программе

# gettext
## gettext

|                                          |                                                                 |
|------------------------------------------|-----------------------------------------------------------------|
| `bindtextdomain(domain, directory)`      | Устанавливает домен и директорию для поиска файлов перевода     |
| `dgettext(domain, message)`              | Возвращает перевод сообщения из указанного домена               |
| `dngettext(domain, singular, plural, n)` | Возвращает перевод множественного сообщения на основе числа `n` |
| `gettext(message)`                       | Возвращает перевод сообщения                                    |
| `ngettext(singular, plural, n)`          | Возвращает перевод множественного сообщения на основе числа `n` |
| `textdomain(domain)`                     | Устанавливает текущий домен перевода                            |

## gettext.translation

|                                                                               |                                                                             |
|-------------------------------------------------------------------------------|-----------------------------------------------------------------------------|
| `gettext.translation(domain, localedir=None, languages=None, fallback=False)` | Создает объект перевода на основе заданного домена и директории локализации |
| `gettext.translation("")`                                                     | Возвращает объект перевода для текущего домена                              |
| `add_fallback(translations)`                                                  | Добавляет объект перевода в список резервных вариантов перевода             |
| `install(domain, localedir=None, unicode=0)`                                  | Устанавливает объект перевода в качестве текущего                           |

Самые часто используемые методы библиотеки "gettext" вместе с их кратким описанием и примером кода

### gettext
Возвращает перевод сообщения
```python
import gettext
gettext.bindtextdomain("mydomain", "locale/")
gettext.textdomain("mydomain")

_ = gettext.gettext
print(_("Hello, world!"))
```

### ngettext
Возвращает перевод множественного сообщения на основе числа n
```python
import gettext
gettext.bindtextdomain("mydomain", "locale/")
gettext.textdomain("mydomain")

_ = gettext.ngettext
print(_("%d apple", "%d apples", 5) % 5)
```

### dgettext
Возвращает перевод сообщения из указанного домена
```python
import gettext
gettext.bindtextdomain("mydomain", "locale/")
gettext.textdomain("mydomain")

_ = gettext.dgettext
print(_("mydomain", "Hello, world!"))
```
