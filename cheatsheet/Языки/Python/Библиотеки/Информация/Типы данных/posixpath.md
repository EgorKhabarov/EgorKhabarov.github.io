<p>Библиотека "posixpath" в Python используется для работы с путями файловой системы в POSIX-совместимых операционных системах.
Она предоставляет функции и методы для манипуляции, анализа и навигации по путям к файлам и директориям.</p>
<p>Методы и подмодули библиотеки "posixpath":</p>
<p><code>posixpath.basename(path)</code>: Возвращает базовое имя файла или директории из заданного пути.
<code>posixpath.dirname(path)</code>: Возвращает имя директории из заданного пути.
<code>posixpath.isabs(path)</code>: Проверяет, является ли заданный путь абсолютным.
<code>posixpath.join(path, *paths)</code>: Объединяет компоненты пути в один.
<code>posixpath.normcase(path)</code>: Возвращает нормализованную версию заданного пути с учетом регистра символов.
<code>posixpath.normpath(path)</code>: Возвращает нормализованную версию заданного пути с учетом символов ".", ".." и разделителей.
<code>posixpath.realpath(path)</code>: Возвращает каноническое имя (полный путь) для заданного пути.
<code>posixpath.split(path)</code>: Разделяет заданный путь на имя директории и базовое имя файла или директории.</p>
<p>Некоторые из наиболее часто используемых методов библиотеки "posixpath":</p>
<p><code>basename(path)</code>: Возвращает имя файла из заданного пути.</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" id="code237b" onclick="copyCode(code237, code237b)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code237"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">posixpath</span>

<span class="n">path</span> <span class="o">=</span> <span class="s2">&quot;/home/user/example.txt&quot;</span>
<span class="n">filename</span> <span class="o">=</span> <span class="n">posixpath</span><span class="o">.</span><span class="n">basename</span><span class="p">(</span><span class="n">path</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">filename</span><span class="p">)</span>  <span class="c1"># Выводит: example.txt</span>
</pre></div></div></div>

<p><code>dirname(path)</code>: Возвращает имя директории из заданного пути.</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" id="code238b" onclick="copyCode(code238, code238b)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code238"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">posixpath</span>

<span class="n">path</span> <span class="o">=</span> <span class="s2">&quot;/home/user/example.txt&quot;</span>
<span class="n">directory</span> <span class="o">=</span> <span class="n">posixpath</span><span class="o">.</span><span class="n">dirname</span><span class="p">(</span><span class="n">path</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">directory</span><span class="p">)</span>  <span class="c1"># Выводит: /home/user</span>
</pre></div></div></div>

<p><code>isabs(path)</code>: Проверяет, является ли заданный путь абсолютным.</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" id="code239b" onclick="copyCode(code239, code239b)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code239"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">posixpath</span>

<span class="n">path</span> <span class="o">=</span> <span class="s2">&quot;/home/user/example.txt&quot;</span>
<span class="n">is_absolute</span> <span class="o">=</span> <span class="n">posixpath</span><span class="o">.</span><span class="n">isabs</span><span class="p">(</span><span class="n">path</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">is_absolute</span><span class="p">)</span>  <span class="c1"># Выводит: True</span>
</pre></div></div></div>