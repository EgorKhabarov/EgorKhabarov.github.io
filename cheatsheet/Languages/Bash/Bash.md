<h1>Bash</h1>
<table>
<thead>
<tr>
<th>Команда</th>
<th>Описание</th>
<th>Пример использования</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>echo</code></td>
<td>Вывод текста в консоль</td>
<td><code>echo "Hello, World!"</code></td>
</tr>
<tr>
<td><code>cd</code></td>
<td>Переход в директорию</td>
<td><code>cd /path/to/directory</code></td>
</tr>
<tr>
<td><code>pwd</code></td>
<td>Вывод текущей директории</td>
<td><code>pwd</code></td>
</tr>
<tr>
<td><code>ls</code></td>
<td>Список файлов и директорий</td>
<td><code>ls -l</code> (подробный список с правами доступа)</td>
</tr>
<tr>
<td><code>cp</code></td>
<td>Копирование файлов и директорий</td>
<td><code>cp source.txt destination.txt</code></td>
</tr>
<tr>
<td><code>mv</code></td>
<td>Перемещение или переименование файла/директории</td>
<td><code>mv oldname.txt newname.txt</code></td>
</tr>
<tr>
<td><code>rm</code></td>
<td>Удаление файлов или директорий</td>
<td><code>rm file.txt</code> (удаление файла), <code>rm -r dir</code> (директория)</td>
</tr>
<tr>
<td><code>mkdir</code></td>
<td>Создание новой директории</td>
<td><code>mkdir new_directory</code></td>
</tr>
<tr>
<td><code>touch</code></td>
<td>Создание пустого файла</td>
<td><code>touch newfile.txt</code></td>
</tr>
<tr>
<td><code>cat</code></td>
<td>Вывод содержимого файла</td>
<td><code>cat file.txt</code></td>
</tr>
<tr>
<td><code>man</code></td>
<td>Документация по команде (man pages)</td>
<td><code>man ls</code> (документация по <code>ls</code>)</td>
</tr>
</tbody>
</table>
<h1>Переменные</h1>
<div class="code_element"><div class="lang_line"><text>bash</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-bash"><div class="highlight"><pre><span></span><span class="nv">my_var</span><span class="o">=</span><span class="s2">&quot;Hello&quot;</span><span class="w">  </span><span class="c1"># (без пробелов вокруг &#x60;=&#x60;)</span>
<span class="nb">echo</span><span class="w"> </span><span class="nv">$my_var</span><span class="w">  </span><span class="c1"># &quot;Hello&quot;</span>
</pre></div></div></div>

<h1>Условия и операторы</h1>
<div class="code_element"><div class="lang_line"><text>bash</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-bash"><div class="highlight"><pre><span></span><span class="k">if</span><span class="w"> </span><span class="o">[</span><span class="w"> </span>условие<span class="w"> </span><span class="o">]</span><span class="p">;</span><span class="w"> </span><span class="k">then</span>
<span class="w">    </span><span class="c1"># код, если условие истинно</span>
<span class="k">else</span>
<span class="w">    </span><span class="c1"># код, если условие ложно</span>
<span class="k">fi</span>
</pre></div></div></div>

<div class="code_element"><div class="lang_line"><text>bash</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-bash"><div class="highlight"><pre><span></span><span class="k">if</span><span class="w"> </span><span class="o">[</span><span class="w"> </span>-f<span class="w"> </span><span class="s2">&quot;file.txt&quot;</span><span class="w"> </span><span class="o">]</span><span class="p">;</span><span class="w"> </span><span class="k">then</span>
<span class="w">    </span><span class="nb">echo</span><span class="w"> </span><span class="s2">&quot;Файл существует&quot;</span>
<span class="k">else</span>
<span class="w">    </span><span class="nb">echo</span><span class="w"> </span><span class="s2">&quot;Файл не существует&quot;</span>
<span class="k">fi</span>
</pre></div></div></div>

