<h2>Strategy (Стратегия)</h2>
<p><strong>Описание:</strong> Определяет семейство алгоритмов, инкапсулирует каждый из них и делает их взаимозаменяемыми.
Позволяет изменять алгоритм независимо от клиентов, которые им пользуются.</p>
<p><strong>Когда использовать:</strong> Когда у вас есть несколько схожих алгоритмов,
и необходимо переключаться между ними в зависимости от условий.</p>
<p><strong>Пример реализации:</strong></p>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="k">class</span> <span class="nc">Strategy</span><span class="p">:</span>
    <span class="k">def</span> <span class="nf">execute</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">data</span><span class="p">):</span>
        <span class="k">raise</span> <span class="ne">NotImplementedError</span>

<span class="k">class</span> <span class="nc">ConcreteStrategyA</span><span class="p">(</span><span class="n">Strategy</span><span class="p">):</span>
    <span class="k">def</span> <span class="nf">execute</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">data</span><span class="p">):</span>
        <span class="k">return</span> <span class="nb">sorted</span><span class="p">(</span><span class="n">data</span><span class="p">)</span>

<span class="k">class</span> <span class="nc">ConcreteStrategyB</span><span class="p">(</span><span class="n">Strategy</span><span class="p">):</span>
    <span class="k">def</span> <span class="nf">execute</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">data</span><span class="p">):</span>
        <span class="k">return</span> <span class="nb">sorted</span><span class="p">(</span><span class="n">data</span><span class="p">,</span> <span class="n">reverse</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>

<span class="k">class</span> <span class="nc">Context</span><span class="p">:</span>
    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">strategy</span><span class="p">:</span> <span class="n">Strategy</span><span class="p">):</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_strategy</span> <span class="o">=</span> <span class="n">strategy</span>

    <span class="k">def</span> <span class="nf">do_some_business_logic</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">data</span><span class="p">):</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_strategy</span><span class="o">.</span><span class="n">execute</span><span class="p">(</span><span class="n">data</span><span class="p">)</span>

<span class="n">context</span> <span class="o">=</span> <span class="n">Context</span><span class="p">(</span><span class="n">ConcreteStrategyA</span><span class="p">())</span>
<span class="nb">print</span><span class="p">(</span><span class="n">context</span><span class="o">.</span><span class="n">do_some_business_logic</span><span class="p">([</span><span class="mi">3</span><span class="p">,</span> <span class="mi">1</span><span class="p">,</span> <span class="mi">2</span><span class="p">]))</span>  <span class="c1"># Вывод: [1, 2, 3]</span>

<span class="n">context</span> <span class="o">=</span> <span class="n">Context</span><span class="p">(</span><span class="n">ConcreteStrategyB</span><span class="p">())</span>
<span class="nb">print</span><span class="p">(</span><span class="n">context</span><span class="o">.</span><span class="n">do_some_business_logic</span><span class="p">([</span><span class="mi">3</span><span class="p">,</span> <span class="mi">1</span><span class="p">,</span> <span class="mi">2</span><span class="p">]))</span>  <span class="c1"># Вывод: [3, 2, 1]</span>
</pre></div></div></div>