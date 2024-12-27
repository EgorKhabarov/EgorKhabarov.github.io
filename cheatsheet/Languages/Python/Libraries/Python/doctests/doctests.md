<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text class="unselectable">Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="k">def</span> <span class="nf">add</span><span class="p">(</span><span class="n">a</span><span class="p">,</span> <span class="n">b</span><span class="p">):</span>
<span class="w">    </span><span class="sd">&quot;&quot;&quot;</span>
<span class="sd">    Возвращает сумму двух чисел.</span>

<span class="sd">    &gt;&gt;&gt; add(2, 3)</span>
<span class="sd">    5</span>
<span class="sd">    &gt;&gt;&gt; add(0, 0)</span>
<span class="sd">    0</span>
<span class="sd">    &gt;&gt;&gt; add(-1, 1)</span>
<span class="sd">    0</span>
<span class="sd">    &quot;&quot;&quot;</span>
    <span class="k">return</span> <span class="n">a</span> <span class="o">+</span> <span class="n">b</span>

<span class="k">if</span> <span class="vm">__name__</span> <span class="o">==</span> <span class="s2">&quot;__main__&quot;</span><span class="p">:</span>
    <span class="kn">import</span> <span class="nn">doctest</span>
    <span class="n">doctest</span><span class="o">.</span><span class="n">testmod</span><span class="p">()</span>
</pre></div></div></div>

<h1>Основные функции и методы</h1>
<table>
<thead>
<tr>
<th>Функция/Метод</th>
<th>Описание</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>doctest.testmod()</code></td>
<td>Тестирует текущий модуль, ищет и выполняет doctests, написанные в docstring</td>
</tr>
<tr>
<td><code>doctest.run_docstring_examples()</code></td>
<td>Запускает примеры doctest для указанной функции или объекта</td>
</tr>
<tr>
<td><code>doctest.ELLIPSIS</code></td>
<td>Разрешает использование "..." в примерах для пропуска некоторых частей вывода</td>
</tr>
<tr>
<td><code>doctest.FAIL_FAST</code></td>
<td>Прекращает выполнение тестов после первой ошибки</td>
</tr>
<tr>
<td><code>doctest.IGNORE_EXCEPTION_DETAIL</code></td>
<td>Игнорирует различия в деталях ошибок при проверке исключений</td>
</tr>
</tbody>
</table>
<h3>Пример с исключением и использованием опций</h3>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text class="unselectable">Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="k">def</span> <span class="nf">divide</span><span class="p">(</span><span class="n">a</span><span class="p">,</span> <span class="n">b</span><span class="p">):</span>
<span class="w">    </span><span class="sd">&quot;&quot;&quot;</span>
<span class="sd">    Делит число a на b.</span>

<span class="sd">    Пример:</span>
<span class="sd">    &gt;&gt;&gt; divide(4, 2)</span>
<span class="sd">    2.0</span>
<span class="sd">    &gt;&gt;&gt; divide(4, 0)</span>
<span class="sd">    Traceback (most recent call last):</span>
<span class="sd">        ...</span>
<span class="sd">    ZeroDivisionError: division by zero</span>
<span class="sd">    &quot;&quot;&quot;</span>
    <span class="k">return</span> <span class="n">a</span> <span class="o">/</span> <span class="n">b</span>

<span class="k">if</span> <span class="vm">__name__</span> <span class="o">==</span> <span class="s2">&quot;__main__&quot;</span><span class="p">:</span>
    <span class="kn">import</span> <span class="nn">doctest</span>
    <span class="n">doctest</span><span class="o">.</span><span class="n">testmod</span><span class="p">(</span><span class="n">optionflags</span><span class="o">=</span><span class="n">doctest</span><span class="o">.</span><span class="n">ELLIPSIS</span><span class="p">)</span>
</pre></div></div></div>

<h1>Как запускать</h1>
<h3>Через код</h3>
<p>Включить <code>doctest.testmod()</code> в своем коде.</p>
<h3>Через командную строку</h3>
<p>Ключ <code>-v</code> (verbose) выводит подробные результаты выполнения тестов.</p>
<div class="code_element"><div class="lang_line"><text>bash</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text class="unselectable">Copy code</text></button></div><div class="code language-bash"><div class="highlight"><pre><span></span>python<span class="w"> </span>-m<span class="w"> </span>doctest<span class="w"> </span>-v<span class="w"> </span>your_script.py
</pre></div></div></div>

<h3>Пример с обработкой ошибок</h3>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text class="unselectable">Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="k">def</span> <span class="nf">safe_divide</span><span class="p">(</span><span class="n">a</span><span class="p">,</span> <span class="n">b</span><span class="p">):</span>
<span class="w">    </span><span class="sd">&quot;&quot;&quot;</span>
<span class="sd">    Делит a на b, возвращает 0, если деление на 0.</span>

<span class="sd">    &gt;&gt;&gt; safe_divide(4, 2)</span>
<span class="sd">    2.0</span>
<span class="sd">    &gt;&gt;&gt; safe_divide(4, 0)</span>
<span class="sd">    0</span>
<span class="sd">    &quot;&quot;&quot;</span>
    <span class="k">try</span><span class="p">:</span>
        <span class="k">return</span> <span class="n">a</span> <span class="o">/</span> <span class="n">b</span>
    <span class="k">except</span> <span class="ne">ZeroDivisionError</span><span class="p">:</span>
        <span class="k">return</span> <span class="mi">0</span>
</pre></div></div></div>