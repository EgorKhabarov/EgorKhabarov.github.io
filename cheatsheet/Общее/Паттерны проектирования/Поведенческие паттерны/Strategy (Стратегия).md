<h2>Strategy (Стратегия)</h2>
<p><strong>Описание:</strong> Определяет семейство алгоритмов, инкапсулирует каждый из них и делает их взаимозаменяемыми.
Позволяет изменять алгоритм независимо от клиентов, которые им пользуются.</p>
<p><strong>Когда использовать:</strong> Когда у вас есть несколько схожих алгоритмов,
и необходимо переключаться между ними в зависимости от условий.</p>
<p><strong>Пример реализации:</strong></p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button"id="codee9b1b9aabd56885d95efa2c9d3873bb5b"onclick="copyCode(codee9b1b9aabd56885d95efa2c9d3873bb5, codee9b1b9aabd56885d95efa2c9d3873bb5b)"><svg stroke="currentColor"fill="none"stroke-width="2"viewBox="0 0 24 24"stroke-linecap="round"stroke-linejoin="round"class="h-4 w-4"height="1em"width="1em"xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="codee9b1b9aabd56885d95efa2c9d3873bb5"><div class="highlight"><pre><span></span><span class="k">class</span> <span class="nc">Strategy</span><span class="p">:</span>
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