<p>Библиотека "genericpath" в Python используется для работы с путями и файловой системой на разных платформах.
Она предоставляет универсальные методы для обработки путей, создания новых путей, проверки наличия файлов и директорий,
а также для работы с именами файлов.</p>
<p>Таблица методов и их описания в модуле "genericpath":</p>
<table>
<thead>
<tr>
<th>Метод</th>
<th>Описание</th>
</tr>
</thead>
<tbody>
<tr>
<td>isdir(path)</td>
<td>Проверяет, является ли указанный путь директорией.</td>
</tr>
<tr>
<td>isfile(path)</td>
<td>Проверяет, является ли указанный путь файлом.</td>
</tr>
<tr>
<td>exists(path)</td>
<td>Проверяет, существует ли указанный путь.</td>
</tr>
<tr>
<td>lexists(path)</td>
<td>Проверяет, существует ли указанный путь (обходя символические ссылки).</td>
</tr>
<tr>
<td>split(path)</td>
<td>Разделяет путь на директорию и базовое имя файла.</td>
</tr>
<tr>
<td>splitext(path)</td>
<td>Разделяет путь на базовое имя файла и расширение.</td>
</tr>
<tr>
<td>basename(path)</td>
<td>Возвращает последний компонент пути (имя файла или директории).</td>
</tr>
<tr>
<td>dirname(path)</td>
<td>Возвращает директорию из пути.</td>
</tr>
<tr>
<td>join(path, *paths)</td>
<td>Объединяет пути в переносимый образ.</td>
</tr>
<tr>
<td>normpath(path)</td>
<td>Преобразует путь, удаляя избыточные разделители и ссылки "." и "..".</td>
</tr>
<tr>
<td>abspath(path)</td>
<td>Возвращает абсолютный путь.</td>
</tr>
</tbody>
</table>
<p>isdir(path): Проверяет, является ли указанный путь директорией.</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" id="code6ff60d93a475490194e6f982381d50a3b" onclick="copyCode(code6ff60d93a475490194e6f982381d50a3, code6ff60d93a475490194e6f982381d50a3b)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code6ff60d93a475490194e6f982381d50a3"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">os.path</span>

<span class="n">path</span> <span class="o">=</span> <span class="s1">&#39;/path/to/directory&#39;</span>
<span class="k">if</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">isdir</span><span class="p">(</span><span class="n">path</span><span class="p">):</span>
    <span class="nb">print</span><span class="p">(</span><span class="sa">f</span><span class="s2">&quot;</span><span class="si">{</span><span class="n">path</span><span class="si">}</span><span class="s2"> is a directory.&quot;</span><span class="p">)</span>
</pre></div></div></div>

<p>isfile(path): Проверяет, является ли указанный путь файлом.</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" id="codebac59ee831ebf862c93bcb920b4620a4b" onclick="copyCode(codebac59ee831ebf862c93bcb920b4620a4, codebac59ee831ebf862c93bcb920b4620a4b)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="codebac59ee831ebf862c93bcb920b4620a4"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">os.path</span>

<span class="n">path</span> <span class="o">=</span> <span class="s1">&#39;/path/to/file.txt&#39;</span>
<span class="k">if</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">isfile</span><span class="p">(</span><span class="n">path</span><span class="p">):</span>
    <span class="nb">print</span><span class="p">(</span><span class="sa">f</span><span class="s2">&quot;</span><span class="si">{</span><span class="n">path</span><span class="si">}</span><span class="s2"> is a file.&quot;</span><span class="p">)</span>
</pre></div></div></div>

<p>exists(path): Проверяет, существует ли указанный путь.</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" id="coded4ab9f66e4f35aad548ef0f9528822f0b" onclick="copyCode(coded4ab9f66e4f35aad548ef0f9528822f0, coded4ab9f66e4f35aad548ef0f9528822f0b)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="coded4ab9f66e4f35aad548ef0f9528822f0"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">os.path</span>

<span class="n">path</span> <span class="o">=</span> <span class="s1">&#39;/path/to/file.txt&#39;</span>
<span class="k">if</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">exists</span><span class="p">(</span><span class="n">path</span><span class="p">):</span>
    <span class="nb">print</span><span class="p">(</span><span class="sa">f</span><span class="s2">&quot;</span><span class="si">{</span><span class="n">path</span><span class="si">}</span><span class="s2"> exists.&quot;</span><span class="p">)</span>
</pre></div></div></div>

<p>splitext(path): Разделяет путь на базовое имя файла и расширение.</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" id="code5153abeef5b9f8e110dbd800b4100df2b" onclick="copyCode(code5153abeef5b9f8e110dbd800b4100df2, code5153abeef5b9f8e110dbd800b4100df2b)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code5153abeef5b9f8e110dbd800b4100df2"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">os.path</span>

<span class="n">path</span> <span class="o">=</span> <span class="s1">&#39;/path/to/file.txt&#39;</span>
<span class="n">base_name</span><span class="p">,</span> <span class="n">extension</span> <span class="o">=</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">splitext</span><span class="p">(</span><span class="n">path</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="sa">f</span><span class="s2">&quot;Base name: </span><span class="si">{</span><span class="n">base_name</span><span class="si">}</span><span class="s2">&quot;</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="sa">f</span><span class="s2">&quot;Extension: </span><span class="si">{</span><span class="n">extension</span><span class="si">}</span><span class="s2">&quot;</span><span class="p">)</span>
</pre></div></div></div>