<h1>Strategy (Стратегия)</h1>
<p><strong>Описание</strong>: Определяет семейство алгоритмов, инкапсулирует их и делает их взаимозаменяемыми.</p>
<p><strong>Когда использовать</strong>: Когда нужно выбрать один из нескольких алгоритмов на этапе выполнения программы.</p>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text class="unselectable">Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="k">class</span> <span class="nc">Strategy</span><span class="p">:</span>
    <span class="k">def</span> <span class="nf">execute</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">a</span><span class="p">,</span> <span class="n">b</span><span class="p">):</span>
        <span class="k">pass</span>

<span class="k">class</span> <span class="nc">AddStrategy</span><span class="p">(</span><span class="n">Strategy</span><span class="p">):</span>
    <span class="k">def</span> <span class="nf">execute</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">a</span><span class="p">,</span> <span class="n">b</span><span class="p">):</span>
        <span class="k">return</span> <span class="n">a</span> <span class="o">+</span> <span class="n">b</span>

<span class="k">class</span> <span class="nc">MultiplyStrategy</span><span class="p">(</span><span class="n">Strategy</span><span class="p">):</span>
    <span class="k">def</span> <span class="nf">execute</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">a</span><span class="p">,</span> <span class="n">b</span><span class="p">):</span>
        <span class="k">return</span> <span class="n">a</span> <span class="o">*</span> <span class="n">b</span>

<span class="k">class</span> <span class="nc">Context</span><span class="p">:</span>
    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">strategy</span><span class="p">):</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">strategy</span> <span class="o">=</span> <span class="n">strategy</span>

    <span class="k">def</span> <span class="nf">execute_strategy</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">a</span><span class="p">,</span> <span class="n">b</span><span class="p">):</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">strategy</span><span class="o">.</span><span class="n">execute</span><span class="p">(</span><span class="n">a</span><span class="p">,</span> <span class="n">b</span><span class="p">)</span>


<span class="n">context</span> <span class="o">=</span> <span class="n">Context</span><span class="p">(</span><span class="n">AddStrategy</span><span class="p">())</span>
<span class="nb">print</span><span class="p">(</span><span class="n">context</span><span class="o">.</span><span class="n">execute_strategy</span><span class="p">(</span><span class="mi">5</span><span class="p">,</span> <span class="mi">3</span><span class="p">))</span>  <span class="c1"># 8</span>

<span class="n">context</span> <span class="o">=</span> <span class="n">Context</span><span class="p">(</span><span class="n">MultiplyStrategy</span><span class="p">())</span>
<span class="nb">print</span><span class="p">(</span><span class="n">context</span><span class="o">.</span><span class="n">execute_strategy</span><span class="p">(</span><span class="mi">5</span><span class="p">,</span> <span class="mi">3</span><span class="p">))</span>  <span class="c1"># 15</span>
</pre></div></div></div>