Библиотека "netrc" в Python используется для работы с файлами .netrc, которые содержат информацию о пользователях,
паролях и хостах для автоматической аутентификации при подключении к удаленным серверам.

Методы модуля "netrc":
`netrc.netrc(file)` - создает объект, представляющий файл .netrc.
`netrc.hosts()` - возвращает список имен хостов из файла .netrc.
`netrc.host(host)` - возвращает объект, представляющий информацию о конкретном хосте.
`netrc.authenticators(host)` - возвращает кортеж с именем пользователя, паролем и аутентификационным методом для указанного хоста.

Самые часто используемые методы:
`netrc.hosts()` - возвращает список хостов из файла .netrc.
`netrc.authenticators(host)` - возвращает информацию об аутентификации для указанного хоста.


`netrc.authenticators(host)`:

```python
import netrc

def get_credentials(hostname):
    credentials = netrc.netrc()
    auth = credentials.authenticators(hostname)
    if auth:
        username, _, password = auth
        return username, password
    else:
        return None

hostname = "example.com"
credentials = get_credentials(hostname)
if credentials:
    username, password = credentials
    print(f"Authenticated on {hostname} with username: {username} and password: {password}")
else:
    print(f"No credentials found for {hostname}")
```
