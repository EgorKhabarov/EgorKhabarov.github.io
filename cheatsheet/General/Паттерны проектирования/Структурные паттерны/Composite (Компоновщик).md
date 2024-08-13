<h3>Composite (Компоновщик)</h3>
<p>Паттерн Компоновщик позволяет работать с группами объектов так же, как с отдельными объектами.
Это удобно для представления иерархических структур.</p>
<div class="code-element">
    <div class="lang-line">
        <text>python</text>
        <button class="copy-button"
        onclick="copyCode(this)">
    <svg stroke="currentColor"
         fill="none"
         stroke-width="2"
         viewBox="0 0 24 24"
         stroke-linecap="round"
         stroke-linejoin="round"
         class="h-4 w-4"
         height="1em"
         width="1em"
         xmlns="http://www.w3.org/2000/svg">
        <path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path>
        <rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect>
    </svg>
    <text>Copy code</text>
</button>

    </div>
    <div class="code"><div class="highlight"><pre><span></span><span class="k">class</span> <span class="nc">Graphic</span><span class="p">:</span>
    <span class="k">def</span> <span class="nf">render</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
        <span class="k">pass</span>

<span class="k">class</span> <span class="nc">Line</span><span class="p">(</span><span class="n">Graphic</span><span class="p">):</span>
    <span class="k">def</span> <span class="nf">render</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
        <span class="nb">print</span><span class="p">(</span><span class="s2">&quot;Rendering a line&quot;</span><span class="p">)</span>

<span class="k">class</span> <span class="nc">Rectangle</span><span class="p">(</span><span class="n">Graphic</span><span class="p">):</span>
    <span class="k">def</span> <span class="nf">render</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
        <span class="nb">print</span><span class="p">(</span><span class="s2">&quot;Rendering a rectangle&quot;</span><span class="p">)</span>

<span class="k">class</span> <span class="nc">GraphicGroup</span><span class="p">(</span><span class="n">Graphic</span><span class="p">):</span>
    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">graphics</span> <span class="o">=</span> <span class="p">[]</span>

    <span class="k">def</span> <span class="nf">add</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">graphic</span><span class="p">):</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">graphics</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">graphic</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">render</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
        <span class="k">for</span> <span class="n">graphic</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">graphics</span><span class="p">:</span>
            <span class="n">graphic</span><span class="o">.</span><span class="n">render</span><span class="p">()</span>

<span class="c1"># Использование</span>
<span class="n">group</span> <span class="o">=</span> <span class="n">GraphicGroup</span><span class="p">()</span>
<span class="n">group</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">Line</span><span class="p">())</span>
<span class="n">group</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">Rectangle</span><span class="p">())</span>
<span class="n">group</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">Line</span><span class="p">())</span>

<span class="n">group</span><span class="o">.</span><span class="n">render</span><span class="p">()</span>
</pre></div></div>
</div>