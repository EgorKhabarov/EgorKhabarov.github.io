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
<td>Проверяет, является ли указанный путь директорией</td>
</tr>
<tr>
<td>isfile(path)</td>
<td>Проверяет, является ли указанный путь файлом</td>
</tr>
<tr>
<td>exists(path)</td>
<td>Проверяет, существует ли указанный путь</td>
</tr>
<tr>
<td>lexists(path)</td>
<td>Проверяет, существует ли указанный путь (обходя символические ссылки)</td>
</tr>
<tr>
<td>split(path)</td>
<td>Разделяет путь на директорию и базовое имя файла</td>
</tr>
<tr>
<td>splitext(path)</td>
<td>Разделяет путь на базовое имя файла и расширение</td>
</tr>
<tr>
<td>basename(path)</td>
<td>Возвращает последний компонент пути (имя файла или директории)</td>
</tr>
<tr>
<td>dirname(path)</td>
<td>Возвращает директорию из пути</td>
</tr>
<tr>
<td>join(path, *paths)</td>
<td>Объединяет пути в переносимый образ</td>
</tr>
<tr>
<td>normpath(path)</td>
<td>Преобразует путь, удаляя избыточные разделители и ссылки "." и ".."</td>
</tr>
<tr>
<td>abspath(path)</td>
<td>Возвращает абсолютный путь</td>
</tr>
</tbody>
</table>
<p>isdir(path): Проверяет, является ли указанный путь директорией.</p>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">os.path</span>

<span class="n">path</span> <span class="o">=</span> <span class="s2">&quot;/path/to/directory&quot;</span>
<span class="k">if</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">isdir</span><span class="p">(</span><span class="n">path</span><span class="p">):</span>
    <span class="nb">print</span><span class="p">(</span><span class="sa">f</span><span class="s2">&quot;</span><span class="si">{</span><span class="n">path</span><span class="si">}</span><span class="s2"> is a directory.&quot;</span><span class="p">)</span>
</pre></div></div></div>

<p>isfile(path): Проверяет, является ли указанный путь файлом.</p>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">os.path</span>

<span class="n">path</span> <span class="o">=</span> <span class="s2">&quot;/path/to/file.txt&quot;</span>
<span class="k">if</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">isfile</span><span class="p">(</span><span class="n">path</span><span class="p">):</span>
    <span class="nb">print</span><span class="p">(</span><span class="sa">f</span><span class="s2">&quot;</span><span class="si">{</span><span class="n">path</span><span class="si">}</span><span class="s2"> is a file.&quot;</span><span class="p">)</span>
</pre></div></div></div>

<p>exists(path): Проверяет, существует ли указанный путь.</p>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">os.path</span>

<span class="n">path</span> <span class="o">=</span> <span class="s2">&quot;/path/to/file.txt&quot;</span>
<span class="k">if</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">exists</span><span class="p">(</span><span class="n">path</span><span class="p">):</span>
    <span class="nb">print</span><span class="p">(</span><span class="sa">f</span><span class="s2">&quot;</span><span class="si">{</span><span class="n">path</span><span class="si">}</span><span class="s2"> exists.&quot;</span><span class="p">)</span>
</pre></div></div></div>

<p>splitext(path): Разделяет путь на базовое имя файла и расширение.</p>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">os.path</span>

<span class="n">path</span> <span class="o">=</span> <span class="s2">&quot;/path/to/file.txt&quot;</span>
<span class="n">base_name</span><span class="p">,</span> <span class="n">extension</span> <span class="o">=</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">splitext</span><span class="p">(</span><span class="n">path</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="sa">f</span><span class="s2">&quot;Base name: </span><span class="si">{</span><span class="n">base_name</span><span class="si">}</span><span class="s2">&quot;</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="sa">f</span><span class="s2">&quot;Extension: </span><span class="si">{</span><span class="n">extension</span><span class="si">}</span><span class="s2">&quot;</span><span class="p">)</span>
</pre></div></div></div>