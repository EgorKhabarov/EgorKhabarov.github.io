<p>Модуль atexit в Python предоставляет возможность регистрации функций,
которые будут выполнены при завершении программы.
Это позволяет управлять завершением программы и выполнением дополнительных действий перед выходом.</p>
<table>
<thead>
<tr>
<th>Метод/Подмодуль</th>
<th>Описание</th>
</tr>
</thead>
<tbody>
<tr>
<td>atexit.register(func)</td>
<td>Регистрирует функцию func для выполнения при выходе из программы.</td>
</tr>
</tbody>
</table>
<p><strong>atexit.register(func)</strong> Регистрирует функцию для выполнения при выходе из программы.</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button"id="code8647a861d5b39a218e88b12240fad9c6b"onclick="copyCode(code8647a861d5b39a218e88b12240fad9c6, code8647a861d5b39a218e88b12240fad9c6b)"><svg stroke="currentColor"fill="none"stroke-width="2"viewBox="0 0 24 24"stroke-linecap="round"stroke-linejoin="round"class="h-4 w-4"height="1em"width="1em"xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code8647a861d5b39a218e88b12240fad9c6"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">atexit</span>

<span class="k">def</span> <span class="nf">exit_handler</span><span class="p">():</span>
    <span class="nb">print</span><span class="p">(</span><span class="s2">&quot;Выход из программы&quot;</span><span class="p">)</span>

<span class="n">atexit</span><span class="o">.</span><span class="n">register</span><span class="p">(</span><span class="n">exit_handler</span><span class="p">)</span>
</pre></div></div></div>