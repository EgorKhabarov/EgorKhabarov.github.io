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
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">logging</span>
<span class="n">logging</span><span class="o">.</span><span class="n">debug</span><span class="p">(</span><span class="s2">&quot;This is a debug message&quot;</span><span class="p">)</span>
</pre></div></div></div>

<p><code>logging.info()</code>: Регистрирует информационное сообщение.</p>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">logging</span>
<span class="n">logging</span><span class="o">.</span><span class="n">info</span><span class="p">(</span><span class="s2">&quot;This is an info message&quot;</span><span class="p">)</span>
</pre></div></div></div>

<p><code>logging.warning()</code>: Регистрирует предупреждение.</p>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">logging</span>
<span class="n">logging</span><span class="o">.</span><span class="n">warning</span><span class="p">(</span><span class="s2">&quot;This is a warning message&quot;</span><span class="p">)</span>
</pre></div></div></div>

<p><code>logging.error()</code>: Регистрирует сообщение об ошибке.</p>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">logging</span>
<span class="n">logging</span><span class="o">.</span><span class="n">error</span><span class="p">(</span><span class="s2">&quot;This is an error message&quot;</span><span class="p">)</span>
</pre></div></div></div>

<p><code>logging.critical()</code>: Регистрирует критическое сообщение.</p>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">logging</span>
<span class="n">logging</span><span class="o">.</span><span class="n">critical</span><span class="p">(</span><span class="s2">&quot;This is a critical message&quot;</span><span class="p">)</span>
</pre></div></div></div>

<p>import logging</p>
<p>Запись в файл</p>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="n">logging</span><span class="o">.</span><span class="n">basicConfig</span><span class="p">(</span><span class="n">filename</span><span class="o">=</span><span class="s2">&quot;example.log&quot;</span><span class="p">,</span>
                    <span class="n">level</span><span class="o">=</span><span class="n">logging</span><span class="o">.</span><span class="n">DEBUG</span><span class="p">)</span>
</pre></div></div></div>

<p>Запись в консоль</p>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="n">logging</span><span class="o">.</span><span class="n">basicConfig</span><span class="p">(</span><span class="n">level</span><span class="o">=</span><span class="n">logging</span><span class="o">.</span><span class="n">DEBUG</span><span class="p">,</span>
                    <span class="nb">format</span><span class="o">=</span><span class="s2">&quot;</span><span class="si">%(message)s</span><span class="s2">&quot;</span><span class="p">)</span>
</pre></div></div></div>

<p>Запись в файл и в консоль</p>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="n">logging</span><span class="o">.</span><span class="n">basicConfig</span><span class="p">(</span><span class="n">filename</span><span class="o">=</span><span class="s2">&quot;example.log&quot;</span><span class="p">,</span>
                    <span class="n">level</span><span class="o">=</span><span class="n">logging</span><span class="o">.</span><span class="n">DEBUG</span><span class="p">,</span>
                    <span class="nb">format</span><span class="o">=</span><span class="s2">&quot;</span><span class="si">%(asctime)s</span><span class="s2"> </span><span class="si">%(levelname)s</span><span class="s2"> </span><span class="si">%(message)s</span><span class="s2">&quot;</span><span class="p">,</span>
                    <span class="n">datefmt</span><span class="o">=</span><span class="s2">&quot;%Y-%m-</span><span class="si">%d</span><span class="s2"> %H:%M:%S&quot;</span><span class="p">)</span>
<span class="n">console</span> <span class="o">=</span> <span class="n">logging</span><span class="o">.</span><span class="n">StreamHandler</span><span class="p">()</span>
<span class="n">console</span><span class="o">.</span><span class="n">setLevel</span><span class="p">(</span><span class="n">logging</span><span class="o">.</span><span class="n">DEBUG</span><span class="p">)</span>
<span class="n">formatter</span> <span class="o">=</span> <span class="n">logging</span><span class="o">.</span><span class="n">Formatter</span><span class="p">(</span><span class="s2">&quot;</span><span class="si">%(asctime)s</span><span class="s2"> &quot;</span>
                              <span class="s2">&quot;</span><span class="si">%(levelname)s</span><span class="s2"> &quot;</span>
                              <span class="s2">&quot;</span><span class="si">%(message)s</span><span class="s2">&quot;</span><span class="p">,</span>
                              <span class="n">datefmt</span><span class="o">=</span><span class="s2">&quot;%Y-%m-</span><span class="si">%d</span><span class="s2"> %H:%M:%S&quot;</span><span class="p">)</span>
<span class="n">console</span><span class="o">.</span><span class="n">setFormatter</span><span class="p">(</span><span class="n">formatter</span><span class="p">)</span>
<span class="n">logging</span><span class="o">.</span><span class="n">getLogger</span><span class="p">(</span><span class="s2">&quot;&quot;</span><span class="p">)</span><span class="o">.</span><span class="n">addHandler</span><span class="p">(</span><span class="n">console</span><span class="p">)</span>
</pre></div></div></div>

<p>Для самих сообщений</p>
<div class="code_element"><div class="lang_line"><text>text</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-text"><div class="highlight"><pre><span></span>%s           строка
%d           для целых чисел
%c           для имени логгера
%f           для чисел с плавающей точкой
%r           для строковых представлений объектов
%m           для сообщения журнала
%x           целое число в шестнадцатеричной системе исчисления
%o           целое число в восьмеричной системе исчисления
%e, %E       число в экспоненциальной форме
</pre></div></div></div>

<p>Для настроек логгирования</p>
<div class="code_element"><div class="lang_line"><text>text</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-text"><div class="highlight"><pre><span></span>%(message)s     сообщение журнала

%(asctime)s     время записи сообщения в формате (по умолчанию YYYY-MM-DD HH:MM:SS,sss настраивать в basicConfig(datefmt))
%(created)f     время записи сообщения в секундах, начиная с 1 января 1970 года

%(filename)s    имя файла, в котором был вызван логгер
%(funcName)s    имя функции, в которой был вызван логгер
%(name)s        имя логгера, который записывает сообщение
%(module)s      имя модуля, в котором был вызван логгер
%(threadName)s  имя потока, в котором был вызван логгер
%(processName)s имя процесса, в котором был вызван логгер

%(levelname)s   уровень журнала (например, DEBUG, INFO, WARNING, ERROR, CRITICAL)
%(levelno)s     уровень журнала в числовом формате (10 для DEBUG, 20 для INFO и т. д.)

%(lineno)d      номер строки, в которой был вызван логгер
%(pathname)s    полный путь к файлу, в котором был вызван логгер
%(process)d     идентификатор процесса, в котором был вызван логгер
%(thread)d      идентификатор потока, в котором был вызван логгер
</pre></div></div></div>

<p>Код для применения функций к тексту</p>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="n">logging</span><span class="o">.</span><span class="n">info</span> <span class="o">=</span> <span class="k">lambda</span> <span class="n">msg</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="n">f</span><span class="o">=</span><span class="n">logging</span><span class="o">.</span><span class="n">info</span><span class="p">:</span> <span class="n">f</span><span class="p">(</span><span class="n">Up</span><span class="p">(</span><span class="n">msg</span><span class="p">),</span> <span class="o">*</span><span class="n">args</span><span class="p">)</span>
</pre></div></div></div>