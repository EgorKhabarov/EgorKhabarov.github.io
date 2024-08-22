<h3>Bridge (Мост)</h3>
<p>Паттерн Мост используется для разделения абстракции и её реализации, позволяя изменять их независимо.
Это достигается использованием интерфейсов или абстрактных классов.</p>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="k">class</span> <span class="nc">DrawingAPI</span><span class="p">:</span>
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
</pre></div></div></div>