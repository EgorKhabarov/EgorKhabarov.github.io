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
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-code-button" onclick="copyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><pre>Copy code</pre></button></div><div class="code"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">os</span>
<span class="kn">import</span> <span class="nn">stat</span>

<span class="n">file_path</span> <span class="o">=</span> <span class="s2">&quot;path/to/file.txt&quot;</span>
<span class="n">file_stat</span> <span class="o">=</span> <span class="n">os</span><span class="o">.</span><span class="n">stat</span><span class="p">(</span><span class="n">file_path</span><span class="p">)</span>
<span class="k">if</span> <span class="n">stat</span><span class="o">.</span><span class="n">S_ISDIR</span><span class="p">(</span><span class="n">file_stat</span><span class="o">.</span><span class="n">st_mode</span><span class="p">):</span>
    <span class="nb">print</span><span class="p">(</span><span class="s2">&quot;File is a directory&quot;</span><span class="p">)</span>
<span class="k">else</span><span class="p">:</span>
    <span class="nb">print</span><span class="p">(</span><span class="s2">&quot;File is not a directory&quot;</span><span class="p">)</span>
</pre></div></div></div>

<p>stat.S_ISREG(mode): Проверяет, является ли файл обычным файлом.</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-code-button" onclick="copyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><pre>Copy code</pre></button></div><div class="code"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">os</span>
<span class="kn">import</span> <span class="nn">stat</span>

<span class="n">file_path</span> <span class="o">=</span> <span class="s2">&quot;path/to/file.txt&quot;</span>
<span class="n">file_stat</span> <span class="o">=</span> <span class="n">os</span><span class="o">.</span><span class="n">stat</span><span class="p">(</span><span class="n">file_path</span><span class="p">)</span>
<span class="k">if</span> <span class="n">stat</span><span class="o">.</span><span class="n">S_ISREG</span><span class="p">(</span><span class="n">file_stat</span><span class="o">.</span><span class="n">st_mode</span><span class="p">):</span>
    <span class="nb">print</span><span class="p">(</span><span class="s2">&quot;File is a regular file&quot;</span><span class="p">)</span>
<span class="k">else</span><span class="p">:</span>
    <span class="nb">print</span><span class="p">(</span><span class="s2">&quot;File is not a regular file&quot;</span><span class="p">)</span>
</pre></div></div></div>

<p>stat.S_IMODE(mode): Возвращает режим доступа к файлу.</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-code-button" onclick="copyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><pre>Copy code</pre></button></div><div class="code"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">os</span>
<span class="kn">import</span> <span class="nn">stat</span>

<span class="n">file_path</span> <span class="o">=</span> <span class="s2">&quot;path/to/file.txt&quot;</span>
<span class="n">file_stat</span> <span class="o">=</span> <span class="n">os</span><span class="o">.</span><span class="n">stat</span><span class="p">(</span><span class="n">file_path</span><span class="p">)</span>
<span class="n">file_mode</span> <span class="o">=</span> <span class="n">stat</span><span class="o">.</span><span class="n">S_IMODE</span><span class="p">(</span><span class="n">file_stat</span><span class="o">.</span><span class="n">st_mode</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="s2">&quot;File mode:&quot;</span><span class="p">,</span> <span class="n">file_mode</span><span class="p">)</span>
</pre></div></div></div>