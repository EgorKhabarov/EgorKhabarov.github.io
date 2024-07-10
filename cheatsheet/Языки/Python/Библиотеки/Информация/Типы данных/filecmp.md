<p>Библиотека "filecmp" используется для сравнения файлов и директорий в Python.
Она предоставляет функциональность для сравнения содержимого файлов, определения различий между файлами и обнаружения одинаковых файлов.</p>
<p>Методы и подмодули модуля "filecmp" можно представить в следующей таблице:</p>
<table>
<thead>
<tr>
<th>Метод/Подмодуль</th>
<th>Краткое Описание</th>
</tr>
</thead>
<tbody>
<tr>
<td>cmp(files1, files2)</td>
<td>Сравнивает содержимое двух файлов и возвращает True, если они одинаковы, и False в противном случае.</td>
</tr>
<tr>
<td>cmpfiles(dir1, dir2)</td>
<td>Сравнивает содержимое двух директорий и возвращает список различий и список одинаковых файлов.</td>
</tr>
<tr>
<td>clear_cache()</td>
<td>Очищает кэш, используемый для сравнения файлов и директорий.</td>
</tr>
<tr>
<td>dircmp(dir1, dir2)</td>
<td>Возвращает объект "dircmp", содержащий информацию о сравнении двух директорий, включая различия и одинаковые файлы.</td>
</tr>
<tr>
<td>cmp_fuzzy(file1, file2)</td>
<td>Сравнивает содержимое двух файлов с использованием нечеткого(размытого) алгоритма сравнения.</td>
</tr>
</tbody>
</table>
<p>Некоторые из самых часто используемых методов библиотеки "filecmp" вместе с краткими описаниями и примерами кода:</p>
<p>Метод cmp(files1, files2) Сравнивает содержимое двух файлов.</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" id="code4112f290fdd49ffe329f8e3dcc36da82b" onclick="copyCode(code4112f290fdd49ffe329f8e3dcc36da82, code4112f290fdd49ffe329f8e3dcc36da82b)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code4112f290fdd49ffe329f8e3dcc36da82"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">filecmp</span>

<span class="k">if</span> <span class="n">filecmp</span><span class="o">.</span><span class="n">cmp</span><span class="p">(</span><span class="s2">&quot;file1.txt&quot;</span><span class="p">,</span> <span class="s2">&quot;file2.txt&quot;</span><span class="p">):</span>
    <span class="nb">print</span><span class="p">(</span><span class="s2">&quot;Файлы одинаковы.&quot;</span><span class="p">)</span>
<span class="k">else</span><span class="p">:</span>
    <span class="nb">print</span><span class="p">(</span><span class="s2">&quot;Файлы различаются.&quot;</span><span class="p">)</span>
</pre></div></div></div>

<p>Метод cmpfiles(dir1, dir2) Сравнивает содержимое двух директорий и возвращает списки различий и одинаковых файлов.</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" id="codef6ef18f058627b10903270d8884af256b" onclick="copyCode(codef6ef18f058627b10903270d8884af256, codef6ef18f058627b10903270d8884af256b)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="codef6ef18f058627b10903270d8884af256"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">filecmp</span>

<span class="n">diff_files</span><span class="p">,</span> <span class="n">common_files</span> <span class="o">=</span> <span class="n">filecmp</span><span class="o">.</span><span class="n">cmpfiles</span><span class="p">(</span><span class="s2">&quot;dir1&quot;</span><span class="p">,</span> <span class="s2">&quot;dir2&quot;</span><span class="p">)</span>

<span class="nb">print</span><span class="p">(</span><span class="s2">&quot;Различные файлы:&quot;</span><span class="p">)</span>
<span class="k">for</span> <span class="n">file</span> <span class="ow">in</span> <span class="n">diff_files</span><span class="p">:</span>
    <span class="nb">print</span><span class="p">(</span><span class="n">file</span><span class="p">)</span>

<span class="nb">print</span><span class="p">(</span><span class="s2">&quot;Одинаковые файлы:&quot;</span><span class="p">)</span>
<span class="k">for</span> <span class="n">file</span> <span class="ow">in</span> <span class="n">common_files</span><span class="p">:</span>
    <span class="nb">print</span><span class="p">(</span><span class="n">file</span><span class="p">)</span>
</pre></div></div></div>