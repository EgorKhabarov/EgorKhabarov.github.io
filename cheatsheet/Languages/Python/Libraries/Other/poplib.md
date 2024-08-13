<p>Библиотека "poplib" в Python используется для работы с протоколом почтового ящика на основе протокола POP3 (Post Office Protocol version 3).
Она позволяет получать электронные письма, удалять их, и выполнять другие операции взаимодействия с почтовым сервером.</p>
<p>Методы и подмодули библиотеки "poplib":</p>
<p><code>poplib.POP3(host[, port])</code>: Создает объект соединения с почтовым сервером POP3 на указанном хосте и порту.
<code>poplib.POP3.user(username)</code>: Аутентифицирует пользователя на сервере, указывая имя пользователя.
<code>poplib.POP3.pass_(password)</code>: Аутентифицирует пользователя на сервере, указывая пароль.
<code>poplib.POP3.stat()</code>: Возвращает информацию о состоянии почтового ящика, включая количество сообщений и общий размер.
<code>poplib.POP3.list([which])</code>: Возвращает список всех сообщений в почтовом ящике, или информацию о конкретном сообщении, если указан параметр "which".
<code>poplib.POP3.retr(which)</code>: Получает содержимое указанного сообщения из почтового ящика.
<code>poplib.POP3.dele(which)</code>: Отмечает указанное сообщение для удаления.
<code>poplib.POP3.quit()</code>: Закрывает соединение с сервером POP3.</p>
<p>Наиболее часто используемые методы в библиотеке "poplib":</p>
<p><code>poplib.POP3(host[, port])</code>: Создание соединения с почтовым сервером.
<code>poplib.POP3.user(username)</code> и <code>poplib.POP3.pass_(password)</code>: Аутентификация пользователя на сервере.
<code>poplib.POP3.stat()</code>: Получение информации о состоянии почтового ящика.
<code>poplib.POP3.list()</code>: Получение списка всех сообщений в почтовом ящике.
<code>poplib.POP3.retr(which)</code>: Получение содержимого конкретного сообщения.
<code>poplib.POP3.quit()</code>: Закрытие соединения с сервером POP3.</p>
<p>Пример использования метода <code>poplib.POP3(user, password)</code> для создания соединения с почтовым сервером:</p>
<pre><code class="language-python">import poplib

pop_server = poplib.POP3(&quot;mail.example.com&quot;, 110)
pop_server.user(&quot;your_username&quot;)
pop_server.pass_(&quot;your_password&quot;)
</code></pre>