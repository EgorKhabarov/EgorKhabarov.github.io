Библиотека "gettext" в Python используется для локализации и перевода текстовых сообщений в программе.

# Таблица методов модуля "gettext" и его подмодулей
### Методы модуля "gettext"
bindtextdomain(domain, directory): устанавливает домен и директорию для поиска файлов перевода.
dgettext(domain, message): возвращает перевод сообщения из указанного домена.
dngettext(domain, singular, plural, n): возвращает перевод множественного сообщения на основе числа n.
gettext(message): возвращает перевод сообщения.
ngettext(singular, plural, n): возвращает перевод множественного сообщения на основе числа n.
textdomain(domain): устанавливает текущий домен перевода.

### Методы подмодуля "gettext.translation"
gettext.translation(domain, localedir=None, languages=None, fallback=False): создает объект перевода на основе заданного домена и директории локализации.
gettext.translation(""): возвращает объект перевода для текущего домена.
add_fallback(translations): добавляет объект перевода в список резервных вариантов перевода.
install(domain, localedir=None, unicode=0): устанавливает объект перевода в качестве текущего.

Самые часто используемые методы библиотеки "gettext" вместе с их кратким описанием и примером кода:

gettext(message): Возвращает перевод сообщения.

```python
import gettext
gettext.bindtextdomain("mydomain", "locale/")
gettext.textdomain("mydomain")

_ = gettext.gettext
print(_("Hello, world!"))
```

ngettext(singular, plural, n): Возвращает перевод множественного сообщения на основе числа n.

```python
import gettext
gettext.bindtextdomain("mydomain", "locale/")
gettext.textdomain("mydomain")

_ = gettext.ngettext
print(_("%d apple", "%d apples", 5) % 5)
```

dgettext(domain, message): Возвращает перевод сообщения из указанного домена.

```python
import gettext
gettext.bindtextdomain("mydomain", "locale/")
gettext.textdomain("mydomain")

_ = gettext.dgettext
print(_("mydomain", "Hello, world!"))
```
