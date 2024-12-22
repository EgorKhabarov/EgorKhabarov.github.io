<h1>Bridge (Мост)</h1>
<p><strong>Описание</strong>: Разделяет абстракцию и реализацию, позволяя изменять их независимо друг от друга.</p>
<p><strong>Когда использовать</strong>: Когда нужно разделить абстракцию и реализацию для независимой модификации и избежать жесткой связанности.</p>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text class="unselectable">Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="k">class</span> <span class="nc">Implementation</span><span class="p">:</span>
    <span class="k">def</span> <span class="nf">operation</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
        <span class="k">pass</span>

<span class="k">class</span> <span class="nc">ConcreteImplementationA</span><span class="p">(</span><span class="n">Implementation</span><span class="p">):</span>
    <span class="k">def</span> <span class="nf">operation</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
        <span class="k">return</span> <span class="s2">&quot;Implementation A&quot;</span>

<span class="k">class</span> <span class="nc">ConcreteImplementationB</span><span class="p">(</span><span class="n">Implementation</span><span class="p">):</span>
    <span class="k">def</span> <span class="nf">operation</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
        <span class="k">return</span> <span class="s2">&quot;Implementation B&quot;</span>

<span class="k">class</span> <span class="nc">Abstraction</span><span class="p">:</span>
    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">implementation</span><span class="p">):</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_implementation</span> <span class="o">=</span> <span class="n">implementation</span>

    <span class="k">def</span> <span class="nf">execute</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_implementation</span><span class="o">.</span><span class="n">operation</span><span class="p">()</span>

<span class="n">abstraction_a</span> <span class="o">=</span> <span class="n">Abstraction</span><span class="p">(</span><span class="n">ConcreteImplementationA</span><span class="p">())</span>
<span class="n">abstraction_b</span> <span class="o">=</span> <span class="n">Abstraction</span><span class="p">(</span><span class="n">ConcreteImplementationB</span><span class="p">())</span>

<span class="nb">print</span><span class="p">(</span><span class="n">abstraction_a</span><span class="o">.</span><span class="n">execute</span><span class="p">())</span>  <span class="c1"># Implementation A</span>
<span class="nb">print</span><span class="p">(</span><span class="n">abstraction_b</span><span class="o">.</span><span class="n">execute</span><span class="p">())</span>  <span class="c1"># Implementation B</span>
</pre></div></div></div>