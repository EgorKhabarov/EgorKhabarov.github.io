<p>Библиотека "logging" в Python используется для добавления логирования,
то есть записи информации о работе программы, чтобы отслеживать ее выполнение и находить ошибки или проблемы.</p>
<p>Методы модуля "logging" и его подмодулей:</p>
<p><code>getLogger()</code>: Возвращает объект логгера для указанного имени.
<code>basicConfig()</code>: Конфигурирует логгинг с использованием базовых параметров.
<code>Logger.setLevel()</code>: Устанавливает уровень логгирования для указанного логгера.
<code>Logger.addHandler()</code>: Добавляет обработчик к указанному логгеру.
<code>Formatter.format()</code>: Форматирует записи логгера в определенном формате.
<code>StreamHandler</code>: Обработчик, который выводит сообщения логгера в поток (например, на консоль).
<code>FileHandler</code>: Обработчик, который выводит сообщения логгера в файл.
<code>RotatingFileHandler</code>: Обработчик, который выводит сообщения логгера в файл с возможностью
автоматического поворота лог-файла при достижении определенного размера или количества записей.</p>
<p>Наиболее часто используемые методы:</p>
<p><code>logging.debug()</code>: Регистрирует отладочное сообщение.</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" id="code232b" onclick="copyCode(code232, code232b)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code232"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">logging</span>
<span class="n">logging</span><span class="o">.</span><span class="n">debug</span><span class="p">(</span><span class="s2">&quot;This is a debug message&quot;</span><span class="p">)</span>
</pre></div></div></div>

<p><code>logging.info()</code>: Регистрирует информационное сообщение.</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" id="code233b" onclick="copyCode(code233, code233b)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code233"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">logging</span>
<span class="n">logging</span><span class="o">.</span><span class="n">info</span><span class="p">(</span><span class="s2">&quot;This is an info message&quot;</span><span class="p">)</span>
</pre></div></div></div>

<p><code>logging.warning()</code>: Регистрирует предупреждение.</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" id="code234b" onclick="copyCode(code234, code234b)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code234"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">logging</span>
<span class="n">logging</span><span class="o">.</span><span class="n">warning</span><span class="p">(</span><span class="s2">&quot;This is a warning message&quot;</span><span class="p">)</span>
</pre></div></div></div>

<p><code>logging.error()</code>: Регистрирует сообщение об ошибке.</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" id="code235b" onclick="copyCode(code235, code235b)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code235"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">logging</span>
<span class="n">logging</span><span class="o">.</span><span class="n">error</span><span class="p">(</span><span class="s2">&quot;This is an error message&quot;</span><span class="p">)</span>
</pre></div></div></div>

<p><code>logging.critical()</code>: Регистрирует критическое сообщение.</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" id="code236b" onclick="copyCode(code236, code236b)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code236"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">logging</span>
<span class="n">logging</span><span class="o">.</span><span class="n">critical</span><span class="p">(</span><span class="s2">&quot;This is a critical message&quot;</span><span class="p">)</span>
</pre></div></div></div>