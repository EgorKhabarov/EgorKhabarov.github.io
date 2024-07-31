<h2>Decorator (Декоратор)</h2>
<p><strong>Описание:</strong> Позволяет динамически добавлять новое поведение объектам, оборачивая их в класс-оболочку.</p>
<p><strong>Когда использовать:</strong> Когда нужно добавлять дополнительные функциональности объектам без изменения их класса.</p>
<p><strong>Пример реализации:</strong></p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button"id="codeb25ad19ef15cffe11f9d4862a2215483b"onclick="copyCode(codeb25ad19ef15cffe11f9d4862a2215483, codeb25ad19ef15cffe11f9d4862a2215483b)"><svg stroke="currentColor"fill="none"stroke-width="2"viewBox="0 0 24 24"stroke-linecap="round"stroke-linejoin="round"class="h-4 w-4"height="1em"width="1em"xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="codeb25ad19ef15cffe11f9d4862a2215483"><div class="highlight"><pre><span></span><span class="k">class</span> <span class="nc">Component</span><span class="p">:</span>
    <span class="k">def</span> <span class="nf">operation</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
        <span class="k">pass</span>

<span class="k">class</span> <span class="nc">ConcreteComponent</span><span class="p">(</span><span class="n">Component</span><span class="p">):</span>
    <span class="k">def</span> <span class="nf">operation</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
        <span class="k">return</span> <span class="s2">&quot;ConcreteComponent&quot;</span>

<span class="k">class</span> <span class="nc">Decorator</span><span class="p">(</span><span class="n">Component</span><span class="p">):</span>
    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">component</span><span class="p">):</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_component</span> <span class="o">=</span> <span class="n">component</span>

    <span class="k">def</span> <span class="nf">operation</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
        <span class="k">return</span> <span class="sa">f</span><span class="s2">&quot;Decorator(</span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">_component</span><span class="o">.</span><span class="n">operation</span><span class="p">()</span><span class="si">}</span><span class="s2">)&quot;</span>

<span class="n">component</span> <span class="o">=</span> <span class="n">ConcreteComponent</span><span class="p">()</span>
<span class="n">decorated</span> <span class="o">=</span> <span class="n">Decorator</span><span class="p">(</span><span class="n">component</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">decorated</span><span class="o">.</span><span class="n">operation</span><span class="p">())</span>  <span class="c1"># Вывод: &quot;Decorator(ConcreteComponent)&quot;</span>
</pre></div></div></div>