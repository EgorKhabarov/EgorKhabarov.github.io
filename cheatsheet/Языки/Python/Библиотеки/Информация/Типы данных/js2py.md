<p>Библиотека "js2py" используется в Python для выполнения и интерпретации JavaScript-кода.
Она предоставляет возможность взаимодействия между Python и JavaScript, позволяя исполнять JavaScript-код внутри среды Python.</p>
<p>Таблица методов модуля "js2py":</p>
<table>
<thead>
<tr>
<th>Метод</th>
<th>Описание кратко</th>
</tr>
</thead>
<tbody>
<tr>
<td>eval_js()</td>
<td>Исполняет переданный JavaScript-код и возвращает его результат.</td>
</tr>
<tr>
<td>call()</td>
<td>Вызывает функцию JavaScript и передает ей аргументы.</td>
</tr>
<tr>
<td>set()</td>
<td>Устанавливает значение переменной JavaScript.</td>
</tr>
<tr>
<td>get()</td>
<td>Получает значение переменной JavaScript.</td>
</tr>
<tr>
<td>delete()</td>
<td>Удаляет переменную JavaScript.</td>
</tr>
</tbody>
</table>
<p>Список самых часто используемых методов, их краткое описание и</p>
<p>eval_js(): Исполняет переданный JavaScript-код и возвращает его результат.</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" id="code4115da5299e778f7e019f73ea83d2b8cb" onclick="copyCode(code4115da5299e778f7e019f73ea83d2b8c, code4115da5299e778f7e019f73ea83d2b8cb)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code4115da5299e778f7e019f73ea83d2b8c"><div class="highlight"><pre><span></span><span class="nb">print</span><span class="p">(</span><span class="n">eval_js</span><span class="p">(</span><span class="s2">&quot;1 + 2&quot;</span><span class="p">))</span>  <span class="c1"># Выводит: 3</span>
</pre></div></div></div>

<p>call(): Вызывает функцию JavaScript и передает ей аргументы.</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" id="code6d3b0e4f8e46f49f3b605a3ce531c018b" onclick="copyCode(code6d3b0e4f8e46f49f3b605a3ce531c018, code6d3b0e4f8e46f49f3b605a3ce531c018b)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code6d3b0e4f8e46f49f3b605a3ce531c018"><div class="highlight"><pre><span></span><span class="n">js_function</span> <span class="o">=</span> <span class="n">js2py</span><span class="o">.</span><span class="n">eval_js</span><span class="p">(</span><span class="s2">&quot;function add(a, b) { return a + b; }&quot;</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">call</span><span class="p">(</span><span class="n">js_function</span><span class="p">,</span> <span class="mi">2</span><span class="p">,</span> <span class="mi">3</span><span class="p">))</span>  <span class="c1"># Выводит: 5</span>
</pre></div></div></div>

<p>set(): Устанавливает значение переменной JavaScript.</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" id="code33283da2d1e2e25f27cdbf51ec275019b" onclick="copyCode(code33283da2d1e2e25f27cdbf51ec275019, code33283da2d1e2e25f27cdbf51ec275019b)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code33283da2d1e2e25f27cdbf51ec275019"><div class="highlight"><pre><span></span><span class="nb">set</span><span class="p">(</span><span class="s2">&quot;x&quot;</span><span class="p">,</span> <span class="mi">10</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">eval_js</span><span class="p">(</span><span class="s2">&quot;x&quot;</span><span class="p">))</span>  <span class="c1"># Выводит: 10</span>
</pre></div></div></div>

<p>get(): Получает значение переменной JavaScript.</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" id="codebb2d46fe4e5a9dcaa9e9814e534dd489b" onclick="copyCode(codebb2d46fe4e5a9dcaa9e9814e534dd489, codebb2d46fe4e5a9dcaa9e9814e534dd489b)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="codebb2d46fe4e5a9dcaa9e9814e534dd489"><div class="highlight"><pre><span></span><span class="n">eval_js</span><span class="p">(</span><span class="s2">&quot;var message = &#39;Hello, world!&#39;&quot;</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">get</span><span class="p">(</span><span class="s2">&quot;message&quot;</span><span class="p">))</span>  <span class="c1"># Выводит: Hello, world!</span>
</pre></div></div></div>

<p>delete(): Удаляет переменную JavaScript.</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" id="codeb55484f8edd5e89e7fd3e8ee5b9baa4ab" onclick="copyCode(codeb55484f8edd5e89e7fd3e8ee5b9baa4a, codeb55484f8edd5e89e7fd3e8ee5b9baa4ab)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="codeb55484f8edd5e89e7fd3e8ee5b9baa4a"><div class="highlight"><pre><span></span><span class="n">eval_js</span><span class="p">(</span><span class="s2">&quot;var x = 5;&quot;</span><span class="p">)</span>
<span class="n">delete</span><span class="p">(</span><span class="s2">&quot;x&quot;</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">eval_js</span><span class="p">(</span><span class="s2">&quot;x&quot;</span><span class="p">))</span>  <span class="c1"># Выводит: undefined</span>
</pre></div></div></div>