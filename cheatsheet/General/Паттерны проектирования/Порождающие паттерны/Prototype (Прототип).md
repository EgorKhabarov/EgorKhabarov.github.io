<h3>Prototype (Прототип)</h3>
<p>Паттерн Прототип позволяет копировать объекты, не зависимо от их конкретных классов.
Это особенно полезно, когда создание нового объекта требует сложной или дорогостоящей инициализации.</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" onclick="copyCode(this)"><svg aria-hidden="true" xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><pre>Copy code</pre></button></div><div class="code"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">copy</span>

<span class="k">class</span> <span class="nc">Prototype</span><span class="p">:</span>
    <span class="k">def</span> <span class="nf">clone</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
        <span class="k">return</span> <span class="n">copy</span><span class="o">.</span><span class="n">deepcopy</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span>

<span class="k">class</span> <span class="nc">ConcretePrototype</span><span class="p">(</span><span class="n">Prototype</span><span class="p">):</span>
    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">attribute</span><span class="p">):</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">attribute</span> <span class="o">=</span> <span class="n">attribute</span>

    <span class="k">def</span> <span class="fm">__str__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
        <span class="k">return</span> <span class="sa">f</span><span class="s2">&quot;ConcretePrototype with attribute: </span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">attribute</span><span class="si">}</span><span class="s2">&quot;</span>

<span class="c1"># Использование</span>
<span class="n">prototype</span> <span class="o">=</span> <span class="n">ConcretePrototype</span><span class="p">(</span><span class="s2">&quot;Initial value&quot;</span><span class="p">)</span>
<span class="n">clone</span> <span class="o">=</span> <span class="n">prototype</span><span class="o">.</span><span class="n">clone</span><span class="p">()</span>
<span class="n">clone</span><span class="o">.</span><span class="n">attribute</span> <span class="o">=</span> <span class="s2">&quot;Changed value&quot;</span>
<span class="nb">print</span><span class="p">(</span><span class="n">prototype</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">clone</span><span class="p">)</span>
</pre></div></div></div>