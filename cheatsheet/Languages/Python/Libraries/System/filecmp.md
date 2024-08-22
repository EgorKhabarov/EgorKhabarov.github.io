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
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">filecmp</span>

<span class="k">if</span> <span class="n">filecmp</span><span class="o">.</span><span class="n">cmp</span><span class="p">(</span><span class="s2">&quot;file1.txt&quot;</span><span class="p">,</span> <span class="s2">&quot;file2.txt&quot;</span><span class="p">):</span>
    <span class="nb">print</span><span class="p">(</span><span class="s2">&quot;Файлы одинаковы.&quot;</span><span class="p">)</span>
<span class="k">else</span><span class="p">:</span>
    <span class="nb">print</span><span class="p">(</span><span class="s2">&quot;Файлы различаются.&quot;</span><span class="p">)</span>
</pre></div></div></div>

<p>Метод cmpfiles(dir1, dir2) Сравнивает содержимое двух директорий и возвращает списки различий и одинаковых файлов.</p>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">filecmp</span>

<span class="n">diff_files</span><span class="p">,</span> <span class="n">common_files</span> <span class="o">=</span> <span class="n">filecmp</span><span class="o">.</span><span class="n">cmpfiles</span><span class="p">(</span><span class="s2">&quot;dir1&quot;</span><span class="p">,</span> <span class="s2">&quot;dir2&quot;</span><span class="p">)</span>

<span class="nb">print</span><span class="p">(</span><span class="s2">&quot;Различные файлы:&quot;</span><span class="p">)</span>
<span class="k">for</span> <span class="n">file</span> <span class="ow">in</span> <span class="n">diff_files</span><span class="p">:</span>
    <span class="nb">print</span><span class="p">(</span><span class="n">file</span><span class="p">)</span>

<span class="nb">print</span><span class="p">(</span><span class="s2">&quot;Одинаковые файлы:&quot;</span><span class="p">)</span>
<span class="k">for</span> <span class="n">file</span> <span class="ow">in</span> <span class="n">common_files</span><span class="p">:</span>
    <span class="nb">print</span><span class="p">(</span><span class="n">file</span><span class="p">)</span>
</pre></div></div></div>