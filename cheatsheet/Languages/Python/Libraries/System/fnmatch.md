<p>Библиотека <code>fnmatch</code> в Python используется для работы с шаблонами файловых имен, основанными на Unix shell-подобном синтаксисе.
Она позволяет легко сопоставлять строки с шаблонами, которые включают такие символы, как <code>*</code>, <code>?</code>, и <code>[]</code>.</p>
<h1>Основные функции и их описание</h1>
<table>
<thead>
<tr>
<th>Функция</th>
<th>Описание</th>
<th>Пример использования</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>fnmatch.fnmatch()</code></td>
<td>Сопоставляет строку с шаблоном.<br>Регистро<strong>зависимо</strong> на Unix и регистро<strong>независимо</strong> на Windows</td>
<td><div class="code" style="border-radius:.375rem .375rem;"><div class="highlight"><pre><div class="highlight"><pre><span></span><span class="n">fnmatch</span><span class="o">.</span><span class="n">fnmatch</span><span class="p">(</span><span class="s2">&quot;foo.txt&quot;</span><span class="p">,</span> <span class="s2">&quot;*.txt&quot;</span><span class="p">)</span><br></pre></div></pre></div></div></td>
</tr>
<tr>
<td><code>fnmatch.fnmatchcase()</code></td>
<td>Сопоставляет строку с шаблоном с учетом регистра на всех платформах</td>
<td><div class="code" style="border-radius:.375rem .375rem;"><div class="highlight"><pre><div class="highlight"><pre><span></span><span class="n">fnmatch</span><span class="o">.</span><span class="n">fnmatchcase</span><span class="p">(</span><span class="s2">&quot;Foo.txt&quot;</span><span class="p">,</span> <span class="s2">&quot;*.TXT&quot;</span><span class="p">)</span><br></pre></div></pre></div></div></td>
</tr>
<tr>
<td><code>fnmatch.filter()</code></td>
<td>Фильтрует список строк, оставляя только те, которые соответствуют шаблону</td>
<td><div class="code" style="border-radius:.375rem .375rem;"><div class="highlight"><pre><div class="highlight"><pre><span></span><span class="n">fnmatch</span><span class="o">.</span><span class="n">filter</span><span class="p">([</span><span class="s2">&quot;foo.txt&quot;</span><span class="p">,</span> <span class="s2">&quot;bar.py&quot;</span><span class="p">],</span> <span class="s2">&quot;*.txt&quot;</span><span class="p">)</span><br></pre></div></pre></div></div></td>
</tr>
<tr>
<td><code>fnmatch.translate()</code></td>
<td>Преобразует шаблон в регулярное выражение,<br>которое можно использовать с <code>re</code> для более сложных сопоставлений</td>
<td><div class="code" style="border-radius:.375rem .375rem;"><div class="highlight"><pre><div class="highlight"><pre><span></span><span class="n">pattern</span> <span class="o">=</span> <span class="n">fnmatch</span><span class="o">.</span><span class="n">translate</span><span class="p">(</span><span class="s2">&quot;*.txt&quot;</span><span class="p">)</span><br></pre></div></pre></div></div></td>
</tr>
</tbody>
</table>
<h1>Специальные символы в шаблонах</h1>
<table>
<thead>
<tr>
<th>Символ</th>
<th>Описание</th>
<th>Пример</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>*</code></td>
<td>Соответствует любой строке (включая пустую)</td>
<td><code>"*.txt"</code> соответствует <code>"file.txt"</code> и <code>"a.txt"</code></td>
</tr>
<tr>
<td><code>?</code></td>
<td>Соответствует любому одному символу</td>
<td><code>"file?.txt"</code> соответствует <code>"file1.txt"</code>, но не <code>"file12.txt"</code></td>
</tr>
<tr>
<td><code>[seq]</code></td>
<td>Соответствует любому символу из <code>seq</code>.<br>Например, <code>[abc]</code> соответствует <code>a</code>, <code>b</code>, или <code>c</code></td>
<td><code>"file[0-9].txt"</code> соответствует <code>"file1.txt"</code>, но не <code>"file12.txt"</code></td>
</tr>
<tr>
<td><code>[!seq]</code></td>
<td>Соответствует любому символу, который <strong>не</strong> входит в <code>seq</code>.<br>Например, <code>[!abc]</code> соответствует любому символу, кроме <code>a</code>, <code>b</code>, или <code>c</code></td>
<td><code>"file[!0-9].txt"</code> соответствует <code>"fileA.txt"</code>, но не <code>"file1.txt"</code></td>
</tr>
</tbody>
</table>
<h1>Примеры использования</h1>
<h3>Сопоставление строки с шаблоном</h3>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text class="unselectable">Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">fnmatch</span>

<span class="nb">print</span><span class="p">(</span><span class="n">fnmatch</span><span class="o">.</span><span class="n">fnmatch</span><span class="p">(</span><span class="s2">&quot;data.csv&quot;</span><span class="p">,</span> <span class="s2">&quot;*.csv&quot;</span><span class="p">))</span>  <span class="c1"># True</span>
<span class="nb">print</span><span class="p">(</span><span class="n">fnmatch</span><span class="o">.</span><span class="n">fnmatch</span><span class="p">(</span><span class="s2">&quot;data.txt&quot;</span><span class="p">,</span> <span class="s2">&quot;*.csv&quot;</span><span class="p">))</span>  <span class="c1"># False</span>
</pre></div></div></div>

<h3>Сопоставление с учетом регистра</h3>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text class="unselectable">Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">fnmatch</span>

