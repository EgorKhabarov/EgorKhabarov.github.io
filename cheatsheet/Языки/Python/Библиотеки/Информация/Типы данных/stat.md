<p>Библиотека "stat" в Python используется для работы с информацией о файловой системе,
такой как атрибуты файла, права доступа и временные метки.</p>
<p>Методы модуля "stat" и его подмодулей:</p>
<p>stat.S_ISDIR(mode): Проверяет, является ли файл директорией.
stat.S_ISREG(mode): Проверяет, является ли файл обычным файлом.
stat.S_ISLNK(mode): Проверяет, является ли файл символической ссылкой.
stat.S_ISSOCK(mode): Проверяет, является ли файл сокетом.
stat.S_ISFIFO(mode): Проверяет, является ли файл каналом FIFO.
stat.S_ISBLK(mode): Проверяет, является ли файл блочным устройством.
stat.S_ISCHR(mode): Проверяет, является ли файл символьным устройством.
stat.S_IMODE(mode): Возвращает режим доступа к файлу.
stat.S_IFMT(mode): Возвращает тип файла и режим доступа.</p>
<p>Самые часто используемые методы:</p>
<p>stat.S_ISDIR(mode): Проверяет, является ли файл директорией.</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button"id="code0808dc74a9a4cd274396c019eeab9833b"onclick="copyCode(code0808dc74a9a4cd274396c019eeab9833, code0808dc74a9a4cd274396c019eeab9833b)"><svg stroke="currentColor"fill="none"stroke-width="2"viewBox="0 0 24 24"stroke-linecap="round"stroke-linejoin="round"class="h-4 w-4"height="1em"width="1em"xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code0808dc74a9a4cd274396c019eeab9833"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">os</span>
<span class="kn">import</span> <span class="nn">stat</span>

<span class="n">file_path</span> <span class="o">=</span> <span class="s2">&quot;path/to/file.txt&quot;</span>
<span class="n">file_stat</span> <span class="o">=</span> <span class="n">os</span><span class="o">.</span><span class="n">stat</span><span class="p">(</span><span class="n">file_path</span><span class="p">)</span>
<span class="k">if</span> <span class="n">stat</span><span class="o">.</span><span class="n">S_ISDIR</span><span class="p">(</span><span class="n">file_stat</span><span class="o">.</span><span class="n">st_mode</span><span class="p">):</span>
    <span class="nb">print</span><span class="p">(</span><span class="s2">&quot;File is a directory&quot;</span><span class="p">)</span>
<span class="k">else</span><span class="p">:</span>
    <span class="nb">print</span><span class="p">(</span><span class="s2">&quot;File is not a directory&quot;</span><span class="p">)</span>
</pre></div></div></div>

<p>stat.S_ISREG(mode): Проверяет, является ли файл обычным файлом.</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button"id="code07c2df88c6af073be74d189e763d2b48b"onclick="copyCode(code07c2df88c6af073be74d189e763d2b48, code07c2df88c6af073be74d189e763d2b48b)"><svg stroke="currentColor"fill="none"stroke-width="2"viewBox="0 0 24 24"stroke-linecap="round"stroke-linejoin="round"class="h-4 w-4"height="1em"width="1em"xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code07c2df88c6af073be74d189e763d2b48"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">os</span>
<span class="kn">import</span> <span class="nn">stat</span>

<span class="n">file_path</span> <span class="o">=</span> <span class="s2">&quot;path/to/file.txt&quot;</span>
<span class="n">file_stat</span> <span class="o">=</span> <span class="n">os</span><span class="o">.</span><span class="n">stat</span><span class="p">(</span><span class="n">file_path</span><span class="p">)</span>
<span class="k">if</span> <span class="n">stat</span><span class="o">.</span><span class="n">S_ISREG</span><span class="p">(</span><span class="n">file_stat</span><span class="o">.</span><span class="n">st_mode</span><span class="p">):</span>
    <span class="nb">print</span><span class="p">(</span><span class="s2">&quot;File is a regular file&quot;</span><span class="p">)</span>
<span class="k">else</span><span class="p">:</span>
    <span class="nb">print</span><span class="p">(</span><span class="s2">&quot;File is not a regular file&quot;</span><span class="p">)</span>
</pre></div></div></div>

<p>stat.S_IMODE(mode): Возвращает режим доступа к файлу.</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button"id="code7b90dbabeb502e6f99c1a491420e400eb"onclick="copyCode(code7b90dbabeb502e6f99c1a491420e400e, code7b90dbabeb502e6f99c1a491420e400eb)"><svg stroke="currentColor"fill="none"stroke-width="2"viewBox="0 0 24 24"stroke-linecap="round"stroke-linejoin="round"class="h-4 w-4"height="1em"width="1em"xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code7b90dbabeb502e6f99c1a491420e400e"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">os</span>
<span class="kn">import</span> <span class="nn">stat</span>

<span class="n">file_path</span> <span class="o">=</span> <span class="s2">&quot;path/to/file.txt&quot;</span>
<span class="n">file_stat</span> <span class="o">=</span> <span class="n">os</span><span class="o">.</span><span class="n">stat</span><span class="p">(</span><span class="n">file_path</span><span class="p">)</span>
<span class="n">file_mode</span> <span class="o">=</span> <span class="n">stat</span><span class="o">.</span><span class="n">S_IMODE</span><span class="p">(</span><span class="n">file_stat</span><span class="o">.</span><span class="n">st_mode</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="s2">&quot;File mode:&quot;</span><span class="p">,</span> <span class="n">file_mode</span><span class="p">)</span>
</pre></div></div></div>