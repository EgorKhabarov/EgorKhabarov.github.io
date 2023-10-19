<p>Библиотека "linecache" в Python используется для чтения линий из файлов с исходным кодом.
Она предоставляет функции для извлечения строк из файла по их номеру.</p>
<p>Методы модуля "linecache" включают:
<code>getline(filename, lineno)</code>: Возвращает указанную строку из указанного файла.
<code>getlines(filename)</code>: Возвращает все строки из указанного файла в виде списка.
<code>clearcache()</code>: Очищает кэш, используемый для хранения строк файла.</p>
<p>Примеры подмодулей отсутствуют.</p>
<p>Некоторые из самых часто используемых методов "linecache" включают:
Метод <code>getline(filename, lineno)</code> - возвращает указанную строку из указанного файла.</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" id="code79b" onclick="copyCode(code79, code79b)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code79"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">linecache</span>

<span class="n">line</span> <span class="o">=</span> <span class="n">linecache</span><span class="o">.</span><span class="n">getline</span><span class="p">(</span><span class="s1">&#39;file.txt&#39;</span><span class="p">,</span> <span class="mi">5</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">line</span><span class="p">)</span>
</pre></div></div></div>

<p>Этот код выведет пятую строку из файла 'file.txt'.</p>
<p>Метод <code>getlines(filename)</code> - возвращает все строки из указанного файла в виде списка.</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" id="code80b" onclick="copyCode(code80, code80b)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code80"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">linecache</span>

<span class="n">lines</span> <span class="o">=</span> <span class="n">linecache</span><span class="o">.</span><span class="n">getlines</span><span class="p">(</span><span class="s1">&#39;file.txt&#39;</span><span class="p">)</span>
<span class="k">for</span> <span class="n">line</span> <span class="ow">in</span> <span class="n">lines</span><span class="p">:</span>
    <span class="nb">print</span><span class="p">(</span><span class="n">line</span><span class="p">)</span>
</pre></div></div></div>

<p>Этот код выведет все строки из файла 'file.txt' по одной строке на каждую итерацию цикла.</p>
<p>Метод <code>clearcache()</code> - очищает кэш, используемый для хранения строк файла.
Это может быть полезно, если файл изменился и требуется обновить строки в кэше.</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" id="code81b" onclick="copyCode(code81, code81b)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code81"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">linecache</span>

<span class="c1"># Изменения в файле &#39;file.txt&#39;</span>

<span class="n">linecache</span><span class="o">.</span><span class="n">clearcache</span><span class="p">()</span>
<span class="n">line</span> <span class="o">=</span> <span class="n">linecache</span><span class="o">.</span><span class="n">getline</span><span class="p">(</span><span class="s1">&#39;file.txt&#39;</span><span class="p">,</span> <span class="mi">5</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">line</span><span class="p">)</span>
</pre></div></div></div>

<p>Этот код сначала очищает кэш, а затем возвращает пятую строку из обновленного файла 'file.txt'.</p>
<p>Примечание: Убедитесь, что файл 'file.txt' существует и содержит нужные строки.</p>