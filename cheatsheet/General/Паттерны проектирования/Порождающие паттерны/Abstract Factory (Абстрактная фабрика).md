<h1>Abstract Factory (Абстрактная фабрика)</h1>
<p><strong>Описание</strong>: Предоставляет интерфейс для создания семейств связанных объектов без указания их конкретных классов.</p>
<p><strong>Когда использовать</strong>: Когда нужно создавать семейства объектов, которые должны использоваться вместе.</p>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="k">class</span> <span class="nc">AbstractProductA</span><span class="p">:</span>
    <span class="k">def</span> <span class="nf">do_something</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
        <span class="k">pass</span>

<span class="k">class</span> <span class="nc">ConcreteProductA1</span><span class="p">(</span><span class="n">AbstractProductA</span><span class="p">):</span>
    <span class="k">def</span> <span class="nf">do_something</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
        <span class="k">return</span> <span class="s2">&quot;Product A1&quot;</span>

<span class="k">class</span> <span class="nc">ConcreteProductA2</span><span class="p">(</span><span class="n">AbstractProductA</span><span class="p">):</span>
    <span class="k">def</span> <span class="nf">do_something</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
        <span class="k">return</span> <span class="s2">&quot;Product A2&quot;</span>

<span class="k">class</span> <span class="nc">AbstractFactory</span><span class="p">:</span>
    <span class="k">def</span> <span class="nf">create_product_a</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
        <span class="k">pass</span>

<span class="k">class</span> <span class="nc">ConcreteFactory1</span><span class="p">(</span><span class="n">AbstractFactory</span><span class="p">):</span>
    <span class="k">def</span> <span class="nf">create_product_a</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
        <span class="k">return</span> <span class="n">ConcreteProductA1</span><span class="p">()</span>

<span class="k">class</span> <span class="nc">ConcreteFactory2</span><span class="p">(</span><span class="n">AbstractFactory</span><span class="p">):</span>
    <span class="k">def</span> <span class="nf">create_product_a</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
        <span class="k">return</span> <span class="n">ConcreteProductA2</span><span class="p">()</span>

<span class="n">factory1</span> <span class="o">=</span> <span class="n">ConcreteFactory1</span><span class="p">()</span>
<span class="n">product_a1</span> <span class="o">=</span> <span class="n">factory1</span><span class="o">.</span><span class="n">create_product_a</span><span class="p">()</span>
<span class="nb">print</span><span class="p">(</span><span class="n">product_a1</span><span class="o">.</span><span class="n">do_something</span><span class="p">())</span>  <span class="c1"># Product A1</span>

<span class="n">factory2</span> <span class="o">=</span> <span class="n">ConcreteFactory2</span><span class="p">()</span>
<span class="n">product_a2</span> <span class="o">=</span> <span class="n">factory2</span><span class="o">.</span><span class="n">create_product_a</span><span class="p">()</span>
<span class="nb">print</span><span class="p">(</span><span class="n">product_a2</span><span class="o">.</span><span class="n">do_something</span><span class="p">())</span>  <span class="c1"># Product A2</span>
</pre></div></div></div>