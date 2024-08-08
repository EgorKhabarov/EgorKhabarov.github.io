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
<div class="code-element">
    <div class="lang-line">
        <text>python</text>
        <button class="copy-button"
        onclick="copyCode(this)">
    <svg stroke="currentColor"
         fill="none"
         stroke-width="2"
         viewBox="0 0 24 24"
         stroke-linecap="round"
         stroke-linejoin="round"
         class="h-4 w-4"
         height="1em"
         width="1em"
         xmlns="http://www.w3.org/2000/svg">
        <path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path>
        <rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect>
    </svg>
    <text>Copy code</text>
</button>

    </div>
    <div class="code"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">poplib</span>

<span class="n">pop_server</span> <span class="o">=</span> <span class="n">poplib</span><span class="o">.</span><span class="n">POP3</span><span class="p">(</span><span class="s2">&quot;mail.example.com&quot;</span><span class="p">,</span> <span class="mi">110</span><span class="p">)</span>
<span class="n">pop_server</span><span class="o">.</span><span class="n">user</span><span class="p">(</span><span class="s2">&quot;your_username&quot;</span><span class="p">)</span>
<span class="n">pop_server</span><span class="o">.</span><span class="n">pass_</span><span class="p">(</span><span class="s2">&quot;your_password&quot;</span><span class="p">)</span>
</pre></div></div>
</div>