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
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" id="codef14b848b2e0297e9f6a388e8747caa35b" onclick="copyCode(codef14b848b2e0297e9f6a388e8747caa35, codef14b848b2e0297e9f6a388e8747caa35b)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="codef14b848b2e0297e9f6a388e8747caa35"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">os</span>
<span class="kn">import</span> <span class="nn">stat</span>

<span class="n">file_path</span> <span class="o">=</span> <span class="s1">&#39;path/to/file.txt&#39;</span>
<span class="n">file_stat</span> <span class="o">=</span> <span class="n">os</span><span class="o">.</span><span class="n">stat</span><span class="p">(</span><span class="n">file_path</span><span class="p">)</span>
<span class="k">if</span> <span class="n">stat</span><span class="o">.</span><span class="n">S_ISDIR</span><span class="p">(</span><span class="n">file_stat</span><span class="o">.</span><span class="n">st_mode</span><span class="p">):</span>
    <span class="nb">print</span><span class="p">(</span><span class="s2">&quot;File is a directory&quot;</span><span class="p">)</span>
<span class="k">else</span><span class="p">:</span>
    <span class="nb">print</span><span class="p">(</span><span class="s2">&quot;File is not a directory&quot;</span><span class="p">)</span>
</pre></div></div></div>

<p>stat.S_ISREG(mode): Проверяет, является ли файл обычным файлом.</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" id="code6f561a02f81121312d1b8e4a88d1dd5db" onclick="copyCode(code6f561a02f81121312d1b8e4a88d1dd5d, code6f561a02f81121312d1b8e4a88d1dd5db)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code6f561a02f81121312d1b8e4a88d1dd5d"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">os</span>
<span class="kn">import</span> <span class="nn">stat</span>

<span class="n">file_path</span> <span class="o">=</span> <span class="s1">&#39;path/to/file.txt&#39;</span>
<span class="n">file_stat</span> <span class="o">=</span> <span class="n">os</span><span class="o">.</span><span class="n">stat</span><span class="p">(</span><span class="n">file_path</span><span class="p">)</span>
<span class="k">if</span> <span class="n">stat</span><span class="o">.</span><span class="n">S_ISREG</span><span class="p">(</span><span class="n">file_stat</span><span class="o">.</span><span class="n">st_mode</span><span class="p">):</span>
    <span class="nb">print</span><span class="p">(</span><span class="s2">&quot;File is a regular file&quot;</span><span class="p">)</span>
<span class="k">else</span><span class="p">:</span>
    <span class="nb">print</span><span class="p">(</span><span class="s2">&quot;File is not a regular file&quot;</span><span class="p">)</span>
</pre></div></div></div>

<p>stat.S_IMODE(mode): Возвращает режим доступа к файлу.</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" id="codeae7970a05ca65a989a0dd71be8b091a4b" onclick="copyCode(codeae7970a05ca65a989a0dd71be8b091a4, codeae7970a05ca65a989a0dd71be8b091a4b)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="codeae7970a05ca65a989a0dd71be8b091a4"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">os</span>
<span class="kn">import</span> <span class="nn">stat</span>

<span class="n">file_path</span> <span class="o">=</span> <span class="s1">&#39;path/to/file.txt&#39;</span>
<span class="n">file_stat</span> <span class="o">=</span> <span class="n">os</span><span class="o">.</span><span class="n">stat</span><span class="p">(</span><span class="n">file_path</span><span class="p">)</span>
<span class="n">file_mode</span> <span class="o">=</span> <span class="n">stat</span><span class="o">.</span><span class="n">S_IMODE</span><span class="p">(</span><span class="n">file_stat</span><span class="o">.</span><span class="n">st_mode</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="s2">&quot;File mode:&quot;</span><span class="p">,</span> <span class="n">file_mode</span><span class="p">)</span>
</pre></div></div></div>