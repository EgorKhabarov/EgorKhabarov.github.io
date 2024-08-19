<h3>Builder (Строитель)</h3>
<p>Паттерн Строитель используется для пошагового создания сложных объектов.
Он отделяет конструирование объекта от его представления,
так что один и тот же процесс создания может создавать разные представления.</p>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code"><div class="highlight"><pre><span></span><span class="k">class</span> <span class="nc">House</span><span class="p">:</span>
    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">walls</span> <span class="o">=</span> <span class="kc">None</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">roof</span> <span class="o">=</span> <span class="kc">None</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">doors</span> <span class="o">=</span> <span class="kc">None</span>

    <span class="k">def</span> <span class="fm">__str__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
        <span class="k">return</span> <span class="sa">f</span><span class="s2">&quot;Walls: </span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">walls</span><span class="si">}</span><span class="s2">, Roof: </span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">roof</span><span class="si">}</span><span class="s2">, Doors: </span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">doors</span><span class="si">}</span><span class="s2">&quot;</span>

<span class="k">class</span> <span class="nc">HouseBuilder</span><span class="p">:</span>
    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">house</span> <span class="o">=</span> <span class="n">House</span><span class="p">()</span>

    <span class="k">def</span> <span class="nf">build_walls</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">walls</span><span class="p">):</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">house</span><span class="o">.</span><span class="n">walls</span> <span class="o">=</span> <span class="n">walls</span>
        <span class="k">return</span> <span class="bp">self</span>

    <span class="k">def</span> <span class="nf">build_roof</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">roof</span><span class="p">):</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">house</span><span class="o">.</span><span class="n">roof</span> <span class="o">=</span> <span class="n">roof</span>
        <span class="k">return</span> <span class="bp">self</span>

    <span class="k">def</span> <span class="nf">build_doors</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">doors</span><span class="p">):</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">house</span><span class="o">.</span><span class="n">doors</span> <span class="o">=</span> <span class="n">doors</span>
        <span class="k">return</span> <span class="bp">self</span>

    <span class="k">def</span> <span class="nf">get_house</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">house</span>

<span class="c1"># Использование</span>
<span class="n">builder</span> <span class="o">=</span> <span class="n">HouseBuilder</span><span class="p">()</span>
<span class="n">house</span> <span class="o">=</span> <span class="n">builder</span><span class="o">.</span><span class="n">build_walls</span><span class="p">(</span><span class="s2">&quot;Brick walls&quot;</span><span class="p">)</span><span class="o">.</span><span class="n">build_roof</span><span class="p">(</span><span class="s2">&quot;Tile roof&quot;</span><span class="p">)</span><span class="o">.</span><span class="n">build_doors</span><span class="p">(</span><span class="s2">&quot;Wooden doors&quot;</span><span class="p">)</span><span class="o">.</span><span class="n">get_house</span><span class="p">()</span>
<span class="nb">print</span><span class="p">(</span><span class="n">house</span><span class="p">)</span>
</pre></div></div></div>