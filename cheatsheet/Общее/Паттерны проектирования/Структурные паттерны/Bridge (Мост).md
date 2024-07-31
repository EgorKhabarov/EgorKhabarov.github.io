<h3>Bridge (Мост)</h3>
<p>Паттерн Мост используется для разделения абстракции и её реализации, позволяя изменять их независимо.
Это достигается использованием интерфейсов или абстрактных классов.</p>
<div class="code-element">
<div class="lang-line">
  <text>python</text>
  <button class="copy-button"
          id="code4b3e45b1239ad908f531d7ebb6482976b"
          onclick="copyCode(code4b3e45b1239ad908f531d7ebb6482976, code4b3e45b1239ad908f531d7ebb6482976b)">
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
<div class="code" id="code4b3e45b1239ad908f531d7ebb6482976"><div class="highlight"><pre><span></span><span class="k">class</span> <span class="nc">DrawingAPI</span><span class="p">:</span>
    <span class="k">def</span> <span class="nf">draw_circle</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">x</span><span class="p">,</span> <span class="n">y</span><span class="p">,</span> <span class="n">radius</span><span class="p">):</span>
        <span class="k">pass</span>

<span class="k">class</span> <span class="nc">DrawingAPI1</span><span class="p">(</span><span class="n">DrawingAPI</span><span class="p">):</span>
    <span class="k">def</span> <span class="nf">draw_circle</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">x</span><span class="p">,</span> <span class="n">y</span><span class="p">,</span> <span class="n">radius</span><span class="p">):</span>
        <span class="nb">print</span><span class="p">(</span><span class="sa">f</span><span class="s2">&quot;API1.circle at (</span><span class="si">{</span><span class="n">x</span><span class="si">}</span><span class="s2">, </span><span class="si">{</span><span class="n">y</span><span class="si">}</span><span class="s2">), radius </span><span class="si">{</span><span class="n">radius</span><span class="si">}</span><span class="s2">&quot;</span><span class="p">)</span>

<span class="k">class</span> <span class="nc">DrawingAPI2</span><span class="p">(</span><span class="n">DrawingAPI</span><span class="p">):</span>
    <span class="k">def</span> <span class="nf">draw_circle</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">x</span><span class="p">,</span> <span class="n">y</span><span class="p">,</span> <span class="n">radius</span><span class="p">):</span>
        <span class="nb">print</span><span class="p">(</span><span class="sa">f</span><span class="s2">&quot;API2.circle at (</span><span class="si">{</span><span class="n">x</span><span class="si">}</span><span class="s2">, </span><span class="si">{</span><span class="n">y</span><span class="si">}</span><span class="s2">), radius </span><span class="si">{</span><span class="n">radius</span><span class="si">}</span><span class="s2">&quot;</span><span class="p">)</span>

<span class="k">class</span> <span class="nc">Circle</span><span class="p">:</span>
    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">x</span><span class="p">,</span> <span class="n">y</span><span class="p">,</span> <span class="n">radius</span><span class="p">,</span> <span class="n">drawing_api</span><span class="p">):</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">x</span> <span class="o">=</span> <span class="n">x</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">y</span> <span class="o">=</span> <span class="n">y</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">radius</span> <span class="o">=</span> <span class="n">radius</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">drawing_api</span> <span class="o">=</span> <span class="n">drawing_api</span>

    <span class="k">def</span> <span class="nf">draw</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">drawing_api</span><span class="o">.</span><span class="n">draw_circle</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">x</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">y</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">radius</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">scale</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">factor</span><span class="p">):</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">radius</span> <span class="o">*=</span> <span class="n">factor</span>

<span class="c1"># Использование</span>
<span class="n">circle1</span> <span class="o">=</span> <span class="n">Circle</span><span class="p">(</span><span class="mi">1</span><span class="p">,</span> <span class="mi">2</span><span class="p">,</span> <span class="mi">3</span><span class="p">,</span> <span class="n">DrawingAPI1</span><span class="p">())</span>
<span class="n">circle1</span><span class="o">.</span><span class="n">draw</span><span class="p">()</span>

<span class="n">circle2</span> <span class="o">=</span> <span class="n">Circle</span><span class="p">(</span><span class="mi">5</span><span class="p">,</span> <span class="mi">7</span><span class="p">,</span> <span class="mi">11</span><span class="p">,</span> <span class="n">DrawingAPI2</span><span class="p">())</span>
<span class="n">circle2</span><span class="o">.</span><span class="n">draw</span><span class="p">()</span>
</pre></div></div>
</div>