<span class="nb">print</span><span class="p">(</span><span class="n">fnmatch</span><span class="o">.</span><span class="n">fnmatchcase</span><span class="p">(</span><span class="s2">&quot;Data.CSV&quot;</span><span class="p">,</span> <span class="s2">&quot;*.csv&quot;</span><span class="p">))</span>  <span class="c1"># False</span>
<span class="nb">print</span><span class="p">(</span><span class="n">fnmatch</span><span class="o">.</span><span class="n">fnmatchcase</span><span class="p">(</span><span class="s2">&quot;Data.CSV&quot;</span><span class="p">,</span> <span class="s2">&quot;*.CSV&quot;</span><span class="p">))</span>  <span class="c1"># True</span>
</pre></div></div></div>

<h3>Фильтрация списка файлов</h3>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text class="unselectable">Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">fnmatch</span>

<span class="n">files</span> <span class="o">=</span> <span class="p">[</span><span class="s2">&quot;data1.csv&quot;</span><span class="p">,</span> <span class="s2">&quot;data2.txt&quot;</span><span class="p">,</span> <span class="s2">&quot;data3.csv&quot;</span><span class="p">]</span>
<span class="n">csv_files</span> <span class="o">=</span> <span class="n">fnmatch</span><span class="o">.</span><span class="n">filter</span><span class="p">(</span><span class="n">files</span><span class="p">,</span> <span class="s2">&quot;*.csv&quot;</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">csv_files</span><span class="p">)</span>  <span class="c1"># [&quot;data1.csv&quot;, &quot;data3.csv&quot;]</span>
</pre></div></div></div>

<h3>Использование с регулярными выражениями</h3>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text class="unselectable">Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">fnmatch</span>
<span class="kn">import</span> <span class="nn">re</span>

<span class="n">pattern</span> <span class="o">=</span> <span class="n">fnmatch</span><span class="o">.</span><span class="n">translate</span><span class="p">(</span><span class="s2">&quot;*.txt&quot;</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">pattern</span><span class="p">)</span>  <span class="c1"># (?s:.*\.txt)\Z</span>

<span class="n">regex</span> <span class="o">=</span> <span class="n">re</span><span class="o">.</span><span class="n">compile</span><span class="p">(</span><span class="n">pattern</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">regex</span><span class="o">.</span><span class="n">match</span><span class="p">(</span><span class="s2">&quot;file.txt&quot;</span><span class="p">))</span>  <span class="c1"># &lt;re.Match object; span=(0, 8), match=&#39;file.txt&#39;&gt;</span>
<span class="nb">print</span><span class="p">(</span><span class="n">regex</span><span class="o">.</span><span class="n">match</span><span class="p">(</span><span class="s2">&quot;file.csv&quot;</span><span class="p">))</span>  <span class="c1"># None</span>
</pre></div></div></div>

<h2>Примечания</h2>
<ul>
<li>На Unix-системах функции <code>fnmatch()</code> и <code>fnmatchcase()</code> работают <strong>с учетом регистра</strong>, а на Windows они <strong>регистронезависимы</strong>.
Однако <code>fnmatchcase()</code> <strong>всегда учитывает регистр</strong>, независимо от платформы.</li>
<li>Используйте <code>fnmatch.translate()</code> для сложных сопоставлений, которые требуют регулярных выражений.</li>
</ul>
<h1>Полезные примеры</h1>
<h3>Сопоставление с шаблоном для нескольких расширений</h3>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text class="unselectable">Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">fnmatch</span>

<span class="n">files</span> <span class="o">=</span> <span class="p">[</span><span class="s2">&quot;report.doc&quot;</span><span class="p">,</span> <span class="s2">&quot;data.csv&quot;</span><span class="p">,</span> <span class="s2">&quot;image.png&quot;</span><span class="p">,</span> <span class="s2">&quot;script.py&quot;</span><span class="p">]</span>
<span class="n">docs</span> <span class="o">=</span> <span class="n">fnmatch</span><span class="o">.</span><span class="n">filter</span><span class="p">(</span><span class="n">files</span><span class="p">,</span> <span class="s2">&quot;*.[dc][so][cv]&quot;</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">docs</span><span class="p">)</span>  <span class="c1"># [&quot;report.doc&quot;, &quot;data.csv&quot;]</span>
</pre></div></div></div>

<h3>Фильтрация скрытых файлов (начинающихся с точки)</h3>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text class="unselectable">Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">fnmatch</span>

<span class="n">files</span> <span class="o">=</span> <span class="p">[</span><span class="s2">&quot;.bashrc&quot;</span><span class="p">,</span> <span class="s2">&quot;data.csv&quot;</span><span class="p">,</span> <span class="s2">&quot;.gitignore&quot;</span><span class="p">,</span> <span class="s2">&quot;script.py&quot;</span><span class="p">]</span>
<span class="n">hidden_files</span> <span class="o">=</span> <span class="n">fnmatch</span><span class="o">.</span><span class="n">filter</span><span class="p">(</span><span class="n">files</span><span class="p">,</span> <span class="s2">&quot;.*&quot;</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">hidden_files</span><span class="p">)</span>  <span class="c1"># [&quot;.bashrc&quot;, &quot;.gitignore&quot;]</span>
</pre></div></div></div>

<h1>Полезные ссылки</h1>
<ul>
<li><a href="https://docs.python.org/3/library/fnmatch.html">Официальная документация</a></li>
<li><a href="https://realpython.com/lessons/filename-matching/">Real Python - Guide to Filename Matching</a></li>
</ul>