<h3>Операторы сравнения</h3>
<ul>
<li><code>-f</code> — существует ли файл</li>
<li><code>-d</code> — существует ли директория</li>
<li><code>-z</code> — пустая ли строка</li>
<li><code>=</code> — равенство строк</li>
<li><code>-lt</code>, <code>-gt</code>, <code>-eq</code> — меньше, больше, равно для чисел</li>
</ul>
<h1>Циклы</h1>
<div class="code_element"><div class="lang_line"><text>bash</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-bash"><div class="highlight"><pre><span></span><span class="k">for</span><span class="w"> </span>var<span class="w"> </span><span class="k">in</span><span class="w"> </span><span class="o">{</span><span class="m">1</span>..5<span class="o">}</span><span class="p">;</span><span class="w"> </span><span class="k">do</span>
<span class="w">    </span><span class="nb">echo</span><span class="w"> </span><span class="nv">$var</span>
<span class="k">done</span>
</pre></div></div></div>
<div class="code_element"><div class="lang_line"><text>bash</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-bash"><div class="highlight"><pre><span></span><span class="k">while</span><span class="w"> </span><span class="o">[</span><span class="w"> </span>условие<span class="w"> </span><span class="o">]</span><span class="p">;</span><span class="w"> </span><span class="k">do</span>
<span class="w">    </span><span class="c1"># действия</span>
<span class="k">done</span>
</pre></div></div></div>

<div class="code_element"><div class="lang_line"><text>bash</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-bash"><div class="highlight"><pre><span></span><span class="nv">counter</span><span class="o">=</span><span class="m">0</span>
<span class="k">while</span><span class="w"> </span><span class="o">[</span><span class="w"> </span><span class="nv">$counter</span><span class="w"> </span>-lt<span class="w"> </span><span class="m">3</span><span class="w"> </span><span class="o">]</span><span class="p">;</span><span class="w"> </span><span class="k">do</span>
<span class="w">    </span><span class="nb">echo</span><span class="w"> </span><span class="s2">&quot;Counter: </span><span class="nv">$counter</span><span class="s2">&quot;</span>
<span class="w">    </span><span class="nv">counter</span><span class="o">=</span><span class="k">$((</span><span class="nv">counter</span><span class="w"> </span><span class="o">+</span><span class="w"> </span><span class="m">1</span><span class="k">))</span>
<span class="k">done</span>
</pre></div></div></div>

<h1>Функции</h1>
<div class="code_element"><div class="lang_line"><text>bash</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-bash"><div class="highlight"><pre><span></span><span class="k">function</span><span class="w"> </span>имя_функции<span class="o">()</span><span class="w"> </span><span class="o">{</span>
<span class="w">    </span><span class="c1"># тело функции</span>
<span class="o">}</span>
</pre></div></div></div>

<div class="code_element"><div class="lang_line"><text>bash</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-bash"><div class="highlight"><pre><span></span><span class="k">function</span><span class="w"> </span>greet<span class="o">()</span><span class="w"> </span><span class="o">{</span>
<span class="w">    </span><span class="nb">echo</span><span class="w"> </span><span class="s2">&quot;Привет, </span><span class="nv">$1</span><span class="s2">!&quot;</span>
<span class="o">}</span>

greet<span class="w"> </span><span class="s2">&quot;Мир&quot;</span><span class="w">  </span><span class="c1"># Выведет &quot;Привет, Мир!&quot;</span>
</pre></div></div></div>

<h1>Перенаправление ввода/вывода</h1>
<h3>&gt;</h3>
<p>Перенаправление вывода в файл (перезаписывает файл).</p>
<div class="code_element"><div class="lang_line"><text>bash</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-bash"><div class="highlight"><pre><span></span><span class="nb">echo</span><span class="w"> </span><span class="s2">&quot;Текст&quot;</span><span class="w"> </span>&gt;<span class="w"> </span>output.txt
</pre></div></div></div>

<h3>&gt;&gt;</h3>
<p>Перенаправление вывода в файл (добавляет к файлу).</p>
<div class="code_element"><div class="lang_line"><text>bash</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-bash"><div class="highlight"><pre><span></span><span class="nb">echo</span><span class="w"> </span><span class="s2">&quot;Еще текст&quot;</span><span class="w"> </span>&gt;&gt;<span class="w"> </span>output.txt
</pre></div></div></div>

