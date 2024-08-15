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
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" onclick="copyCode(this)"><svg aria-hidden="true" xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><pre>Copy code</pre></button></div><div class="code"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">atexit</span>

<span class="k">def</span> <span class="nf">exit_handler</span><span class="p">():</span>
    <span class="nb">print</span><span class="p">(</span><span class="s2">&quot;Выход из программы&quot;</span><span class="p">)</span>

<span class="n">atexit</span><span class="o">.</span><span class="n">register</span><span class="p">(</span><span class="n">exit_handler</span><span class="p">)</span>
</pre></div></div></div>