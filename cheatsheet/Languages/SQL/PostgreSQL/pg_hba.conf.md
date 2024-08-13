<div class="code-element"><div class="lang-line"><text>bash</text><button class="copy-button" onclick="copyCode(this)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code"><div class="highlight"><pre><span></span>notepad<span class="w"> </span><span class="s2">&quot;C:\Program Files\PostgreSQL\16\data\pg_hba.conf&quot;</span>
</pre></div></div></div>

<div class="code-element"><div class="lang-line"><text>bash</text><button class="copy-button" onclick="copyCode(this)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code"><div class="highlight"><pre><span></span>net<span class="w"> </span>stop<span class="w"> </span>postgresql-x64-16
net<span class="w"> </span>start<span class="w"> </span>postgresql-x64-16
</pre></div></div></div>

<h1>Запись может быть сделана в одном из семи форматов:</h1>
<blockquote>
<p>local      база  пользователь  метод-аутентификации  [параметры-аутентификации]
host       база  пользователь  адрес  метод-аутентификации  [параметры-аутентификации]
hostssl    база  пользователь  адрес  метод-аутентификации  [параметры-аутентификации]
hostnossl  база  пользователь  адрес  метод-аутентификации  [параметры-аутентификации]
host       база  пользователь  IP-адрес  IP-маска  метод-аутентификации  [параметры-аутентификации]
hostssl    база  пользователь  IP-адрес  IP-маска  метод-аутентификации  [параметры-аутентификации]
hostnossl  база  пользователь  IP-адрес  IP-маска  метод-аутентификации  [параметры-аутентификации]</p>
</blockquote>
<table>
<thead>
<tr>
<th></th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>local</td>
<td>Unix-сокеты</td>
</tr>
<tr>
<td>host</td>
<td>Подключения по <code>TCP/IP</code>. С <code>SSL</code> и без <code>SSL</code>.</td>
</tr>
<tr>
<td>hostssl</td>
<td>Подключения по <code>TCP/IP</code> с применением шифрования <code>SSL</code>.</td>
</tr>
<tr>
<td>hostnossl</td>
<td>Противоположен <code>hostssl</code>. Подключения по <code>TCP/IP</code> без шифрования <code>SSL</code>.</td>
</tr>
<tr>
<td>база</td>
<td>- <code>all</code> - все базы данных<br>- <code>sameuser</code> - имя запрашиваемой базы данных совпадает с именем запрашиваемого пользователя<br>- <code>samerole</code> - запрашиваемый пользователь должен быть членом роли с таким же именем, как и у запрашиваемой базы данных.<br>  (<code>samegroup</code> — это устаревший, но допустимый вариант значения <code>samerole</code>.)<br>  Суперпользователи не становятся членами роли автоматически из-за <code>samerole</code>,<br>  а только если они являются явными членами роли, прямо или косвенно, и не только из-за того, что они суперпользователи.<br>- <code>replication</code> - если запрашивается подключение для физической репликации (для таких подключений не выбирается какая-то конкретная база данных).<br>Любое другое значение воспринимается как имя определённой базы <code>Postgres Pro</code>.<br>Несколько имён баз данных можно указать, разделяя их запятыми.<br>Файл, содержащий имена баз данных, можно указать, поставив знак <code>@</code> в начале его имени.</td>
</tr>
<tr>
<td>пользователь</td>
<td>- <code>all</code> - все пользователи.<br>  Имя группы начинается с <code>+</code>.<br>  (В <code>Postgres Pro</code> нет никакой разницы между пользователем и группой; знак + означает «совпадение любых ролей,<br>   которые прямо или косвенно являются членами роли», тогда как имя без знака <code>+</code> является подходящим только для этой конкретной роли.)<br>  Суперпользователь рассматривается как член роли, только если он явно является членом этой роли, прямо или косвенно,<br>  а не только потому, что он является суперпользователем.<br>Несколько имён пользователей можно указать, разделяя их запятыми.<br>Файл, содержащий имена пользователей, можно указать, поставив знак <code>@</code> в начале его имени.</td>
</tr>
<tr>
<td>адрес</td>
<td>ip/mask<br>- <code>all</code> - любой IP-адрес<br>- <code>samehost</code> - любые IP-адреса данного сервера- <br>- <code>samenet</code> - любой адрес любой подсети, к которой сервер подключён напрямую<br><br>Имени, начинающееся с точки (<code>.</code>), соответствует суффиксу актуального имени узла.<br>Так, <code>.example.com</code> будет соответствовать <code>foo.example.com</code> (а не только <code>example.com</code>).<br>Это поле применимо только к записям <code>host</code>, <code>hostssl</code> и <code>hostnossl</code>.</td>
</tr>
<tr>
<td>метод-аутентификации</td>
<td>- <code>trust</code> - Разрешает безусловное подключение.<br>  Этот метод позволяет тому, кто может подключиться к серверу с базой данных <code>Postgres Pro</code>,<br>  войти под любым желаемым пользователем <code>Postgres Pro</code> без введения пароля и без какой-либо другой аутентификации. <a href="https://postgrespro.ru/docs/postgrespro/10/auth-methods#AUTH-TRUST">Подробности</a><br>- <code>reject</code> - Отклоняет подключение безусловно.<br>  Полезна для «фильтрации» некоторых серверов группы, например, строка <code>reject</code> может отклонить попытку подключения одного компьютера,<br>  при этом следующая строка позволяет подключиться остальным компьютерам в той же сети.<br>- <code>scram-sha-256</code> Проверяет пароль пользователя, производя аутентификацию <code>SCRAM-SHA-256</code>. <a href="https://postgrespro.ru/docs/postgrespro/10/auth-methods#AUTH-PASSWORD">Подробности</a><br>- <code>md5</code> Проверяет пароль пользователя, производя аутентификацию <code>SCRAM-SHA-256</code> или <code>MD5</code>. <a href="https://postgrespro.ru/docs/postgrespro/10/auth-methods#AUTH-PASSWORD">Подробности</a><br>- <code>password</code> Требует для аутентификации введения клиентом незашифрованного пароля.<br>  Поскольку пароль посылается простым текстом через сеть, такой способ не стоит использовать, если сеть не вызывает доверия. <a href="https://postgrespro.ru/docs/postgrespro/10/auth-methods#AUTH-PASSWORD">Подробности</a><br>- <code>gss</code> Для аутентификации пользователя использует <code>GSSAPI</code>. Этот способ доступен только для подключений по <code>TCP/IP</code>. <a href="https://postgrespro.ru/docs/postgrespro/10/auth-methods#GSSAPI-AUTH">Подробности</a><br>- <code>sspi</code> Для аутентификации пользователя использует <code>SSPI</code>. Способ доступен только для <code>Windows</code>. <a href="https://postgrespro.ru/docs/postgrespro/10/auth-methods#SSPI-AUTH">Подробности</a><br>- <code>ident</code> Получает имя пользователя операционной системы клиента, связываясь с сервером <code>Ident</code>,<br>  и проверяет, соответствует ли оно имени пользователя базы данных.<br>  Аутентификация ident может использоваться только для подключений по <code>TCP/IP</code>.<br>  Для локальных подключений применяется аутентификация peer. <a href="https://postgrespro.ru/docs/postgrespro/10/auth-methods#AUTH-IDENT">Подробности</a><br>- <code>peer</code> Получает имя пользователя операционной системы клиента из операционной системы и проверяет,<br>  соответствует ли оно имени пользователя запрашиваемой базы данных.<br>  Доступно только для локальных подключений. <a href="https://postgrespro.ru/docs/postgrespro/10/auth-methods#AUTH-PEER">Подробности</a><br>- <code>ldap</code> Проводит аутентификацию, используя сервер <code>LDAP</code>. <a href="https://postgrespro.ru/docs/postgrespro/10/auth-methods#AUTH-LDAP">Подробности</a><br>- <code>radius</code> Проводит аутентификацию, используя сервер <code>RADIUS</code>. <a href="https://postgrespro.ru/docs/postgrespro/10/auth-methods#AUTH-RADIUS">Подробности</a><br>- <code>cert</code> Проводит аутентификацию, используя клиентский сертификат <code>SSL</code>. <a href="https://postgrespro.ru/docs/postgrespro/10/auth-methods#AUTH-CERT">Подробности</a><br>- <code>pam</code> Проводит аутентификацию, используя службу подключаемых модулей аутентификации (<code>PAM</code>), предоставляемую операционной системой. <a href="https://postgrespro.ru/docs/postgrespro/10/auth-methods#AUTH-PAM">Подробности</a><br>- <code>bsd</code> Проводит аутентификацию, используя службу аутентификации <code>BSD</code>, предоставляемую операционной системой. <a href="https://postgrespro.ru/docs/postgrespro/10/auth-methods#AUTH-BSD">Подробности</a></td>
</tr>
<tr>
<td>параметры-аутентификации</td>
<td><code>имя=значение</code><br><code>clientcert</code> можно задать в любой записи hostssl.<br>Если он равен <code>1</code>, клиент должен представить подходящий (доверенный) сертификат <code>SSL</code>,<br>в дополнение к другим требованиям метода проверки подлинности.</td>
</tr>
</tbody>
</table>
<blockquote>
<p>Удалённое соединение по <code>TCP/IP</code> невозможно, если сервер запущен без определения соответствующих значений
для параметра конфигурации <code>listen_addresses</code>, поскольку по умолчанию система принимает подключения по <code>TCP/IP</code>
только для локального адреса замыкания <code>localhost</code>.</p>
</blockquote>
<p><a href="https://postgrespro.ru/docs/postgrespro/10/auth-pg-hba-conf">https://postgrespro.ru/docs/postgrespro/10/auth-pg-hba-conf</a></p>