<h3>&lt;</h3>
<p>Перенаправление ввода из файла.</p>
<div class="code_element"><div class="lang_line"><text>bash</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-bash"><div class="highlight"><pre><span></span>cat<span class="w"> </span>&lt;<span class="w"> </span>input.txt
</pre></div></div></div>

<h3>2&gt;</h3>
<p>Перенаправление ошибок в файл.</p>
<div class="code_element"><div class="lang_line"><text>bash</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-bash"><div class="highlight"><pre><span></span>ls<span class="w"> </span>несуществующий_файл<span class="w"> </span><span class="m">2</span>&gt;<span class="w"> </span>errors.txt
</pre></div></div></div>

<h3>&amp;&gt;</h3>
<p>Перенаправление как стандартного вывода, так и ошибок.</p>
<div class="code_element"><div class="lang_line"><text>bash</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-bash"><div class="highlight"><pre><span></span>команда<span class="w"> </span><span class="p">&amp;</span>&gt;<span class="w"> </span>output_and_errors.txt
</pre></div></div></div>

<h1>Пайплайн (Pipeline)</h1>
<p>Пайплайн используется для передачи вывода одной команды как ввода другой команды</p>
<div class="code_element"><div class="lang_line"><text>bash</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-bash"><div class="highlight"><pre><span></span>cat<span class="w"> </span>file.txt<span class="w"> </span><span class="p">|</span><span class="w"> </span>grep<span class="w"> </span><span class="s2">&quot;pattern&quot;</span>
</pre></div></div></div>

<h1>Аргументы командной строки</h1>
<ul>
<li><code>$0</code> — имя скрипта.</li>
<li><code>$1</code>, <code>$2</code>, ..., <code>$N</code> — аргументы командной строки.</li>
<li><code>$#</code> — количество аргументов.</li>
<li><code>$@</code> — все аргументы.</li>
</ul>
<p>Пример скрипта, который выводит все аргументы:</p>
<div class="code_element"><div class="lang_line"><text>bash</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-bash"><div class="highlight"><pre><span></span><span class="ch">#!/bin/bash</span>
<span class="nb">echo</span><span class="w"> </span><span class="s2">&quot;Имя скрипта: </span><span class="nv">$0</span><span class="s2">&quot;</span>
<span class="nb">echo</span><span class="w"> </span><span class="s2">&quot;Первый аргумент: </span><span class="nv">$1</span><span class="s2">&quot;</span>
<span class="nb">echo</span><span class="w"> </span><span class="s2">&quot;Количество аргументов: </span><span class="nv">$#</span><span class="s2">&quot;</span>
</pre></div></div></div>

<h1>Массивы</h1>
<h3>Создание массива</h3>
<div class="code_element"><div class="lang_line"><text>bash</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-bash"><div class="highlight"><pre><span></span><span class="nv">my_array</span><span class="o">=(</span>one<span class="w"> </span>two<span class="w"> </span>three<span class="o">)</span>
</pre></div></div></div>

<h3>Доступ к элементам массива</h3>
<div class="code_element"><div class="lang_line"><text>bash</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-bash"><div class="highlight"><pre><span></span><span class="nb">echo</span><span class="w"> </span><span class="si">${</span><span class="nv">my_array</span><span class="p">[0]</span><span class="si">}</span><span class="w">  </span><span class="c1"># Первый элемент</span>
</pre></div></div></div>

<h3>Все элементы массива</h3>
<div class="code_element"><div class="lang_line"><text>bash</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-bash"><div class="highlight"><pre><span></span><span class="nb">echo</span><span class="w"> </span><span class="si">${</span><span class="nv">my_array</span><span class="p">[@]</span><span class="si">}</span>
</pre></div></div></div>

