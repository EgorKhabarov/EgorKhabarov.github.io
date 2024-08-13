<p>Библиотека "netrc" в Python используется для работы с файлами .netrc, которые содержат информацию о пользователях,
паролях и хостах для автоматической аутентификации при подключении к удаленным серверам.</p>
<p>Методы модуля "netrc":
<code>netrc.netrc(file)</code> - создает объект, представляющий файл .netrc.
<code>netrc.hosts()</code> - возвращает список имен хостов из файла .netrc.
<code>netrc.host(host)</code> - возвращает объект, представляющий информацию о конкретном хосте.
<code>netrc.authenticators(host)</code> - возвращает кортеж с именем пользователя, паролем и аутентификационным методом для указанного хоста.</p>
<p>Самые часто используемые методы:
<code>netrc.hosts()</code> - возвращает список хостов из файла .netrc.
<code>netrc.authenticators(host)</code> - возвращает информацию об аутентификации для указанного хоста.</p>
<p><code>netrc.authenticators(host)</code>:</p>
<pre><code class="language-python">import netrc

def get_credentials(hostname):
    credentials = netrc.netrc()
    auth = credentials.authenticators(hostname)
    if auth:
        username, _, password = auth
        return username, password
    else:
        return None

hostname = &quot;example.com&quot;
credentials = get_credentials(hostname)
if credentials:
    username, password = credentials
    print(f&quot;Authenticated on {hostname} with username: {username} and password: {password}&quot;)
else:
    print(f&quot;No credentials found for {hostname}&quot;)
</code></pre>