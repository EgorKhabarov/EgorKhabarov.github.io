<h1>State (Состояние)</h1>
<p><strong>Описание</strong>: Позволяет объекту изменять своё поведение в зависимости от внутреннего состояния, меняя свой класс.</p>
<p><strong>Когда использовать</strong>: Когда объект может находиться в одном из нескольких состояний, и поведение объекта меняется в зависимости от его состояния.</p>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="k">class</span> <span class="nc">State</span><span class="p">:</span>
    <span class="k">def</span> <span class="nf">handle</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">context</span><span class="p">):</span>
        <span class="k">pass</span>

<span class="k">class</span> <span class="nc">ConcreteStateA</span><span class="p">(</span><span class="n">State</span><span class="p">):</span>
    <span class="k">def</span> <span class="nf">handle</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">context</span><span class="p">):</span>
        <span class="n">context</span><span class="o">.</span><span class="n">state</span> <span class="o">=</span> <span class="n">ConcreteStateB</span><span class="p">()</span>
        <span class="nb">print</span><span class="p">(</span><span class="s2">&quot;Transition to ConcreteStateB&quot;</span><span class="p">)</span>

<span class="k">class</span> <span class="nc">ConcreteStateB</span><span class="p">(</span><span class="n">State</span><span class="p">):</span>
    <span class="k">def</span> <span class="nf">handle</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">context</span><span class="p">):</span>
        <span class="n">context</span><span class="o">.</span><span class="n">state</span> <span class="o">=</span> <span class="n">ConcreteStateA</span><span class="p">()</span>
        <span class="nb">print</span><span class="p">(</span><span class="s2">&quot;Transition to ConcreteStateA&quot;</span><span class="p">)</span>

<span class="k">class</span> <span class="nc">Context</span><span class="p">:</span>
    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">state</span><span class="p">):</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">state</span> <span class="o">=</span> <span class="n">state</span>

    <span class="k">def</span> <span class="nf">request</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">state</span><span class="o">.</span><span class="n">handle</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span>


<span class="n">context</span> <span class="o">=</span> <span class="n">Context</span><span class="p">(</span><span class="n">ConcreteStateA</span><span class="p">())</span>
<span class="n">context</span><span class="o">.</span><span class="n">request</span><span class="p">()</span>  <span class="c1"># Transition to ConcreteStateB</span>
<span class="n">context</span><span class="o">.</span><span class="n">request</span><span class="p">()</span>  <span class="c1"># Transition to ConcreteStateA</span>
</pre></div></div></div>