<h1>Специальные символы</h1>
<table>
<thead>
<tr>
<th>Символ</th>
<th>Описание</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>#</code></td>
<td>Комментарий</td>
</tr>
<tr>
<td><code>;</code></td>
<td>Разделение нескольких команд на одной строке</td>
</tr>
<tr>
<td><code>&amp;&amp;</code></td>
<td>Логическое И (следующая команда выполняется, если предыдущая завершилась успешно)</td>
</tr>
<tr>
<td><code>||</code></td>
<td>Логическое ИЛИ (следующая команда выполняется, если предыдущая завершилась неудачно)</td>
</tr>
<tr>
<td><code>&amp;</code></td>
<td>Запуск команды в фоновом режиме</td>
</tr>
<tr>
<td><code>`</code></td>
<td>Выполнение команды и подстановка её результата</td>
</tr>
</tbody>
</table>
<h1>Управление процессами</h1>
<ul>
<li><strong>Запуск команды в фоне</strong>: <code>command &amp;</code></li>
<li><strong>Просмотр всех процессов</strong>: <code>ps</code></li>
<li><strong>Завершение процесса</strong>: <code>kill PID</code></li>
</ul>
<h1>Пример</h1>
<div class="code_element"><div class="lang_line"><text>bash</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-bash"><div class="highlight"><pre><span></span><span class="ch">#!/bin/bash</span>

<span class="c1"># Этот скрипт приветствует пользователя</span>
<span class="nb">echo</span><span class="w"> </span><span class="s2">&quot;Как вас зовут?&quot;</span>
<span class="nb">read</span><span class="w"> </span>name
<span class="nb">echo</span><span class="w"> </span><span class="s2">&quot;Привет, </span><span class="nv">$name</span><span class="s2">!&quot;</span>

<span class="c1"># Проверка наличия файла</span>
<span class="k">if</span><span class="w"> </span><span class="o">[</span><span class="w"> </span>-f<span class="w"> </span><span class="s2">&quot;example.txt&quot;</span><span class="w"> </span><span class="o">]</span><span class="p">;</span><span class="w"> </span><span class="k">then</span>
<span class="w">    </span><span class="nb">echo</span><span class="w"> </span><span class="s2">&quot;Файл example.txt существует.&quot;</span>
<span class="k">else</span>
<span class="w">    </span><span class="nb">echo</span><span class="w"> </span><span class="s2">&quot;Файл example.txt не найден.&quot;</span>
<span class="k">fi</span>

<span class="c1"># Цикл по списку</span>
<span class="k">for</span><span class="w"> </span>i<span class="w"> </span><span class="k">in</span><span class="w"> </span><span class="o">{</span><span class="m">1</span>..5<span class="o">}</span><span class="p">;</span><span class="w"> </span><span class="k">do</span>
<span class="w">    </span><span class="nb">echo</span><span class="w"> </span><span class="s2">&quot;Цикл номер </span><span class="nv">$i</span><span class="s2">&quot;</span>
<span class="k">done</span>
</pre></div></div></div>

<h1>Полезные команды</h1>
<ul>
<li><code>grep</code> — Поиск текста в файле</li>
</ul>
<div class="code_element"><div class="lang_line"><text>bash</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-bash"><div class="highlight"><pre><span></span>grep<span class="w"> </span><span class="s2">&quot;pattern&quot;</span><span class="w"> </span>file.txt
</pre></div></div></div>

<ul>
<li><code>find</code> — Поиск файлов и директорий</li>
</ul>
<div class="code_element"><div class="lang_line"><text>bash</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-bash"><div class="highlight"><pre><span></span>find<span class="w"> </span>/path<span class="w"> </span>-name<span class="w"> </span><span class="s2">&quot;*.txt&quot;</span>
</pre></div></div></div>

<ul>
<li><code>chmod</code> — Изменение прав доступа к файлу</li>
</ul>
<div class="code_element"><div class="lang_line"><text>bash</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-bash"><div class="highlight"><pre><span></span>chmod<span class="w"> </span>+x<span class="w"> </span>script.sh<span class="w">  </span><span class="c1"># Сделать файл исполняемым</span>
</pre></div></div></div>

<ul>
<li><code>tar</code> — Архивация файлов</li>
</ul>
<div class="code_element"><div class="lang_line"><text>bash</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-bash"><div class="highlight"><pre><span></span>tar<span class="w"> </span>-cvf<span class="w"> </span>archive.tar<span class="w"> </span>directory/
</pre></div></div></div>

<ul>
<li><code>curl</code> — Запросы по HTTP</li>
</ul>
<div class="code_element"><div class="lang_line"><text>bash</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-bash"><div class="highlight"><pre><span></span>curl<span class="w"> </span>http://example.com
</pre></div></div></div>