<h1>Interpreter (Интерпретатор)</h1>
<p><strong>Описание</strong>: Определяет грамматику языка и интерпретирует предложения в этом языке.</p>
<p><strong>Когда использовать</strong>: Когда нужно анализировать и исполнять предложения в специфическом языке или грамматике.</p>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text class="unselectable">Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="k">class</span> <span class="nc">Expression</span><span class="p">:</span>
    <span class="k">def</span> <span class="nf">interpret</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">context</span><span class="p">):</span>
        <span class="k">pass</span>

<span class="k">class</span> <span class="nc">Number</span><span class="p">(</span><span class="n">Expression</span><span class="p">):</span>
    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">value</span><span class="p">):</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">value</span> <span class="o">=</span> <span class="n">value</span>

    <span class="k">def</span> <span class="nf">interpret</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">context</span><span class="p">):</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">value</span>

<span class="k">class</span> <span class="nc">Add</span><span class="p">(</span><span class="n">Expression</span><span class="p">):</span>
    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">left</span><span class="p">,</span> <span class="n">right</span><span class="p">):</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">left</span> <span class="o">=</span> <span class="n">left</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">right</span> <span class="o">=</span> <span class="n">right</span>

    <span class="k">def</span> <span class="nf">interpret</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">context</span><span class="p">):</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">left</span><span class="o">.</span><span class="n">interpret</span><span class="p">(</span><span class="n">context</span><span class="p">)</span> <span class="o">+</span> <span class="bp">self</span><span class="o">.</span><span class="n">right</span><span class="o">.</span><span class="n">interpret</span><span class="p">(</span><span class="n">context</span><span class="p">)</span>


<span class="n">context</span> <span class="o">=</span> <span class="p">{}</span>
<span class="n">expr</span> <span class="o">=</span> <span class="n">Add</span><span class="p">(</span><span class="n">Number</span><span class="p">(</span><span class="mi">3</span><span class="p">),</span> <span class="n">Number</span><span class="p">(</span><span class="mi">4</span><span class="p">))</span>
<span class="nb">print</span><span class="p">(</span><span class="n">expr</span><span class="o">.</span><span class="n">interpret</span><span class="p">(</span><span class="n">context</span><span class="p">))</span>  <span class="c1"># 7</span>
</pre></div></div></div>