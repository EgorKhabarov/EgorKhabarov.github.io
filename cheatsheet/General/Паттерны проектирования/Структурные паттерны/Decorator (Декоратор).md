<h2>Decorator (Декоратор)</h2>
<p><strong>Описание:</strong> Позволяет динамически добавлять новое поведение объектам, оборачивая их в класс-оболочку.</p>
<p><strong>Когда использовать:</strong> Когда нужно добавлять дополнительные функциональности объектам без изменения их класса.</p>
<p><strong>Пример реализации:</strong></p>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="k">class</span> <span class="nc">Component</span><span class="p">:</span>
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