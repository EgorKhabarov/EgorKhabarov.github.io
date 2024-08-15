<h2>Декораторы</h2>
<p>Специальные функции, которые позволяют модифицировать поведение других функций.
Они часто используются для добавления нового функционала к существующим функциям без изменения их кода.</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" onclick="copyCode(this)"><svg aria-hidden="true" xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><pre>Copy code</pre></button></div><div class="code"><div class="highlight"><pre><span></span><span class="k">def</span> <span class="nf">cache_decorator</span><span class="p">(</span><span class="n">func</span><span class="p">):</span>
    <span class="n">cache</span> <span class="o">=</span> <span class="p">{}</span>
    <span class="k">def</span> <span class="nf">wrapper</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
        <span class="n">key</span> <span class="o">=</span> <span class="sa">f</span><span class="s2">&quot;</span><span class="si">{</span><span class="n">args</span><span class="si">}</span><span class="s2">:</span><span class="si">{</span><span class="n">kwargs</span><span class="si">}</span><span class="s2">&quot;</span>
        <span class="k">if</span> <span class="n">key</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">cache</span><span class="p">:</span>
            <span class="n">cache</span><span class="p">[</span><span class="n">key</span><span class="p">]</span> <span class="o">=</span> <span class="n">func</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
        <span class="k">return</span> <span class="n">cache</span><span class="p">[</span><span class="n">key</span><span class="p">]</span>
    <span class="k">return</span> <span class="n">wrapper</span>

<span class="nd">@cache_decorator</span>
<span class="k">def</span> <span class="nf">expensive_function</span><span class="p">(</span><span class="n">x</span><span class="p">):</span>
    <span class="c1"># дорогая расчетная функция</span>
    <span class="k">return</span> <span class="n">x</span><span class="o">**</span><span class="mi">2</span>

<span class="nb">print</span><span class="p">(</span><span class="n">expensive_function</span><span class="p">(</span><span class="mi">2</span><span class="p">))</span>  <span class="c1"># 4</span>
<span class="nb">print</span><span class="p">(</span><span class="n">expensive_function</span><span class="p">(</span><span class="mi">2</span><span class="p">))</span>  <span class="c1"># 4 (значение берется из кеша)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">expensive_function</span><span class="p">(</span><span class="mi">3</span><span class="p">))</span>  <span class="c1"># 9</span>
<span class="nb">print</span><span class="p">(</span><span class="n">expensive_function</span><span class="p">(</span><span class="mi">3</span><span class="p">))</span>  <span class="c1"># 9 (значение берется из кеша)</span>
</pre></div></div></div>

<h2>closure (Замыкания)</h2>
<p>Функции, которые ссылаются на переменные, определенные вне этой функции.
Они позволяют сохранять состояние переменных между вызовами функции.
Замыкания часто используются в Python для создания функций-генераторов,
которые возвращают новые функции с измененными параметрами.</p>
<p>Например, следующий код создает функцию-генератор, которая возвращает
функции, увеличивающие число на указанное значение:</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" onclick="copyCode(this)"><svg aria-hidden="true" xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><pre>Copy code</pre></button></div><div class="code"><div class="highlight"><pre><span></span><span class="k">def</span> <span class="nf">make_incrementor</span><span class="p">(</span><span class="n">n</span><span class="p">):</span>
    <span class="k">def</span> <span class="nf">incrementor</span><span class="p">(</span><span class="n">x</span><span class="p">):</span>
        <span class="k">return</span> <span class="n">x</span> <span class="o">+</span> <span class="n">n</span>
    <span class="k">return</span> <span class="n">incrementor</span>

<span class="n">plus_3</span> <span class="o">=</span> <span class="n">make_incrementor</span><span class="p">(</span><span class="mi">3</span><span class="p">)</span>
<span class="n">plus_5</span> <span class="o">=</span> <span class="n">make_incrementor</span><span class="p">(</span><span class="mi">5</span><span class="p">)</span>

<span class="nb">print</span><span class="p">(</span><span class="n">plus_3</span><span class="p">(</span><span class="mi">10</span><span class="p">))</span>  <span class="c1"># 13</span>
<span class="nb">print</span><span class="p">(</span><span class="n">plus_5</span><span class="p">(</span><span class="mi">10</span><span class="p">))</span>  <span class="c1"># 15</span>
</pre></div></div></div>