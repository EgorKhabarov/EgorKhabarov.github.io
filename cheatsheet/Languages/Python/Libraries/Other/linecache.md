<p>Библиотека "linecache" в Python используется для чтения линий из файлов с исходным кодом.
Она предоставляет функции для извлечения строк из файла по их номеру.</p>
<p>Методы модуля "linecache" включают:
<code>getline(filename, lineno)</code>: Возвращает указанную строку из указанного файла.
<code>getlines(filename)</code>: Возвращает все строки из указанного файла в виде списка.
<code>clearcache()</code>: Очищает кэш, используемый для хранения строк файла.</p>
<p>Примеры подмодулей отсутствуют.</p>
<p>Некоторые из самых часто используемых методов "linecache" включают:
Метод <code>getline(filename, lineno)</code> - возвращает указанную строку из указанного файла.</p>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">linecache</span>

<span class="n">line</span> <span class="o">=</span> <span class="n">linecache</span><span class="o">.</span><span class="n">getline</span><span class="p">(</span><span class="s2">&quot;file.txt&quot;</span><span class="p">,</span> <span class="mi">5</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">line</span><span class="p">)</span>
</pre></div></div></div>

<p>Этот код выведет пятую строку из файла "file.txt".</p>
<p>Метод <code>getlines(filename)</code> - возвращает все строки из указанного файла в виде списка.</p>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">linecache</span>

<span class="n">lines</span> <span class="o">=</span> <span class="n">linecache</span><span class="o">.</span><span class="n">getlines</span><span class="p">(</span><span class="s2">&quot;file.txt&quot;</span><span class="p">)</span>
<span class="k">for</span> <span class="n">line</span> <span class="ow">in</span> <span class="n">lines</span><span class="p">:</span>
    <span class="nb">print</span><span class="p">(</span><span class="n">line</span><span class="p">)</span>
</pre></div></div></div>

<p>Этот код выведет все строки из файла "file.txt" по одной строке на каждую итерацию цикла.</p>
<p>Метод <code>clearcache()</code> - очищает кэш, используемый для хранения строк файла.
Это может быть полезно, если файл изменился и требуется обновить строки в кэше.</p>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">linecache</span>

<span class="c1"># Изменения в файле &quot;file.txt&quot;</span>

<span class="n">linecache</span><span class="o">.</span><span class="n">clearcache</span><span class="p">()</span>
<span class="n">line</span> <span class="o">=</span> <span class="n">linecache</span><span class="o">.</span><span class="n">getline</span><span class="p">(</span><span class="s2">&quot;file.txt&quot;</span><span class="p">,</span> <span class="mi">5</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">line</span><span class="p">)</span>
</pre></div></div></div>

<p>Этот код сначала очищает кэш, а затем возвращает пятую строку из обновленного файла "file.txt".</p>
<p>Примечание: Убедитесь, что файл "file.txt" существует и содержит нужные строки.</p>